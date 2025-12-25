try:
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    print("所有库安装成功！")
    print(f"Streamlit版本: {st.__version__}")
    print(f"Pandas版本: {pd.__version__}")
    print(f"Plotly版本: {px.__version__}")
except ImportError as e:
    print(f"导入错误: {e}")
