# Name(s): Shelby Sash, Sidney Huschart, Andrew Mehlman
# email: sashsk@mail.uc.edu, huschash@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: November 7,2024
# Course #/Section: IS4010/ 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using github to connect to a databse and extract results
# Brief Description of what this module does: Produces a randomized output of product descriptions 
# Citations: stack overflow
# Anything else that's relevant: N/A

#main.py

from dbUtilitiesPackage.dbUtilities import *

import random  #for step 2

import pyodbc


try:
    conn= connect_to_database() 
    # Submit a query to the SQL Server instance and store the results in the cursor object
    cursor = conn.cursor()  #establishes temporary table 
    cursor.execute('SELECT * FROM tProduct') #submits sql to db engine and stores in cursor
except Exception as e: 
    #I'd like to know more
    print("error accessing database")
    print(e) 
    exit()  #given up. how do i get out of this module 
    

#step 1
query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
#print(query_string)
#Submit the query to out db server and store the results in a variable
results = cursor.execute(query_string)
products = cursor.fetchall()  #maybe ?

#step 2
selectedProduct = random.choice(products)
productID = selectedProduct.ProductID
description = selectedProduct.Description
manufacturerID = selectedProduct.ManufacturerID
brandID = selectedProduct.BrandID

#step 3 & step 4
query_manufacturer = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturerID}"
cursor.execute(query_manufacturer)
manufacturer = cursor.fetchone().Manufacturer

#step 5
query_brand = f"SELECT Brand FROM tBrand WHERE BrandID = {brandID}"
cursor.execute(query_brand)
brand = cursor.fetchone().Brand

#step 6 -- given query
query_items_sold = f"""
SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
FROM dbo.tTransactionDetail
INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {productID})
"""
cursor.execute(query_items_sold)
itemsSold = cursor.fetchone().NumberOfItemsSold

#step 7 THIS IS THE ONLY OUTPUT
#Product Description, Manufacturer, Brand, and Number of Items Sold

sentence1= (f"The product is {brand}.")
print(sentence1)
sentence2= (f"It is manufactured by {manufacturer}")
print(sentence2)
sentence3=(f"It is described as having {description}")
print(sentence3)



