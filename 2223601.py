def run() :     
    # import modules here 
    import pandas as pd  # type: ignore
    import numpy as np # type: ignore

    # logic 
    df = pd.read_csv(r"C:\Users\S42104\Desktop\bajaj\Data Engineering\data - sample.xlsx")
    print(df.head())
    
    return(df)
import mysql.connector as c
conn= c.connect()

