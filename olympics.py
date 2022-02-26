import pyspark
import pandas as pd


spark = pyspark.sql.SparkSession(pyspark.SparkContext())


def excel_to_csv(name):
    pd.read_excel(name + '.xlsx').to_csv(name + '.csv', sep=',', index=False)


excel_to_csv('Atheletes')
