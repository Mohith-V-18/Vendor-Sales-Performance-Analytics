import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import numpy as np
import logging
from ingestion_db import ingest_db


logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    '''this function will merge the different tables to get the overall vendor summary and adding new columns in resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary as (
    SELECT "VendorNumber", SUM("Freight") as "FreightCost"
            FROM vendor_invoice
            GROUP BY "VendorNumber"),
    
    PurchaseSummary as ( SELECT
    p."VendorNumber",
    p."VendorName",
    p."Brand",
    p."Description",
    AVG(p."PurchasePrice") as "PurchasePrice",
    pp."Volume",
    AVG(pp."Price") as "ActualPrice",
    SUM(p."Quantity") as "TotalPurchaseQuantity",
    SUM(p."Dollars") as "TotalPurchaseDollars"
    FROM purchases as p
    JOIN purchase_prices as pp
    ON p."Brand" = pp."Brand"
    WHERE p."PurchasePrice" > 0
    GROUP BY p."VendorNumber", p."VendorName", p."Brand", p."Description", pp."Volume"),
    
    SalesSummary as (SELECT
    "VendorNo",
    "Brand",
    SUM("SalesQuantity") as "TotalSalesQuantity",
    SUM("SalesDollars") as "TotalSalesDollars",
    AVG("SalesPrice") as "SalesPrice",
    SUM("ExciseTax") as "TotalSalesExciseTax"
    FROM sales
    GROUP BY "VendorNo", "Brand")
    
    SELECT
        ps."VendorNumber",
        ps."VendorName",
        ps."Brand",
        ps."Description",
        ps."Volume",
        ps."PurchasePrice",
        ps."ActualPrice",
        ps."TotalPurchaseQuantity",
        ps."TotalPurchaseDollars",
        ss."SalesPrice",
        ss."TotalSalesQuantity",
        ss."TotalSalesDollars",
        ss."TotalSalesExciseTax",
        fs."FreightCost"
    FROM PurchaseSummary as ps
    LEFT JOIN SalesSummary as ss
    ON ps."VendorNumber" = ss."VendorNo" AND ps."Brand" = ss."Brand"
    LEFT JOIN FreightSummary as fs
    ON ps."VendorNumber" = fs."VendorNumber"
    ORDER BY ps."TotalPurchaseDollars" DESC """, conn)

    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    #changing the datatype to float
    df['Volume'] = df["Volume"].astype("float64")

    #filling missing value with 0
    df.fillna(0, inplace=True)

    #removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #creating new columns for better analysis
    df["GrossProfit"] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df["ProfitMargin"] = (df['GrossProfit']/df['TotalSalesDollars'])*100
    df["StockTurnOver"] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    df["SalestoPurchaseRatio"] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

    #filling infinity values with 0(new columns)
    vendor_sales_summary.replace([np.inf, -np.inf], 0 , inplace = True)

    return df

if __name__=='__main__':
    username="postgres"
    password=quote_plus("Mohith@23")
    host="localhost"
    port="5432"
    database="inventory"

    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
    conn=engine.connect()

    logging.info('Creating Vendor Summary Table......')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())
    
    logging.info('Cleaning Data....')
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data....')
    ingest_db(clean_df, "vendor_sales_summary", conn)
    logging.info('Completed')
    
