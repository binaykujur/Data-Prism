import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

# Title of the app
st.title("Data Prism")

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the dataset
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display the dataset
    st.subheader("Original Dataset")
    st.write(df)

    # Data cleaning options
    st.sidebar.header("Data Cleaning Options")

    # 1. Handle missing values
    if st.sidebar.checkbox("Handle Missing Values"):
        st.subheader("Handle Missing Values")
        st.write("Current missing values in the dataset:")
        st.write(df.isnull().sum())

        option = st.selectbox(
            "Choose an option to handle missing values:",
            ("Drop rows with missing values", "Fill with mean", "Fill with median", "Fill with mode", "Fill with custom value")
        )

        if option == "Drop rows with missing values":
            df = df.dropna()
        elif option == "Fill with mean":
            df = df.fillna(df.mean())
        elif option == "Fill with median":
            df = df.fillna(df.median())
        elif option == "Fill with mode":
            df = df.fillna(df.mode().iloc[0])
        elif option == "Fill with custom value":
            custom_value = st.text_input("Enter custom value to fill missing values:")
            if custom_value:
                df = df.fillna(custom_value)

        st.write("Dataset after handling missing values:")
        st.write(df)

    # 2. Remove duplicates
    if st.sidebar.checkbox("Remove Duplicates"):
        st.subheader("Remove Duplicates")
        df = df.drop_duplicates()
        st.write("Dataset after removing duplicates:")
        st.write(df)

    # 3. Rename columns
    if st.sidebar.checkbox("Rename Columns"):
        st.subheader("Rename Columns")
        new_columns = st.text_input("Enter new column names (comma-separated):")
        if new_columns:
            new_columns = new_columns.split(",")
            if len(new_columns) == len(df.columns):
                df.columns = new_columns
                st.write("Dataset after renaming columns:")
                st.write(df)
            else:
                st.error("Number of new column names does not match the number of columns in the dataset.")

    # 4. Drop columns
    if st.sidebar.checkbox("Drop Columns"):
        st.subheader("Drop Columns")
        columns_to_drop = st.multiselect("Select columns to drop:", df.columns)
        if columns_to_drop:
            df = df.drop(columns=columns_to_drop)
            st.write("Dataset after dropping columns:")
            st.write(df)

    # 5. Reset index
    if st.sidebar.checkbox("Reset Index"):
        st.subheader("Reset Index")
        df = df.reset_index(drop=True)
        st.write("Dataset after resetting index:")
        st.write(df)

    # 6. Convert data types
    if st.sidebar.checkbox("Convert Data Types"):
        st.subheader("Convert Data Types")
        column_to_convert = st.selectbox("Select column to convert:", df.columns)
        new_type = st.selectbox(
            "Select new data type:",
            ("int", "float", "str", "datetime")
        )
        if st.button("Convert"):
            try:
                if new_type == "datetime":
                    df[column_to_convert] = pd.to_datetime(df[column_to_convert])
                else:
                    df[column_to_convert] = df[column_to_convert].astype(new_type)
                st.write(f"Column '{column_to_convert}' converted to {new_type}.")
                st.write(df.dtypes)
            except Exception as e:
                st.error(f"Error converting column: {e}")

    # 7. Handle outliers
    if st.sidebar.checkbox("Handle Outliers"):
        st.subheader("Handle Outliers")
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        column_to_handle = st.selectbox("Select numeric column to handle outliers:", numeric_columns)
        method = st.selectbox(
            "Choose a method to handle outliers:",
            ("Remove outliers", "Cap outliers")
        )
        if method == "Remove outliers":
            lower_bound = st.number_input("Enter lower bound (percentile):", value=0.05)
            upper_bound = st.number_input("Enter upper bound (percentile):", value=0.95)
            lower_limit = df[column_to_handle].quantile(lower_bound)
            upper_limit = df[column_to_handle].quantile(upper_bound)
            df = df[(df[column_to_handle] >= lower_limit) & (df[column_to_handle] <= upper_limit)]
            st.write(f"Outliers outside the range [{lower_limit}, {upper_limit}] removed.")
        elif method == "Cap outliers":
            lower_bound = st.number_input("Enter lower bound (percentile):", value=0.05)
            upper_bound = st.number_input("Enter upper bound (percentile):", value=0.95)
            lower_limit = df[column_to_handle].quantile(lower_bound)
            upper_limit = df[column_to_handle].quantile(upper_bound)
            df[column_to_handle] = df[column_to_handle].clip(lower_limit, upper_limit)
            st.write(f"Outliers capped to the range [{lower_limit}, {upper_limit}].")
        st.write(df)

    # 8. Filter rows
    if st.sidebar.checkbox("Filter Rows"):
        st.subheader("Filter Rows")
        filter_column = st.selectbox("Select column to filter:", df.columns)
        if pd.api.types.is_numeric_dtype(df[filter_column]):
            min_val = float(df[filter_column].min())
            max_val = float(df[filter_column].max())
            filter_range = st.slider(
                "Select range to filter:",
                min_val, max_val, (min_val, max_val)
            )
            df = df[(df[filter_column] >= filter_range[0]) & (df[filter_column] <= filter_range[1])]
        else:
            filter_value = st.text_input(f"Enter value to filter in column '{filter_column}':")
            df = df[df[filter_column].astype(str).str.contains(filter_value, case=False)]
        st.write("Dataset after filtering:")
        st.write(df)

    # 9. Text cleaning
    if st.sidebar.checkbox("Text Cleaning"):
        st.subheader("Text Cleaning")
        text_column = st.selectbox("Select text column to clean:", df.select_dtypes(include=[object]).columns)
        if st.checkbox("Convert to lowercase"):
            df[text_column] = df[text_column].str.lower()
        if st.checkbox("Remove special characters"):
            df[text_column] = df[text_column].str.replace(r'[^\w\s]', '', regex=True)
        if st.checkbox("Remove whitespace"):
            df[text_column] = df[text_column].str.strip()
        if st.checkbox("Standardize text (capitalize first letter)"):
            df[text_column] = df[text_column].str.capitalize()
        st.write("Dataset after text cleaning:")
        st.write(df)

    # 10. Replace values
    if st.sidebar.checkbox("Replace Values"):
        st.subheader("Replace Values")
        column_to_replace = st.selectbox("Select column to replace values:", df.columns)
        old_value = st.text_input("Enter value to replace:")
        new_value = st.text_input("Enter new value:")
        if st.button("Replace"):
            df[column_to_replace] = df[column_to_replace].replace(old_value, new_value)
            st.write("Dataset after replacing values:")
            st.write(df)

    # 11. Drop rows by condition
    if st.sidebar.checkbox("Drop Rows by Condition"):
        st.subheader("Drop Rows by Condition")
        column_to_filter = st.selectbox("Select column to filter:", df.columns)
        condition = st.selectbox(
            "Select condition:",
            ("Greater than", "Less than", "Equal to", "Contains")
        )
        if condition in ["Greater than", "Less than", "Equal to"]:
            threshold = st.number_input(f"Enter threshold value for '{condition}':")
            if condition == "Greater than":
                df = df[df[column_to_filter] > threshold]
            elif condition == "Less than":
                df = df[df[column_to_filter] < threshold]
            elif condition == "Equal to":
                df = df[df[column_to_filter] == threshold]
        elif condition == "Contains":
            value = st.text_input("Enter value to filter:")
            df = df[df[column_to_filter].astype(str).str.contains(value, case=False)]
        st.write("Dataset after dropping rows:")
        st.write(df)

    # 12. Split columns
    if st.sidebar.checkbox("Split Columns"):
        st.subheader("Split Columns")
        column_to_split = st.selectbox("Select column to split:", df.columns)
        delimiter = st.text_input("Enter delimiter to split by:")
        if delimiter:
            split_columns = st.number_input("Enter number of columns to split into:", min_value=2, max_value=10, value=2)
            if st.button("Split"):
                df = df.join(df[column_to_split].str.split(delimiter, expand=True).iloc[:, :split_columns])
                st.write("Dataset after splitting column:")
                st.write(df)

    # 13. Merge columns
    if st.sidebar.checkbox("Merge Columns"):
        st.subheader("Merge Columns")
        columns_to_merge = st.multiselect("Select columns to merge:", df.columns)
        separator = st.text_input("Enter separator for merging:")
        if columns_to_merge and separator:
            new_column_name = st.text_input("Enter new column name:")
            if new_column_name:
                df[new_column_name] = df[columns_to_merge].astype(str).agg(separator.join, axis=1)
                st.write("Dataset after merging columns:")
                st.write(df)

    # 14. Remove rows with specific values
    if st.sidebar.checkbox("Remove Rows with Specific Values"):
        st.subheader("Remove Rows with Specific Values")
        column_to_filter = st.selectbox("Select column to filter:", df.columns)
        values_to_remove = st.text_input("Enter values to remove (comma-separated):")
        if values_to_remove:
            values_to_remove = values_to_remove.split(",")
            df = df[~df[column_to_filter].isin(values_to_remove)]
            st.write("Dataset after removing rows:")
            st.write(df)

    # 15. Apply custom function
    if st.sidebar.checkbox("Apply Custom Function"):
        st.subheader("Apply Custom Function")
        column_to_apply = st.selectbox("Select column to apply function:", df.columns)
        custom_function = st.text_input("Enter custom function (e.g., lambda x: x * 2):")
        if custom_function:
            try:
                df[column_to_apply] = df[column_to_apply].apply(eval(custom_function))
                st.write("Dataset after applying custom function:")
                st.write(df)
            except Exception as e:
                st.error(f"Error applying custom function: {e}")

    # Download cleaned dataset
    st.subheader("Download Cleaned Dataset")
    cleaned_file = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Cleaned Dataset as CSV",
        data=cleaned_file,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a dataset to get started.")