# Data Cleaning & Structural Validation

## Project Overview
This project focuses on cleaning messy data and validating its structure using Python and the Pandas library. The main goal is to improve data quality by removing duplicate records, handling missing values, correcting data types, and standardizing column names and categorical values.

**Objective:** To transform raw, inconsistent data into a clean and structured dataset suitable for further analysis.

## Tools and Technologies Used
- Python
- Pandas
- Jupyter Notebook
- CSV (Comma-Separated Values)
- GitHub

## Project Files
- `messy_sample_dataset.csv` – Original sample dataset containing inconsistent and missing values.
- `cleaned_customer_dataset.csv` – Final cleaned dataset.
- `Data_Cleaning_Structural_Validation.ipynb` – Jupyter Notebook containing the cleaning process and validation checks.
- `clean_data.py` – Python script used to perform data cleaning.
- `cleaning_validation_summary.txt` – Summary of cleaning steps and validation results.

## Data Cleaning Steps
1. **Duplicate Removal:** Identified and removed duplicate records.
2. **Missing Values:** Checked for missing data and handled it using suitable cleaning rules.
3. **Column Standardization:** Standardized column names for consistency.
4. **Data Type Validation:** Converted columns such as age and purchase amount to appropriate data types.
5. **Date Standardization:** Converted dates into a consistent format.
6. **Categorical Standardization:** Corrected inconsistent category values, such as differences in capitalization and spacing.
7. **Structural Validation:** Checked the cleaned dataset to ensure that it followed the expected structure.

## Results
- Original dataset: 21 rows
- Cleaned dataset: 20 rows
- Duplicate records removed: 1
- Column names and categorical values standardized.
- Data types and date formats checked.
- Missing and invalid values reviewed according to the documented cleaning rules.

## How to Run the Project
1. Download or clone this repository.
2. Install the required Python library:

   `pip install pandas`

3. Open `Data_Cleaning_Structural_Validation.ipynb` in Jupyter Notebook.
4. Run the notebook cells in order to review the cleaning process and validation results.

You can also run the Python script using:

`python clean_data.py`

## Conclusion
This project demonstrates how Python and Pandas can be used to clean messy data and validate its structure. The process improves data consistency and prepares the dataset for reliable analysis.

## Dataset Note
The dataset used in this project is a sample dataset created for demonstration and practice purposes. It is not an official customer dataset.

## Author
BCA Student
