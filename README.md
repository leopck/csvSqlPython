# csvSqlPython (Really should have named it better... It just helps transforming data from CSV format to SQL format)

## Converting csv files to SQL using Python demo project

### Using Pandas

This is a simple project to demonstrate the use of Python Anaconda or Pandas for parsing or extracting csv files and converting it into SQL language.

By converting the csv files into SQL, it provides a faster means as well as a simpler way to control the datas inside the csv files. Since SQL handles all the algorithms and difficult data arrangement and joinings of datas, SQL would be one of the few good solutions to solve data management in Python.

Therefore in this project, we will be looking into Python pandas library to convert csv files into SQL to simplify the data handling.

### Getting Started

```
pip install -r requirements.txt
python example/test.py
```

### Some details for the script


`function`: makeFileIntoSQL(file, nameoftable, sqlengine)

`Usage`   : converts csv files into SQL files

`Example` : makeFileIntoSQL('file1.csv', 'augdata', disk_engine) 

``##  augdata is the name of the table in the SQL, you can rename this to whatever you like. This would affect the SQL queries.``

**From pandas library**


`function`: pandas.read_sql_query('SELECT * FROM augdata', create_engine('sqlite:///name.db'))

`Usage`   : make SQL query and save the results into a variable

`Example` : df = pd.read_sql_query('SELECT * FROM augdata', disk_engine)

### Usage

1. Create an SQL engine and import sqlalchemy and pandas

				from sqlalchemy import create_engine
                import pandas as pd

				disk_engine = create_engine('sqlite:///awesome.db')

2. import csvtosql and select the csv files that you want to convert into SQL tables and pass to the makeFileIntoSQL the disk_engine

				import csvtosql as cs
                cs.makeFileIntoSQL('file1.csv', 'data', disk_engine)

3. Run your normal SQL queries as usual! Just perform each SQL queries using pandas library.

				data = pd.read_sql_query('SELECT * FROM augdata', disk_engine)
                print data ## To view the output of the query

4. If you have more than one csv files that you want to parse then just add into the makeFileIntoSQL()
				
                cs.makeFileIntoSQL('file2.csv', 'data2', disk_engine)
                data2 = pd.read_sql_query('SELECT * FROM data2', disk_engine)
                print data2

5. Your code should look like this now:
				
                import csvtosql as cs
                import pandas as pd
                from sqlalchemy import create_engine
                
                disk_engine = create_engine('sqlite:///awesome.db')
                cs.makeFileIntoSQL('file1.csv', 'data', disk_engine)
                
                data = pd.read_sql_query('SELECT * FROM data', disk_engine)
                print data
                
                cs.makeFileIntoSQL('file2.csv', 'data2', disk_engine)
                data2 = pd.read_sql_query('SELECT * FROM data2', disk_engine)
                print data2                
                
                
Fin. Enjoy your SQL querying.








