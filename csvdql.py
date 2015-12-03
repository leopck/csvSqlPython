import pandas as pd
from sqlalchemy import create_engine # database connection
import datetime as dt
from IPython.display import display

# import plotly.plotly as py # interactive graphing
# from plotly.graph_objs import Bar, Scatter, Marker, Layout

# display(pd.read_csv('Aug14.csv'))
disk_engine = create_engine('sqlite:///awesome.db')

def makeFileIntoSQL(myFile, sqlName):
    chunksize = 20000
    j = 0
    index_start = 1
    for df in pd.read_csv(myFile, chunksize=chunksize, iterator=True, encoding='utf-8'):
        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns
        df.index += index_start
        df.to_sql(sqlName, disk_engine, if_exists='replace')
        index_start = df.index[-1] + 1


makeFileIntoSQL('Aug14.csv', 'data')
makeFileIntoSQL('July01.csv', 'julydata')

df = pd.read_sql_query('SELECT * FROM data LIMIT 3', disk_engine)
print df

df_july = pd.read_sql_query('SELECT * FROM julydata LIMIT 3', disk_engine)
print df_july
#
# df = pd.read_sql_query('SELECT STATE FROM data LIMIT 50', disk_engine)
# df.head()
#
# df = pd.read_sql_query('SELECT STATE, COUNT(*) as `num_complaints`'
#                        'FROM data '
#                        'GROUP BY SYMPTOM_ERROR_CODE', disk_engine)
# df.head()
#
# df = pd.read_sql_query('SELECT STATE, COUNT(*) as `num_complaints`'
#                        'FROM data '
#                        'GROUP BY STATE '
#                        'ORDER BY -num_complaints', disk_engine)

# py.iplot([Bar(x=df.STATE, y=df.num_complaints)], filename='awesome1/most common complaints by state')
