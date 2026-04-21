import pandas as pd
import matplotlib.pyplot as plt

def LoadData(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def ShowData(df):
    if df is not None:
        print("Data:")
        print(df)
    else:
        print("No data to display.")

def TotalSales(df):
    if df is not None:
        total_sales = df["amount"].sum()
        print("\nTotal Sales:", total_sales)
    else:
        print("No data to calculate total sales.")

def SalesByProduct(df):
    if df is not None:
        sales_by_product = df.groupby("product")["amount"].sum()
        print("\nSales by Product:")
        print(sales_by_product)
        

def BarChart(df):
    if df is not None:
        sales_by_product = df.groupby("product")["amount"].sum()
        sales_by_product.plot(kind='bar')
        plt.title("Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
    else:
        print("No data to create bar chart.")

def FilterData(df, product_name):
    if df is not None:
        filtered_data = df[df["product"] == product_name]
        print(f"\nData for {product_name}:")
        print(filtered_data)
    else:
        print("No data to filter.")

def sales_after_date(df, date):
    if df is not None:
        filtered_data = df[df["date"] > date]
        print(f"\nSales after {date}:")
        print(filtered_data)
    else:
        print("No data to filter.")

def main():
    df = LoadData("C:\\Users\\bhara\\OneDrive\\Desktop\\Book1.csv")
    df["date"] = pd.to_datetime(df["date"]) 
    ShowData(df)
    TotalSales(df)
    SalesByProduct(df)
    FilterData(df, "Laptop")
    sales_after_date(df, "2026-01-03")
    BarChart(df)

if __name__ == "__main__":
    main()