import glob
import xlrd
files = glob.glob("C:\\test\\New folder\\*.xlsx")
datafile = "C:\\test\\sum.xlsx"
data = xlrd.open_workbook(datafile)
sht = data.sheet_by_index(0)





for filename in files:
    workbook = xlrd.open_workbook(filename)

    for sheet in workbook.sheets():
        if sheet.name.find("Results")>0:
            # Collect Job Data

            # Collect RCA Data
            for row in range(sheet.nrows):
                for column in range(sheet.ncols):
                    if s == sheet.cell(row, column).value:
                        return (row, column)

            data.append(sheet.cell_value(10,8))