import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Excel Dashboard")

# Upload Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
if uploaded_file:
    # Read Excel file
    data = pd.read_excel(uploaded_file)
    
    st.subheader("Raw Data")
    st.dataframe(data)
    
    # Example: display numeric column options
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        st.subheader("Charts")
        col = st.selectbox("Select column to visualize", numeric_cols)
        chart_type = st.radio("Chart type", ("Bar", "Line"))
        
        if chart_type == "Bar":
            fig = px.bar(data, x=data.index, y=col)
        else:
            fig = px.line(data, x=data.index, y=col)
        
        st.plotly_chart(fig)
