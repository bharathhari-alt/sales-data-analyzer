import pandas as pd
import matplotlib.pyplot as plt



# Load data
df = pd.read_csv("C:\\Users\\bhara\\OneDrive\\Desktop\\Book1.csv")

# Show data
print("Data:")
print(df)

# Total sales
total_sales = df["amount"].sum()
print("\nTotal Sales:", total_sales)

# Sales by product
sales_by_product = df.groupby("product")["amount"].sum()
print("\nSales by Product:")
print(sales_by_product)

sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.show()