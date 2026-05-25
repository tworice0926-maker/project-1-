import pandas as pd

file_path = 'SuperMarket_Analysis.csv'
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()
sales_col = 'Sales' if 'Sales' in df.columns else 'Total'

print("========== 1. 檢視資料 ==========")
print(f"資料總筆數: {len(df)}")
print("前 5 筆資料內容:")
print(df.head())
print("\n")

print("========== 2. 篩選資料 ==========")
filtered_df = df[(df['Branch'] == 'A') & (df['Customer type'] == 'Member')]
print(f"符合 Branch='A' 且 Customer type='Member' 的資料共有: {len(filtered_df)} 筆")
print(filtered_df.head())
print("\n")

print("========== 3. 產品線銷售與評分彙總 ==========")
product_summary = df.groupby('Product line').agg(
    Sales=(sales_col, 'sum'),
    Rating=('Rating', 'mean')
).round(2)
print(product_summary)
print("\n")

print("========== 4. 城市與性別分組彙總 ==========")
city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=(sales_col, 'mean'),
    Transaction_Count=('Invoice ID', 'count')
).round(2)
print(city_gender_summary)
print("\n")

print("========== 5. 最高銷售額產品線 ==========")
best_product_line = product_summary['Sales'].idxmax()
best_sales_amount = product_summary['Sales'].max()
print(f"總銷售額最高的產品線為: {best_product_line} (總銷售額: {best_sales_amount})")
print("\n")

output_filename = '0520_pandas_3OK.CSV'
product_summary.to_csv(output_filename)
print(f"========== 檔案已成功輸出為 {output_filename} (已計算至小數後2位) ==========")