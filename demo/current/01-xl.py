import openpyxl
workbook = openpyxl.load_workbook("myfile.xlsx")

# adds a new worksheet to an existing workbook
worksheet = workbook.create_sheet(title='mysheet')

# never ever forget to save the workbook. I've done this a lot
workbook.save(filename="myfile.xlsx")
