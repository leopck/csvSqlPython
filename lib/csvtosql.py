import pandas as pd
from sqlalchemy import create_engine # database connection

############################################
# uncomment this below if you want to see the output the of data in a table
# from IPython.display import display
# display(pd.read_csv('file1.csv'))
############################################

class CSVtoSQL:
        def __init__(self):
                pass

        def makeFileIntoSQL(self, filename, sqlName, sqlEngine):
                chunksize = 20000
                j = 0
                index_start = 1
                for df in pd.read_csv(filename, chunksize=chunksize, iterator=True, encoding='utf-8'):
                        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns
                        df.index += index_start
                        df.to_sql(sqlName, sqlEngine, if_exists='append') ##change to if_exists='replace' if you don't want to replace the database file
                        index_start = df.index[-1] + 1

if __name__ == "__main__":
    ##Create sqlite engine
    disk_engine = create_engine('sqlite:///awesome.db')

    ##Start class
    cs = CSVtoSQL()

    ##Converting files into SQL tables
    cs.makeFileIntoSQL('file1.csv', 'augdata', disk_engine)
    cs.makeFileIntoSQL('file2.csv', 'julydata', disk_engine)

    ##Examples of SQL queries
    ##Example 1
    df = pd.read_sql_query('SELECT * FROM augdata', disk_engine)
    print ("This is data from file1.csv")
    print (df)
    print ("")

    ##Example 2
    df_july = pd.read_sql_query('SELECT * FROM julydata', disk_engine)
    print ("This is data from file2.csv")
    print (df_july)
    print ("")

    ##Example 3
    df = pd.read_sql_query('SELECT NAME FROM augdata', disk_engine)
    print ("This is data from file1.csv")
    print (df)
    print ("")

    ##Example 4
    df = pd.read_sql_query('SELECT AGE, COUNT(*) as `num_complaints`'
                           'FROM augdata '
                           'GROUP BY NAME', disk_engine)
    print ("This is data from file1.csv")
    print (df)
    print ("")

    ##Example 5
    df = pd.read_sql_query('SELECT ID, COUNT(*) as `num_complaints`'
                           'FROM augdata '
                           'GROUP BY BEING '
                           'ORDER BY -num_complaints', disk_engine)
    print ("This is data from file1.csv")
    print (df)
    print ("")
