#!/bin/bash                                                                                                                                                                                                 
export PATH=${PATH}:${CMSSW_BASE}/src/PandaCore/bin/

#submission number
export SUBMIT_NAME="v_8026_monoj"
#scratch space
export scratch_area="/uscms_data/d3"

export PANDA="${CMSSW_BASE}/src/PandaAnalysis"

#export PANDA_CFG="http://t3serv001.mit.edu/~mcremone/histcatalog/test.cfg"
#export PANDA_CFG="http://t3serv001.mit.edu/~bmaier/stuff/ZpA0.txt"
#export PANDA_CFG="http://t3serv001.mit.edu/~bmaier/stuff/ZpBaryonic.txt"
export PANDA_CFG="http://t3serv001.mit.edu/~snarayan/histcatalog/20170522_004.cfg"
export PANDA_FLATDIR="${scratch_area}/${USER}/panda/"${SUBMIT_NAME}"/flat/"

mkdir -p $PANDA_FLATDIR

#export SUBMIT_TMPL="skim_monojet_tmpl.py" ####
#export SUBMIT_TMPL="skim_vbf_tmpl.py"
export SUBMIT_TMPL="skim_monoj_tmpl.py"                                                                                                                                            

export SUBMIT_WORKDIR="${scratch_area}/${USER}/condor/"${SUBMIT_NAME}"/work/"
export SUBMIT_LOGDIR="${scratch_area}/${USER}/condor/"${SUBMIT_NAME}"/logs/"
export SKIM_CFGDIR="${scratch_area}/${USER}/skim/configs"
#EOS
export SUBMIT_OUTDIR="/store/user/${USER}/panda/"${SUBMIT_NAME}"/batch/"

export SKIM_MONOJET_FLATDIR="${scratch_area}/${USER}/skim/"${SUBMIT_NAME}"/monojet/"
export SKIM_MONOHIGGS_FLATDIR="${scratch_area}/${USER}/skim/"${SUBMIT_NAME}"/monohiggs_boosted/"
export SKIM_MONOHIGGS_RESOLVED_FLATDIR="${scratch_area}/${USER}/skim/"${SUBMIT_NAME}"/monohiggs_resolved/"

mkdir -p $SUBMIT_WORKDIR $SUBMIT_LOGDIR $SKIM_MONOJET_FLATDIR $SKIM_MONOHIGGS_FLATDIR $SKIM_MONOHIGGS_RESOLVED_FLATDIR
#mkdir -p $SUBMIT_OUTDIR/locks/
#mkdir -p $SUBMIT_OUTDIR/workdir/

rm $SKIM_MONOJET_FLATDIR/*.sh
rm $SKIM_MONOHIGGS_FLATDIR/*.sh
rm $SKIM_MONOHIGGS_RESOLVED_FLATDIR/*.sh

ln -s $SKIM_CFGDIR/runSkim.sh  $SKIM_MONOJET_FLATDIR
ln -s $SKIM_CFGDIR/runSkimAll.sh  $SKIM_MONOJET_FLATDIR

ln -s $SKIM_CFGDIR/runSkim.sh  $SKIM_MONOHIGGS_FLATDIR
ln -s $SKIM_CFGDIR/runSkimAll.sh $SKIM_MONOHIGGS_FLATDIR

ln -s $SKIM_CFGDIR/runSkim.sh  $SKIM_MONOHIGGS_RESOLVED_FLATDIR
ln -s $SKIM_CFGDIR/runSkimAll.sh $SKIM_MONOHIGGS_RESOLVED_FLATDIR

echo "Checking validity of path"
echo "========================================================="
$PANDA_FLATDIR; $SUBMIT_WORKDIR; $SUBMIT_LOGDIR; /eos/uscms${SUBMIT_OUTDIR}; $SKIM_CFGDIR; $SKIM_MONOJET_FLATDIR
$SKIM_MONOHIGGS_FLATDIR; $SKIM_MONOHIGGS_RESOLVED_FLATDIR
echo "========================================================="

#private production                                                                                                                                                                                        
 
export PRIVATE_LOGDIR="${HOME}/cms/logs/monotop_private_panda/"
export PRIVATE_PRODDIR="${HOME}/cms/hist/monotop_private_pandatree/"
export PRIVATE_CFGDIR="${HOME}/cms/condor/monotop_private_panda/"

# fitting                                                                                                                                                                                                   
#export PANDA_FIT=/data/t3serv014/snarayan/CMSSW_7_4_7/
#export PANDA_XSECS=/home/snarayan/cms/cmssw/analysis/MonoTop_Xsec/
#export PANDA_FITTING=${PANDA_FLATDIR}/fitting/
#mkdir -p $PANDA_FITTING/scans/ $PANDA_FITTING/logs/


