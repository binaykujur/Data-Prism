# Streamlit Data Cleaning App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-00A98F?style=for-the-badge&logo=openpyxl&logoColor=white)

A powerful and interactive web application built with **Streamlit** for cleaning and preprocessing datasets. This app allows users to upload their datasets (CSV or Excel), perform various data cleaning operations, and download the cleaned dataset.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

### **Basic Cleaning Options**
- **Handle Missing Values**: Drop rows with missing values or fill them with mean, median, mode, or a custom value.
- **Remove Duplicates**: Remove duplicate rows from the dataset.
- **Rename Columns**: Rename columns in the dataset.
- **Drop Columns**: Drop selected columns from the dataset.
- **Reset Index**: Reset the index of the dataset.

### **Advanced Cleaning Options**
- **Convert Data Types**: Convert columns to `int`, `float`, `str`, or `datetime`.
- **Handle Outliers**: Remove or cap outliers in numeric columns.
- **Text Cleaning**: Convert text to lowercase, remove special characters, remove whitespace, and standardize text.
- **Replace Values**: Replace specific values in a column with another value.
- **Drop Rows by Condition**: Drop rows based on conditions like greater than, less than, equal to, or contains.
- **Split Columns**: Split a column into multiple columns based on a delimiter.
- **Merge Columns**: Merge multiple columns into a single column.
- **Remove Rows with Specific Values**: Remove rows where a column contains specific values.
- **Apply Custom Function**: Apply a custom function to a column.

### **Filtering Options**
- **Filter Rows**: Filter rows based on numeric ranges or string matching.

### **Download Cleaned Dataset**
- Download the cleaned dataset as a CSV file.

---

## Installation

Follow these steps to set up and run the Streamlit Data Cleaning App on your local machine.

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/streamlit-data-cleaning-app.git
   cd streamlit-data-cleaning-app
   
2. **Install dependencies**:
    
    install the required packages using pip
    ```bash
    pip install streamlit pandas numpy openpyxl
           
3. **Run the app**:

    start the streamlit app by running the following command:
    ```bash
    streamlit run app.py

## Usage
### Upload dataset
1.Click on the "Upload your dataset (CSV or Excel)" button to upload your dataset.
2.Supported file formats: .csv and .xlsx.

### Perform cleaning operations
1. Use the sidebar to select and apply various data cleaning operations.
2. Options include handling missing values, removing duplicates, renaming columns, dropping columns, and more.

### filter data
1. Use the filtering options to filter rows based on specific conditions.
2. Filter numeric columns using a slider or text columns using a search box.

### download cleaned dataset

1. After cleaning the dataset, click the "Download Cleaned Dataset as CSV" button to download the cleaned dataset.

## Contact
For any questions, feedback, or suggestions, feel free to reach out:
- email: binay.kujur@aol.com
- github: binaykujur
- linkedin: binay kujur