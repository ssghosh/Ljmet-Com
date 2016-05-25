import os,sys,datetime

shift = sys.argv[1]

sampleList=[
# 'TprimeTprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1300_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 'TprimeTprime_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',

# #	'BprimeBprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1300_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'BprimeBprime_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# 
# #	'X53X53_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1100_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1100_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1300_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1300_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1500_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1500_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-700_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-700_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-900_LH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',
# #	'X53X53_M-900_RH_TuneCUETP8M1_13TeV-madgraph-pythia8.txt',

# 'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8.txt',
# 'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8.txt',
# 'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',
# 'TT_TuneCUETP8M1_13TeV-powheg-pythia8.txt',
# 
# 'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1.txt',
# 'ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1.txt',
# 'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt',
# 'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt',
# 
# 'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt',
# 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt',
# 
# 'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt',
# 
# 	## MANY MANY DI/TRI BOSONS, LIKELY NEED TO LOOK FOR MORE TRI
# 'WW_TuneCUETP8M1_13TeV-pythia8.txt',
# 'WWJJToLNuLNu_EWK_QCD_noTop_13TeV-madgraph-pythia8.txt',
# 'WWJJToLNuLNu_QCD_noTop_13TeV-madgraph-pythia8.txt',
# 'WWTo2L2Nu_13TeV-powheg.txt',
# 'WWToLNuQQ_13TeV-powheg.txt',
# 
# 'WZ_TuneCUETP8M1_13TeV-pythia8.txt',
# 'WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8.txt',
# 'WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt',
# 'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',
# 
# 'ZZ_TuneCUETP8M1_13TeV-pythia8.txt',
# 'ZZTo2L2Nu_13TeV_powheg_pythia8.txt',
# 'ZZJJTo4L_13TeV-madgraph-pythia8.txt',
# 'ZZTo4L_13TeV-amcatnloFXFX-pythia8.txt',
# 'ZZTo4L_13TeV_powheg_pythia8.txt',
# 
# 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',

	### RUN WITH root://eoscms.cern.ch in condor_submit.py
# 	'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt',
# 	'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8.txt',
# 	'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8.txt',
# 	'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',
# 	'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',
# 	'WWW_4f_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',
	'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.txt',

	]

# if shift == 'nominal':
# sampleList.append('TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8.txt'),
# sampleList.append('TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8.txt'),
# sampleList.append('ST_t-channel_4f_scaledown_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1.txt'),
# sampleList.append('ST_t-channel_4f_scaleup_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1.txt'),
# sampleList.append('ST_tW_top_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt'),
# sampleList.append('ST_tW_top_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt'),
# sampleList.append('ST_tW_antitop_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt'),
# sampleList.append('ST_tW_antitop_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1.txt'),

print '====== LJMET SUBMISSION ======'

relBase = os.environ['CMSSW_BASE']
print 'Relbase:',relBase

thisDir = relBase+'/src/LJMet/Com/condor_TTinclusive_032516/'
tarfile = relBase+'.tar'
print 'Making tar:'
if os.path.exists(tarfile):
	print 'tar already exists! Will not re-tar!'
else:
	os.chdir(relBase)
	os.chdir('../')
	print 'tar --exclude="src/LJMet/Com/.git" -zcf'+tarfile+' '+relBase.split('/')[-1]+'/'
	os.system('tar --exclude="src/LJMet/Com/.git" -zcf '+tarfile+' '+relBase.split('/')[-1])
	os.chdir(thisDir)

for sample in sampleList:
	os.system('python condor_submit.py --useMC True --sample '+sample.split('.')[0]+' --fileList '+thisDir+'fileLists/'+sample+' --submit True --inputTar '+tarfile+' --outDir /eos/uscms/store/user/lpcljm/LJMet_3lepTT_051316 --shift '+shift)

## shift should be (one at a time): nominal, JECup, JECdown, JERup, JERdown
## If you want to use different directory names, edit lines 144 - 147 in condor_submit.py so the config is edited correctly
