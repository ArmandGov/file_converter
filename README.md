# CSV to Excel Converter

Convert CSV files to Excel format with frozen headers and automatic filters.

## Features

- Converts CSV files to Excel (.xlsx) format
- Freezes the first row (headers) for easy scrolling
- Adds autofilters to all columns
- Auto-adjusts column widths

## Installation

```bash
pip install pandas xlsxwriter
```

## Usage

```python
from csv_to_excel_converter import csv_to_excel_with_formatting

# Convert with auto-generated filename (replaces .csv with .xlsx)
csv_to_excel_with_formatting('data.csv')

# Convert with custom output filename
csv_to_excel_with_formatting('input.csv', 'formatted_output.xlsx')
```

## Function Parameters

- `csv_file_path` (str): Path to input CSV file
- `excel_file_path` (str, optional): Output Excel file path. If not provided, uses same name as CSV with .xlsx extension

## Example

```python
# This converts 'sales_data.csv' to 'sales_data.xlsx'
csv_to_excel_with_formatting('sales_data.csv')
```

The resulting Excel file will have:
- Frozen header row
- Filters on all columns
- Auto-adjusted column widths
