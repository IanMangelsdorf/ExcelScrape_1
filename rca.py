class all_data():
    pass

class RCA():

    def __init__(self):
        self.weight = -999.25
        self.phi_BV=-999.25
        self.phi_GV = -999.25
        self.Ka = -999.25
        self.KaOB = -999.25
        self.phiOB = -999.25
        self.GD = -999.25
        self.BV = -999.25
        self.GV = -999.25
        self.PV = -999.25
        self.len = -999.25
        self.diam =-999.25
        self.Pmean = -999.25
        self.plug_depth =-999.25
        self.dtime = "null"
        self.well ="null"
        self.rptDate="null"
        self.dir ="null"
        self.plug = "null"
        self.So = 0
        self.Sw = 0
        self.Stotal = 0
        self.Comments = "null"
        self.description = "null"
        self.lube = "null"


    def id(self):
        return '{} {} {}'.format(self.plug_depth, self.well, self.dtime)

    def all_rca(self):
        return '{} {} {}'.format(self.plug_depth, self.well, self.dtime)