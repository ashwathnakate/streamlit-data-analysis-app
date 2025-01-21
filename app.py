import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Imports remain the same as above

# Add title and description
st.title('Data Analysis Application')
st.subheader('Explore datasets, visualize data, and gain insights! 📊')

# Create a dropdown list to choose a dataset
dataset_options = ['iris', 'titanic', 'tips', 'diamonds']
selected_dataset = st.selectbox('Select a dataset', dataset_options)

# Load the selected dataset
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df = sns.load_dataset('tips')
elif selected_dataset == 'diamonds':
    df = sns.load_dataset('diamonds')

# Button to upload a custom dataset
uploaded_file = st.file_uploader('Upload your dataset', type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Check file extension and process accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

# Display the dataset
st.write(df)

# Display the number of rows and columns
st.write('### Dataset Dimensions:')
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Display column names and data types
st.write('### Column Names and Data Types:')
st.write(df.dtypes)

# Identify and display null values
st.write('### Null Value Analysis:')
if df.isnull().sum().sum() > 0:
    st.write(df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No Null Values Detected.')

# Display summary statistics
st.write('### Summary Statistics:')
st.write(df.describe())

# Pairplot
# Create a pairplot
st.subheader('Pairplot')
# Validate if the dataset has enough numerical columns
numeric_columns = df.select_dtypes(include=np.number).columns

if len(numeric_columns) > 1:  # Ensure there are at least two numerical columns
    hue_column = st.selectbox('Column to be used for hue (optional)', [None] + list(df.columns))
    try:
        # Generate pairplot with or without hue
        if hue_column and hue_column != 'None':
            st.pyplot(sns.pairplot(df, hue=hue_column))
        else:
            st.pyplot(sns.pairplot(df))
    except Exception as e:
        st.warning(f"Could not generate pairplot: {e}")
else:
    st.warning("Not enough numerical columns to create a pairplot. The dataset must have at least two numerical columns.")


# Heatmap
st.subheader('📊 Correlation Heatmap')
numeric_columns = df.select_dtypes(include=np.number).columns
if len(numeric_columns) > 1:
    corr_matrix = df[numeric_columns].corr()
    heatmap_fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                           x=corr_matrix.columns,
                                           y=corr_matrix.columns,
                                           colorscale='Viridis'))
    st.plotly_chart(heatmap_fig)
else:
    st.write('Not enough numeric columns for correlation heatmap.')

# Distribution Plot
st.subheader('📊 Distribution Plot')
dist_column = st.selectbox('Select a column for Distribution Plot', df.columns)
if dist_column in df.select_dtypes(include=np.number).columns:
    fig, ax = plt.subplots()
    sns.histplot(df[dist_column], kde=True, ax=ax)
    st.pyplot(fig)
else:
    st.write(f"Column '{dist_column}' is not numeric. Please select a numeric column.")

# Boxplot
st.subheader('📦 Boxplot Visualization')
boxplot_column = st.selectbox('Select a column for Boxplot', df.columns)
if boxplot_column in df.select_dtypes(include=np.number).columns:
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=boxplot_column, ax=ax)
    st.pyplot(fig)
else:
    st.write(f"Column '{boxplot_column}' is not numeric. Please select a numeric column.")

# Outlier Detection
st.subheader('🔍 Outlier Detection')
outlier_column = st.selectbox('Select a column for Outlier Detection', numeric_columns)
if outlier_column:
    q1 = df[outlier_column].quantile(0.25)
    q3 = df[outlier_column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[outlier_column] < lower_bound) | (df[outlier_column] > upper_bound)]
    st.write(f"Outliers detected in '{outlier_column}':")
    st.write(outliers)

# Scatter Plot
st.subheader('📌 Scatter Plot')
x_axis = st.selectbox('Select column for X-axis', numeric_columns)
y_axis = st.selectbox('Select column for Y-axis', numeric_columns)
if x_axis and y_axis:
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_axis, y=y_axis, hue=hue_column, ax=ax)
    st.pyplot(fig)

# Footer
st.write('---')
st.write('Built with Streamlit | https://github.com/ashwathnakate 🚀')
