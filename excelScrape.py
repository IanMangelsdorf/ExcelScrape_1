import glob
import xlrd
files = glob.glob("C:\Users\User\Desktop\*.xlsx")

class all_data():

    def

class RCA():

    def weight(self, weight):
        return self.weight()

    def gv(self,a):
        pass

    def bv(self):
        pass

    def pv(self):
        pass

    def phi_bv(self):
        pass

    def phi_pv(self):
        pass

    def phi_ob(self):
        pass

    def ka(self):
        pass

    def ka_ob(self):
        pass

    def plug_id(self):
        pass

    def plug_depth(self):
        pass

    def well(self):
        pass

    def dtime(self):
        pass

    def id(self):
        self.plug_depth + self.well + self.dtime


a = RCA()

a.weight(100.21)
print (a.weight)


for filename in files:
    workbook = xlrd.open_workbook(filename)
    for sheet in workbook.sheets():
        Data.append(sheet.cell_value(10,8))