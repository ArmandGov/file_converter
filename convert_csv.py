import pandas as pd
import os
from pathlib import Path
import sys


def csv_converter(filepath, excel_path=None):
    """
    converts a CSV file to Excel with frozen first row and filters.

    args:
        filepath: Path to input csv file 
        excel_path: path to where excel file should be saved, if none given, uses same path as csv file
    """

    try:
        # read csv file
        df = pd.read_csv(filepath)

        # generate output filename if not provided
        if excel_path is None:
            csv_path = Path(filepath)
            excel_file_path = csv_path.with_suffix('.xlsx')

        # create excel writer object with xlsxwriter engine for formatting
        with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)

            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            worksheet.freeze_panes(1,0)
            
            # get dimentions of dataframe
            max_row = len(df)
            max_col = len(df.columns)

            # set autofilter for the entire data range (including headers)
            worksheet.autofilter(0, 0, max_row, max_col)

            # auto adjust column widths
            for i, column in enumerate(df.columns):
                column_len = max(
                    df[column].astype(str).str.len().max(), # max eln in column
                    len(str(column)) # len of column name
                )

                # set column width with some padding, but cap it at reasonable max
                worksheet.set_column(i, i, min(column_len + 2, 50))

        print(f'Successfully converted {csv_path} to {excel_file_path}')
        return excel_file_path
    
    except Exception as e:
        print(f'Error converting {csv_path}: {str(e)}')


if __name__ == "__main__":
    csv_converter(sys.argv[1])