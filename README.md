# csvSqlPython

## Converting csv files to SQL using Python demo project

This is a simple project to demonstrate the use of Python Anaconda or Pandas for parsing or extracting csv files and converting it into SQL language.

By converting the csv files into SQL, it provides a faster means as well as a simpler way to control the datas inside the csv files. Since SQL handles all the algorithms and difficult data arrangement and joinings of datas, SQL would be one of the few good solutions to solve data management in Python.

Therefore in this project, we will be looking into Python pandas library to convert csv files into SQL to simplify the data handling.



### How to use the python script

1. Install Anaconda `(https://www.continuum.io/downloads)`
2. git clone this project or download the zip file of this project.
3. Run `ipython csvtosql.py`



### Some details for the script


`function`: makeFileIntoSQL(file, nameoftable)

`Usage`   : converts csv files into SQL files

`Example` : makeFileIntoSQL('file1.csv', 'augdata') ##'augdata' is the name of the table in the SQL, you can rename this to whatever you like. This would affect the SQL queries.



**From pandas library**


`function`: pandas.read_sql_query('SELECT * FROM augdata', create_engine('sqlite:///name.db'))

`Usage`   : make SQL query and save the results into a variable

`Example` : df = pd.read_sql_query('SELECT * FROM augdata', disk_engine)







