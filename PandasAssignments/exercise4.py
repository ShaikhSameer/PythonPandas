import pandas as pd

df = pd.read_csv('data/sales_data.csv')
print(df)

"""
#
#   How much sale produced by each salesman
#
"""

sales_by_salesman = df.groupby('SalesRep').sum()['Units']
print("Sales by each salesman:\n", sales_by_salesman)


"""
#
#   Which salesman produced the best sale
#
"""

best_salesman = sales_by_salesman.idxmax()
print("\nBest salesman:", best_salesman)


"""
#
#   Display sale of each month
#
"""

sales_by_month = df.groupby('Date')['Units'].sum()
print("\nSales by each month:\n", sales_by_month)


"""
#
#   Find out the best month of sale
#
"""

best_month = sales_by_month.idxmax()
print("\nBest month of sale:", best_month)


"""
#
#   In which region we got the best sale
#
"""

best_region = df.groupby('Region')['Units'].sum().idxmax()
print("\nBest sales region:", best_region)


"""
#
#  What product sold the most
#
"""

most_sold_product = df.groupby('Product')['Units'].sum().idxmax()
print("\nMost sold product:", most_sold_product)
