# csvSqlPython

## Converting csv files to SQL using Python demo project

This is a simple project to demonstrate the use of Python Anaconda or Pandas for parsing or extracting csv files and converting it into SQL language.

By converting the csv files into SQL, it provides a faster means as well as a simpler way to control the datas inside the csv files. Since SQL handles all the algorithms and difficult data arrangement and joinings of datas, SQL would be one of the few good solutions to solve data management in Python.

Therefore in this project, we will be looking into Python pandas library to convert csv files into SQL to simplify the data handling.

### How to use the python script

1. Install Anaconda `(https://www.continuum.io/downloads)`
2. git clone this project or download the zip file of this project.
3. Run `ipython csvtosql.py`

### Understanding the script

def makeFileIntoSQL(myFile, sqlName):
    chunksize = 20000
    j = 0
    index_start = 1
    for df in pd.read_csv(myFile, chunksize=chunksize, iterator=True, encoding='utf-8'):
        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
        df.index += index_start
        df.to_sql(sqlName, disk_engine, if_exists='replace')
        index_start = df.index[-1] + 1






