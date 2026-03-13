

import streamlit as st
import pandas as pd
import plotly.express as px

# Tiêu đề Dashboard
st.title("Phân tích Mỹ phẩm Shopee 💄")

# Tạo thanh chọn hãng (Sidebar)
brand = st.sidebar.selectbox("Chọn thương hiệu:", ["Cocoon", "La Roche-Posay", "Estee Lauder"])

# Giả lập dữ liệu
data = pd.DataFrame({
    'Sản phẩm': ['Kem dưỡng', 'Serum', 'Sữa rửa mặt', 'Toner'],
    'Doanh số': [450, 300, 600, 200]
})

st.write(f"Đang hiển thị dữ liệu cho hãng: **{brand}**")

# Vẽ biểu đồ tương tác
fig = px.bar(data, x='Sản phẩm', y='Doanh số', color='Sản phẩm', title="Doanh số theo dòng sản phẩm")
st.plotly_chart(fig)

# Hiển thị bảng dữ liệu luật kết hợp (Apriori)
st.subheader("Luật kết hợp (Bán kèm)")
st.table(pd.DataFrame({
    'Sản phẩm A': ['Kem dưỡng'],
    'Sản phẩm B': ['Mặt nạ'],
    'Confidence': ['85%'],
    'Lift': [2.1]
}))
