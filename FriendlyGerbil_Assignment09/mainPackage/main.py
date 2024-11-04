# Name(s): Shelby Sash, Sidney Huschart, Andrew Mehlman
# email: sashsk@mail.uc.edu
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