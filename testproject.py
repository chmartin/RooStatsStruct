import sys
sys.argv.insert(1, "-b")
import ROOT
import loadlib
del sys.argv[1]
import random
from extendedcounter import *
import style

########################################
#parameters
testmu = 1
testfa3s = {0: 1, 1: 2, 0.5: 4, -0.5: 418}
varnames = ["sMELA_ggH", "D0-_dec", "Dcp_dec"]
########################################

f = ROOT.TFile.Open("fa3_0_0_workspace_nobkg.root")
#f = ROOT.TFile.Open("fa3_0_0_workspace.root")
w = f.Get("workspace")

fa3 = w.var("fa3")
mu = w.var("mu")

pdf = w.pdf("ggH_0_0")

for varname in varnames:
    var = w.var(varname)
    print varname, var
    frame = var.frame()

    othervarnames = varnames[:]
    othervarnames.remove(varname)
    othervars = [w.var(a) for a in othervarnames]

    for testfa3 in testfa3s:
        ROOT.RooRandom.randomGenerator().SetSeed(random.randint(0,10000))

        c1 = ROOT.TCanvas.MakeDefCanvas()
        mu.setVal(testmu)
        fa3.setVal(testfa3)
        pdf.createProjection(ROOT.RooArgSet(*othervars)).plotOn(frame, ROOT.RooFit.LineColor(testfa3s[testfa3]))

    frame.Draw()
    [c1.SaveAs("/afs/cern.ch/user/h/hroskes/www/VBF/Summer2015/scans/projection_%s.%s" % (varname, format)) for format in ["png", "eps", "root", "pdf"]]
