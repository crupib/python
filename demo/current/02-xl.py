import openpyxl
# loads an existing workbook myfile.xlsx
workbook = openpyxl.load_workbook("myfile.xlsx")

# adds a new worksheet to an existing workbook
worksheet = workbook.create_sheet(title='mysheet')

# hide gridlines in a worksheet
worksheet.sheet_view.showGridLines = False

# enable gridlines in a worksheet
worksheet.sheet_view.showGridLines = True
