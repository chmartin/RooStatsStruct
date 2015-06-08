from MakePDF import *

templatedir = "/afs/cern.ch/work/h/hroskes/Summer2015_VBF/makeTemplates/templates/"
channelnames = {0: "2e2mu", 1: "4mu", 2: "4e"}

class MakePDF_Heshy(MakePDF):

    def __init__(self):
        for channel in channelnames:
            self.makeWorkspace(channel)

    def makeWorkspace(self, channelCode):
        categoryCode = 2
        templateFile = templatedir + channelnames[channelCode] + "_templates.root"
        on_off_Code = 0
        templateName_SM = "template_VBFscalar"
        templateName_PS = "template_VBFpseudoscalar"
        templateName_mix = "template_VBFmixture"
        MakePDF.makeWorkspace(self, channelCode, categoryCode, templateFile, on_off_Code, templateName_SM, templateName_PS, templateName_mix)

MakePDF_Heshy()