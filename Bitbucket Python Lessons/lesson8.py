# -*- coding: utf-8 -*-
"""
Lesson 8

Pulling data from a Microsoft SQL database
"""

from pandas import DataFrame, date_range, concat
import pandas as pd
import sys
from sqlalchemy import create_engine, MetaData, Table, select

'''
Version 1
In this section we use the sqlalchemy library to grab data from a sql database
'''

# Parameters
ServerName = "PMSISQL06"
Database =  "Smiths_Dev"
TableName = "Main_Sales"

# Create the connection
engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database)
conn = engine.connect()

# Required for querying tables
metadata = MetaData(conn)

# Table to query
tbl = Table(TableName, metadata, autoload=True, schema="dbo")
#tbl.create(checkfirst=)