# PCOS_Detection



<div align="center">
    <img src="https://tse1.mm.bing.net/th/id/OIP.rwrX0phesVws97q8xhHzMAHaHa?rs=1&pid=ImgDetMain&o=7&rm=3" alt="PCOS Detection Logo" height="220">
</div>

# Aim
This project aims to develop a machine learning model to detect Polycystic Ovary Syndrome (PCOS) using clinical and diagnostic data. The notebook includes data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and interpretation of results. The goal is to assist healthcare professionals in identifying PCOS cases more efficiently and accurately.


# About the Dataset

The dataset used in this project contains comprehensive clinical and physical parameters for the detection of Polycystic Ovary Syndrome (PCOS) and related infertility issues. Data was collected from 10 different hospitals across Kerala, India, and is designed to support robust machine learning analysis.

### Key Features

- **Clinical and Diagnostic Data:** Includes a wide range of features such as menstrual history, hormone levels, blood group, blood pressure, and other relevant health indicators.
- **Standardized Units:** All measurements are converted to standard units (e.g., height in centimeters).
- **Binary Encoding:** Yes/No questions are encoded as 1 (Yes) and 0 (No) for consistency.
- **Blood Group Encoding:** Blood groups are represented numerically:
    - A+ = 11, A- = 12, B+ = 13, B- = 14, O+ = 15, O- = 16, AB+ = 17, AB- = 18
- **Blood Pressure:** Entered as separate systolic and diastolic values.
- **Random Glucose Test:** RBS (Random Blood Sugar) values are included.
- **Beta-HCG Cases:** Both Case I and II are recorded; if only one is available, it is repeated for consistency.
- **Data Quality:** 
    - All patient records are complete, with no missing (NaN) or non-numeric values.
    - Manipulated or highlighted data is marked with specific colors (e.g., orange for manipulated, red for blanks, green for PCOS-positive cases).
    - Additional information, if any, is kept separate from the main dataset format.

### Data Entry Guidelines

1. Ensure all data is converted to the specified units (e.g., feet to centimeters).
2. Complete all fields for each patient; do not leave blanks.
3. Use the specified color codes for manipulated data, blanks, and PCOS-positive cases for easier reference.
4. For Yes/No questions, use 1 for Yes and 0 for No.
5. Enter blood pressure as two separate values: systolic and diastolic.
6. Avoid mixing additional information with the main dataset; keep it in a separate section if needed.

This structured and well-annotated dataset enables accurate and efficient analysis for PCOS detection and related research.

Link for Dataset- https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos

# Setup:
Run the SetYouUp.ipynb file to get started.

## Project Organization

```
├──SetYouUp.ipynb      <- Jupyter notebook to set up additional requirements for you.
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         pcos_detection and configuration for tools like black
│
│
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── pcos_detection   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes pcos_detection a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    └──── dataset.py              <- Scripts to download or generate data```

--------

