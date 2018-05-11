import glob
import xlrd
import rca
import csv

files = glob.glob("C:\\test\\New folder\\*.xlsx")
datafile = "C:\\test\\sum.xlsx"
data = xlrd.open_workbook(datafile)
sht = data.sheet_by_index(0)
output = "c:\\test\\allrca.csv"


def find_job(sh, find):
    for r in range(sh.nrows):
        for c in range(sh.ncols):
            if find == sheet.cell(r, c).value:
                return  sheet.cell(r, c).value


def find_columns(sh, dFields):
    for f in dFields:
        for r in range(sh.nrows):
            for c in range(sh.ncols):
                if f == sheet.cell(r, c).value:
                    return  dFields, r+1

def rca_data():
    pass


def write_csv(writeto, writewhat):
    csvfile = open(writeto, 'wb')
    csvwriter = csv.writer(csvfile)
    for item in writewhat:
        csvwriter.writerow(item)
    csvfile.close()


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


        dflieds, toprow = find_columns(sheet,dflieds)
        # Collect RCA Data

        for f in dflieds:

            for row in range(sheet.nrows):
                for column in range(sheet.ncols):
                    if s == sheet.cell(row, column).value:
                        pass

    write_csv(output, dataline)
