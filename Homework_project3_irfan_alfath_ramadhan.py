import json
import psycopg2 as pg
from zipfile import ZipFile
from sqlalchemy import true
import pandas as pd


schema_json = 'D:Belajar_Python/user_address.json'
create_schema_sql = """create table user_address_2018_snapshots {};"""
zip_small_file = 'D:Belajar_Python/dataset-small.zip'
small_file_name = 'dataset-small.csv'


with open (schema_json, 'r') as schema:
    content = json.loads(schema.read())
list_schema = []
for c in content:
    col_name =  c['column_name']
    col_type = c['column_type']
    constraint = c['is_null_able']
    ddl_list = [col_name, col_type, constraint]
    list_schema.append(ddl_list)        
    
list_schema2 = []
for s in list_schema:
    l = ' '.join(s)
    list_schema2.append(l)

create_schema_sql = """create table user_address_2018_snapshots {};"""
create_schema_sql_final = create_schema_sql.format(tuple(list_schema2)).replace("'", "")


#innit postgres conn
conn = pg.connect(database= 'shipping_orders',
                  user= 'postgres',
                  password= 'admin',
                  host= '127.0.0.1',
                  port='5432') 

conn.autocommit=True  
cursor=conn.cursor()
try:
    cursor.execute(create_schema_sql_final)
    print("ddl schema has sussecfully created...")
except pg.errors.DuplicateTable:
    print("table already exists...")

#load zipped file to dataframe
zf = ZipFile(zip_small_file)
df = pd.read_csv(zf.open(small_file_name))
print(df.head())