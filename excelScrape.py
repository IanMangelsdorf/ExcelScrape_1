import glob
import xlrd
import rca


files = glob.glob("C:\\test\\New folder\\*.xlsx")
datafile = "C:\\test\\sum.xlsx"
data = xlrd.open_workbook(datafile)
sht = data.sheet_by_index(0)



def find_job(sh, find):
    for r in range(sh.nrows):
        for c in range(sh.ncols):
            if find == sheet.cell(r, c).value:
                return  sheet.cell(r, c).value

def find_colums(sh, dFields):
    for f in dFields:
        for r in range(sh.nrows):
            for c in range(sh.ncols):
                if f == sheet.cell(r, c).value:
                    return  dFields, r

def rca_data():
    pass

for filename in files:
    workbook = xlrd.open_workbook(filename)

    for sheet in workbook.sheets():
        a = rca.RCA()
        if sheet.name.find("Results")>0:
            # Collect Job Data
            a.well = find_job(sheet,"Well")
            a.Company  = find_job(sheet,"Company")
            a.Doc = find_job(sheet,"Document")
            a.rpt_date = find_job(sheet,"Date")

        dflieds, toprow = find_colums(sheet,dflieds)
            # Collect RCA Data

            for f in dflieds:

            for row in range(sheet.nrows):
                for column in range(sheet.ncols):
                    if s == sheet.cell(row, column).value:
                        pass


            data.append(sheet.cell_value(10,8))