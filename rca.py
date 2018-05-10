class all_data():
    pass

class RCA():

    def __init__(self):
        self.weight = 0
        self.phi_BV=0
        self.phi_GV = 0
        self.phi_Ka = 0
        self.phi_GD = 0
        self.plug_depth =0
        self.dtime = ""
        self.well =""


    def id(self):
        return '{} {} {}'.format(self.plug_depth, self.well, self.dtime)

    def all_rca(self):
        return '{} {} {}'.format(self.plug_depth, self.well, self.dtime)