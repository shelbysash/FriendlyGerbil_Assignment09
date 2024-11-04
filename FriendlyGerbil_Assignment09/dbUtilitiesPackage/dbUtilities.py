# Name(s): Shelby Sash, Sidney Huschart, Andrew Mehlman
# email: sashsk@mail.uc.edu, huschash@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: November 7,2024
# Course #/Section: IS4010/ 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using github to connect to a databse and extract results 
# Brief Description of what this module does: Function for connecting to the SQL Server database 
# Citations: N/A
# Anything else that's relevant: N/A

#db utilities

import pyodbc

def connect_to_database():
    """
    Connect to the database
    @return Connecition Object: the open connection, or None on error
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;' 
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')  
    except: 
        conn = None  #failture 
        
    return conn

