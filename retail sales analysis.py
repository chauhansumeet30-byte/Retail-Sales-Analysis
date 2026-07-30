1. monthly_sales_trend 

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sample sales.csv",encoding="latin1")
df.columns=df.columns.str.strip().str.lower()

df["order date"]=pd.to_datetime(df["order date"],errors="coerce")
df=df.dropna(subset=["order date"])


df["month"]=df["order date"].dt.month

monthly_sales=df.groupby("month")["sales"].sum().reset_index()

plt.plot(monthly_sales["month"],monthly_sales["sales"])
plt.xlabel("month")
plt.ylabel("sales")
plt.title("monthly sales trend")
plt.show()


2.category_analysis

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sample sales.csv",encoding="latin1")
df.columns=df.columns.str.strip().str.lower()

category_sales=df.groupby("category")["sales"].sum().reset_index()

plt.bar(category_sales["category"],category_sales["sales"])
plt.xlabel("categories")
plt.ylabel("sales")
plt.title("sales by category")
plt.show()


3. region_wise_sales

import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv("sample sales.csv",encoding="latin1")
df.columns=df.columns.str.strip().str.lower()

region_sales=df.groupby("region")["sales"].sum().reset_index()

plt.bar(region_sales["region"],region_sales["sales"])
plt.xlabel("region")
plt.ylabel("sales")
plt.title("region-wise Sales")
plt.show()


4. high_profit_orders

import pandas as pd
df=pd.read_csv("sample sales.csv",encoding="latin1")
df.columns=df.columns.str.strip().str.lower()

high_profit_orders=df[df["profit"]>500]
print(high_profit_orders)

high_profit_orders.to_csv("high profit orders.csv")