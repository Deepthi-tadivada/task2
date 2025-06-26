import pandas as pd
import pyodbc
import configparser
 
#loaded data that required df ,increment_data
# Read configuration details from config.ini
config = configparser.ConfigParser()
config.read(r'C:\Users\Deepthi\Desktop\python_tasks\TASK4\config.ini')
 
# Extract database connection details
db_config = config['ssms']
 
# Use a context manager for the connection
with pyodbc.connect(
    f"DRIVER={db_config['DRIVER']};"
    f"SERVER={db_config['SERVER']};"
    f"DATABASE={db_config['DATABASE']};"
    f"UID={db_config['UID']};"
    f"PWD={db_config['PWD']};"
) as conn:
    # Query Customers table
    query_orders = "SELECT * FROM sales.orders;"
    orders_df = pd.read_sql(query_orders, conn)
    order_items="select *from sales.order_items"
    order_items=pd.read_sql(order_items,conn)  
    df=orders_df.merge(order_items, on="order_id", how="inner")
    IncrementOrders="select * from dbo.IncrementOrders"
    IncrementOrders_df=pd.read_sql(IncrementOrders,conn)
    updated_orders="select * from dbo.updated_orders"
    updated_orders_df=pd.read_sql(updated_orders,conn)
    
    
# df ---main data
# IncrementOrders_df ---increment_data

print(updated_orders_df)