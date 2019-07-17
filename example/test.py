import os, sys
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '../lib')))

from csvtosql import CSVtoSQL as CtoS
import pandas as pd
from sqlalchemy import create_engine

######### Opening File and Creating sqlite engine #########

file1 = open(abspath(join(dirname(__file__), "./file1.csv")), "r")
file2 = open(abspath(join(dirname(__file__), "./file2.csv")), "r")
disk_engine = create_engine('sqlite:///awesome.db')

######### Initialize Class #########
cs = CtoS()

cs.makeFileIntoSQL(file1, 'data', disk_engine)
data = pd.read_sql_query('SELECT * FROM data', disk_engine)
print (data)

cs.makeFileIntoSQL(file2, 'data2', disk_engine)
data2 = pd.read_sql_query('SELECT * FROM data2', disk_engine)
print (data2)
