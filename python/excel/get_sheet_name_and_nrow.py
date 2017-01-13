'''
This file will extract the name of sheets and number of rows in that sheet from given excel sheet.
It uses openpyxl for reading excel sheets.
Usage Example:
python get_sheet_name_and_nrow.py <path/to/excel/sheet.xlsx>
'''

# Getting file name provided by user
import sys
if len(sys.argv) == 2:
    fileName = sys.argv[1]
    print("Entered file name = ", fileName)
    # Checking if mentioned file exists in the system
    import os
    if os.path.isfile(fileName):
        # Checking extension of given file
        if fileName.lower().endswith(('.xlsx', '.xlsx', '.xlsm', '.xltx', '.xltm')):
            import openpyxl
            try:
                wb = openpyxl.load_workbook(fileName)
                sheet_names = wb.get_sheet_names()
                count = 0
                for sheet_name in sheet_names:
                    count += 1
                    sheet = wb.get_sheet_by_name(sheet_name)
                    print("'%s', '%s', '%s'"%(count, sheet_name, sheet.max_row-1))
            except Exception as e:
                print("Catched some unexpected exception", e)
        else:
            print("Invalid file type") 
    else:
        print("File does not exist") 
else:
    print("Usage:")
    print("python get_sheet_name_and_nrow.py <path/to/excel/sheet.xlsx>")
