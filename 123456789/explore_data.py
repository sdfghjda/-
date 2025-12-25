import pandas as pd

# 读取Excel文件
file_path = '两版合并后的年报数据_完整版.xlsx'
df = pd.read_excel(file_path)

# 显示数据的基本信息
print("数据基本信息：")
print(df.info())

# 显示数据的前几行
print("\n数据前5行：")
print(df.head())

# 显示所有列名
print("\n所有列名：")
print(df.columns.tolist())

# 显示年份范围
if '年份' in df.columns:
    print("\n年份范围：")
    print(f"最小值：{df['年份'].min()}")
    print(f"最大值：{df['年份'].max()}")

# 显示股票代码的数量
if '股票代码' in df.columns:
    print("\n股票代码数量：")
    print(f"唯一股票代码数：{df['股票代码'].nunique()}")
    print(f"前10个股票代码：{df['股票代码'].unique()[:10]}")