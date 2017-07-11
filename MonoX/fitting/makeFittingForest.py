#!/usr/bin/env python
from re import sub
from sys import argv,exit
from os import path,getenv
from glob import glob
import argparse
parser = argparse.ArgumentParser(description='make forest')
parser.add_argument('--region',metavar='region',type=str,default=None)
#parser.add_argument('--couplings',metavar='couplings',type=str,default=None)
args = parser.parse_args()
#couplings = args.couplings
#if couplings=='nominal':
#    couplings = None
out_region = args.region
region = out_region.split('_')[0]
if region=='test':
    is_test = True 
    region = 'signal'
else:
    is_test = False

argv=[]
import PandaAnalysis.Flat.fitting_forest as forest 
from PandaCore.Tools.Misc import *
import PandaCore.Tools.Functions # kinematics
import PandaAnalysis.MonoX.MonoXSelection as sel

basedir = getenv('PANDA_FLATDIR')+'/'
lumi = 35900

def f(x):
    return basedir + x + '.root'

def shift_btags(additional=None):
    shifted_weights = {}
    #if not any([x in region for x in ['signal','top','w']]):
    #    return shifted_weights 
    for shift in ['BUp','BDown','MUp','MDown']:
        for cent in ['sf_btag']:
            shiftedlabel = ''
            if 'sj' in cent:
                shiftedlabel += 'sj'
            if 'B' in shift:
                shiftedlabel += 'btag'
            else:
                shiftedlabel += 'mistag'
            if 'Up' in shift:
                shiftedlabel += 'Up'
            else:
                shiftedlabel += 'Down'
            weight = sel.weights[region+'_'+cent+shift]%lumi
            if additional:
                weight = tTIMES(weight,additional)
            shifted_weights[shiftedlabel] = weight
    return shifted_weights
vmap = {}
#vmap = {'top_ecf_bdt':'top_ecf_bdt'}
mc_vmap = {'genBosonPt':'genBosonPt'}
if region in ['signal','test']:
    u,uphi, = ('pfmet','pfmetphi')
elif 'photon' in region:
    u,uphi = ('pfUAmag','pfUAphi')
elif 'single' in region:
    u,uphi = ('pfUWmag','pfUWphi')
elif 'di' in region:
    u,uphi = ('pfUZmag','pfUZphi')
vmap['met'] = 'min(%s,999.9999)'%u 
vmap['fj1Pt'] = 'fj1Pt'
vmap['fj1MSD_corr'] = 'fj1MSD_corr'
vmap['fj1ECFN_2_3_10'] = 'fj1ECFN_2_3_10'
vmap['fj1ECFN_1_2_10'] = 'fj1ECFN_1_2_10'

weights = {'nominal' : sel.weights[region]%lumi}
#if couplings:
#    weights['nominal'] = tTIMES(weights['nominal'],couplings)
weights.update(shift_btags(couplings))


factory = forest.RegionFactory(name = region if not(is_test) else 'test',
                               cut = sel.cuts[region],
                               variables = vmap, 
                               mc_variables = mc_vmap, 
                               mc_weights = weights)



if is_test:
    factory.add_process(f('Diboson'),'Diboson')
elif region=='photon':
    factory.add_process(f('GJets'),'Pho')
    factory.add_process(f('SinglePhoton'),'Data',is_data=True,extra_cut=sel.triggers['pho'])
    factory.add_process(f('SinglePhoton'),'QCD',is_data=True,
                        extra_weights='sf_phoPurity',extra_cut=sel.triggers['pho'])
elif out_region not in ['signal']:
    factory.add_process(f('ZtoNuNu'),'Zvv')
    factory.add_process(f('ZJets'),'Zll')
    factory.add_process(f('WJets'),'Wlv')
    factory.add_process(f('TTbar'),'ttbar')
    factory.add_process(f('SingleTop'),'ST')
    factory.add_process(f('Diboson'),'Diboson')
    factory.add_process(f('QCD'),'QCD')
    if 'electron' in region:
        factory.add_process(f('SingleElectron'),'Data',is_data=True,extra_cut=sel.triggers['ele'])
    else:
        factory.add_process(f('MET'),'Data',is_data=True,extra_cut=sel.triggers['met'])

elif out_region=='signal':
    for m in [300,500,1000]:
        factory.add_process(f('ST_tch_DM-scalar_LO-%i_1-13_TeV'%m),'stdm_%i'%m)


if is_test:
    region = 'test'
factory.run(basedir+'/fitting/fittingForest_%s.root'%out_region)
