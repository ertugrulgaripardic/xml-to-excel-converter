# XML to Excel Converter

![image](https://github.com/ertugrulgaripardic/xml-to-excel-converter/assets/118535200/acdeee89-1384-48e9-acba-4e972d787d48)


This repository contains scripts to convert XML data into Excel (.xlsx) files. The scripts are designed to download XML data, parse it, and export specific fields into a well-organized Excel spreadsheet.

## Scripts

### 1. xml_to_excel.py

This script downloads an XML file from a specified URL and converts it into an Excel file. The script extracts product data including `ProductID`, `Name`, `Price`, and `Description`.

#### Usage:

1. Modify the `url` variable in the script to point to your XML file.
2. Run the script using Python:
    ```bash
    python xml_to_excel.py
    ```
3. The script will create an Excel file named `products.xlsx` in the same directory.

### 2. get-pictures.py

This script reads a local XML file and extracts product image URLs, then writes them into an Excel file.

#### Usage:

1. Modify the `xml_file` and `excel_file` variables in the script to point to your XML file and desired Excel output file.
2. Run the script using Python:
    ```bash
    python get-pictures.py
    ```
3. The script will create an Excel file named as specified in the `excel_file` variable.

## Requirements

- Python 3.x
- pandas
- requests
- openpyxl

You can install the required packages using pip:
```bash
pip install pandas requests openpyxl
