import csvtosql as cs
import pandas as pd
from sqlalchemy import create_engine

disk_engine = create_engine('sqlite:///awesome.db')
cs.makeFileIntoSQL('file1.csv', 'data', disk_engine)

data = pd.read_sql_query('SELECT * FROM data', disk_engine)
print (data)

cs.makeFileIntoSQL('file2.csv', 'data2', disk_engine)
data2 = pd.read_sql_query('SELECT * FROM data2', disk_engine)
print (data2)
