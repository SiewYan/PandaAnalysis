#! /usr/bin/env python

import os
import copy
import math
from array import array
from ROOT import gROOT, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText

from PandaAnalysis.MonoX.drawUtils import *
from PandaAnalysis.MonoX.variables import *
#from PandaAnalysis.MonoX.MonoXSelection import sel
from PandaAnalysis.MonoX.samples import samples
from PandaCore.Tools.Misc import *

#gROOT.Macro('../Heppy/python/tools/functions.C')

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-b", "--bash", action="store_true", default=False, dest="runBash")
(options, args) = parser.parse_args()
if options.runBash: gROOT.SetBatch(True)

gROOT.SetBatch(True)
########## SETTINGS ##########
#gROOT.Macro('functions.C')
gStyle.SetOptStat(0)
LUMI        = 35800. # in pb-1
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
#NTUPLEDIR   = '/lustre/cmsdata/pazzini/ALPHA/v6/Pruned/'
NTUPLEDIR = getenv('PANDA_FLATDIR')+'/'

back = []
#sign = ['hsDM-500-50-200','hsDM-1000-50-200','hsDM-1500-50-200','hsDM-2000-50-200','hsDM-2500-50-200']
colors = [616+4, 632, 800+7, 800, 416+1, 860+10, 600, 616, 921, 922]

massPoints = []
channels = []
color = {"XVZmmlp" : 634, "XVZmmhp" : 410, "XVZeelp" : 856, "XVZeehp" : 418}

def signal(var, cut, sign, process, folder, reg, analysis):

    proc = process
    signals = sign
    #level = analysis
    level = "reco"

    if level == 'reco':
        cut = "1==1"
    elif level == 'ana1':
        cut = "nFatjet==1 && fj1Pt>200 && nTau==0 && Sum$(jetPt>30 && jetIso)<2 && nLooseLep==0 && nLooseElectron==0 && nLoosePhoton==0 && pfmet>250 && dphipfmet>0.4 && isojetNBtags==0 && fj1MSD > 25 && fj1DoubleCSV>0.75"
    elif level == 'ana2':
        cut = "nFatjet==1 && fj1Pt>200 && nTau==0 && Sum$(jetPt>30 && jetIso)<2 && nLooseLep==0 && nLooseElectron==0 && nLoosePhoton==0 && pfmet>250 && dphipfmet>0.4 && isojetNBtags==0 && fj1MSD > 25 && fj1DoubleCSV<0.75"
    else:
        cut = "0"

    weights = "%f*sf_pu*sf_tt*normalizedWeight*sf_lepID*sf_lepIso*sf_lepTrack*sf_ewkV*sf_qcdV*sf_metTrig*sf_btag0" %LUMI
    # var, cut, weight
    hist = project(var, cut ,weights, signals, [], NTUPLEDIR)
        #hist[s].Scale(LUMI)
        #hist[s].SetLineWidth(2)
    c = drawSignal(hist,signals,reg)
    drawCMS(-1, "Simulation","g_{#chi}= 1.0; g_{q}= 0.25; #theta_{mix}= 0.01",proc,cut)

    if folder.split("_")[0] == 'hsDM':
        fod="hsDM"
    else:
        fod="ZpDM"

    if not os.path.exists(fod):
        os.makedirs(fod)

    c[0].Print(fod+"/"+folder+"_"+var+".pdf")
    c[0].Print(fod+"/"+folder+"_"+var+".png")
    #c[0].Print("signalPlots/Signal_"+var+".root")
    #if not options.runBash: raw_input("Press Enter to continue...")

#HSDM
#Scanning on Zprime
sign = ['hsDM-500-50-200','hsDM-1000-50-200','hsDM-1500-50-200','hsDM-2000-50-200','hsDM-2500-50-200','hsDM-3000-50-200']
signal("pfmet" , "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_Zpscan",True,"ana1")
signal("fj1MSD", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_Zpscan",False,"ana1")
signal("fj1Pt", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_Zpscan",True,"ana1")

#Scanning on hs
sign = ['hsDM-1500-50-200','hsDM-1500-70-200','hsDM-1500-90-200'] 
signal("pfmet" , "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_hsscan",True,"ana1")
signal("fj1MSD", "" , sign , "pp #rightarrow s(b#bar{b}) + DM", "hsDM_hsscan",False,"ana1")
signal("fj1Pt", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_hsscan",True,"ana1")

#Scanning on DM
sign = ['hsDM-1000-50-50','hsDM-1000-50-100','hsDM-1000-50-150','hsDM-1000-50-200','hsDM-1000-50-250','hsDM-1000-50-300','hsDM-1000-50-400']
signal("pfmet" , "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_DMscan",True,"ana1")
signal("fj1MSD", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_DMscan",False,"ana1")
signal("fj1Pt", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_DMscan",True,"ana1")

#Scanning on threshold effect
sign = ['hsDM-495-50-250','hsDM-495-70-250','hsDM-495-90-250']
signal("pfmet" , "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_thrScan",True,"ana1")
signal("fj1MSD", "" , sign , "pp #rightarrow s(b#bar{b}) + DM", "hsDM_thrScan",False,"ana1")
signal("fj1Pt", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","hsDM_thrScan",True,"ana1")

####################################################################################

#Zpdm                                                                                                                                                 
#Scanning on Zprime                                                                                                                    
sign = ['ZpDM-50-50-10','ZpDM-100-50-10','ZpDM-300-50-10','ZpDM-1000-50-10','ZpDM-1500-50-10','ZpDM-2000-50-10','ZpDM-2500-50-10','ZpDM-3000-50-10']
signal("pfmet" , "" , sign , "pp #rightarrow Z'(q#bar{q}) + DM","ZpDM_Zpscan",True,"ana2")
signal("fj1MSD", "" , sign , "pp #rightarrow Z'(q#bar{q}) + DM","ZpDm_Zpscan",True,"ana2")

#Scanning on hs                                                                                      
sign = ['ZpDM-1000-50-10','ZpDM-1000-150-10']
signal("pfmet" , "" , sign , "pp #rightarrow Z'(q#bar{q}) + DM","ZpDM_hsscan",True,"ana2")
signal("fj1MSD", "" , sign , "pp #rightarrow Z'(q#bar{q}) + DM", "ZpDM_hsscan",True,"ana2")

#Scanning lowMass                                                                                                               
sign = ['hsDM-1000-50-50','hsDM-1000-50-100','hsDM-1000-50-150','hsDM-1000-50-200','hsDM-1000-50-250','hsDM-1000-50-300']
signal("pfmet" , "" , sign , "pp #rightarrow s(b#bar{b}) + DM","ZpDM_lowMScan",True,"ana2")
signal("fj1MSD", "" , sign , "pp #rightarrow s(b#bar{b}) + DM","ZpDM_lowMScan",False,"ana2")


