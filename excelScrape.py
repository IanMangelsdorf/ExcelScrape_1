import glob
import xlrd
import rca
import csv

files = glob.glob("C:\\test\\New folder\\*.xlsx")
print (files.count())
datafile = "C:\\test\\sum.xlsx"
data = xlrd.open_workbook(datafile)
sht = data.sheet_by_index(0)
output = "c:\\test\\allrca.csv"


def find_ind(sh, find):
    for r in range(sh.nrows):
        for c in range(sh.ncols):
            if find == sh.cell(r, c).value:
                return  sh.cell(r, c).value


def find_fields(sh, dFields):
    for f in dFields:
        for r in range(sh.nrows):
            for c in range(sh.ncols):
                if f == sh.cell(r, c).value:
                    return  dFields, r+1

def rca_data():
    for filename in files:
        x = +1
        workbook = xlrd.open_workbook(filename)
        print ("scraping workbook " + str(x) + " of " + str(files.count))

        for sheet in workbook.sheets():
            a = rca.RCA()
            if sheet.name.find("Results") > 0:
                # Collect Job Data
                a.well = find_ind(sheet, "Well")
                a.Company = find_ind(sheet, "Company")
                a.Doc = find_ind(sheet, "Document")
                a.rpt_date = find_ind(sheet, "Date")

            dflieds, toprow = find_fields(sheet, dflieds)
            # Collect RCA Data

            for f in dflieds:

                for row in range(sheet.nrows):
                    for column in range(sheet.ncols):
                        if s == sheet.cell(row, column).value:
                            pass

        write_csv(output, dataline)


def write_csv(writeto, writewhat):
    csvfile = open(writeto, 'wb')
    csvwriter = csv.writer(csvfile)
    for item in writewhat:
        csvwriter.writerow(item)
    csvfile.close()


if __name__ == "__main__":
    rca_data()
