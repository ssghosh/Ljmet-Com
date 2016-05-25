import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

# Define the base process
process = cms.Process("LJMetCom")

#Arguments from condor submit script which are used more than once
condorIsMC = bool(True)
relBase    = str('/storage/local/data1/condor/execute/dir_18472/CMSSW_7_6_4')
condorJSON = str('None')
############################################################
#
# FWLite application options
process.load('LJMet.Com.ljmet_cfi')
process.ljmet.isMc = cms.bool(condorIsMC)

# Exclude some unnecessary calculators from the process
process.ljmet.excluded_calculators = cms.vstring(
    #'TpTpCalc',
    'PileUpCalc',
    'BTagSFCalc',
    'TprimeCalc',
    'DileptonCalc',
    'DileptonEventSelector',
    'CATopoCalc',
    'StopCalc',
    'PdfCalc',
    'ChargedHiggsCalc',
    'LjetsTopoCalc',
    'WprimeCalc'
    )

# common calculator options
process.load('LJMet.Com.commonCalc_cfi')

# singleLep calculator options
process.load('LJMet.Com.singleLepCalc_cfi')
process.singleLepCalc.isMc              = cms.bool(condorIsMC)
process.singleLepCalc.keepFullMChistory = cms.bool(condorIsMC)
process.singleLepCalc.UseElMVA          = cms.bool(True)
process.singleLepCalc.saveLooseLeps     = cms.bool(True)

# Jet substructure calculator options
process.load('LJMet.Com.JetSubCalc_cfi')
process.JetSubCalc.useHTT = cms.bool(False)
process.JetSubCalc.killHF = cms.bool(False) # False, because we want jets/objects in |eta| > 2.5, this is fine in 76x, but not in 74x?
process.JetSubCalc.doNewJEC = cms.bool(True)
process.JetSubCalc.JECup = cms.bool(False)
process.JetSubCalc.JECdown = cms.bool(False)
process.JetSubCalc.useL2L3Mass = cms.bool(True)
process.JetSubCalc.isMc = cms.bool(condorIsMC)
process.JetSubCalc.MCL2JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L2Relative_AK8PFchs.txt')
process.JetSubCalc.MCL3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L3Absolute_AK8PFchs.txt')
process.JetSubCalc.DataL2JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2Relative_AK8PFchs.txt')
process.JetSubCalc.DataL3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L3Absolute_AK8PFchs.txt')
process.JetSubCalc.DataL2L3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2L3Residual_AK8PFchs.txt')

############################################################
#
# Event selector options
#
process.event_selector = cms.PSet(

    selection = cms.string('singleLepSelector'),

    # Define cuts -- variable names are strings searched by src/singleLepEventSelector.cc

    debug  = cms.bool(False),

    isMc  = cms.bool(condorIsMC),
    keepFullMChistory = cms.bool(condorIsMC),
    doLaserCalFilt  = cms.bool(False),

    # Trigger cuts
    trigger_cut  = cms.bool(True),
    dump_trigger = cms.bool(False),

    mctrigger_path_el = cms.vstring(
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v1',          'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v2',          'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v3',          'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v4',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v1',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v2',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v3',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v4',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v1',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v2',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v3',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v4',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v1',    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v2',    'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v3',     'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v1', 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v2', 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3',  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v4',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1','HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2','HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
        'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v1',              'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v2',              'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v3',               'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v4',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1',      'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',      'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3',       'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v1',  'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v2',  'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v3',   'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v4',
		'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1',      'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',      'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v3',       'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v4',        
		'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1','HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2','HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3', 'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
		'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v1',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v2',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v3',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v4',
        ),
    mctrigger_path_mu = cms.vstring(
        'HLT_TripleMu_12_10_5_v1',                           'HLT_TripleMu_12_10_5_v2',                           'HLT_TripleMu_12_10_5_v3',                           'HLT_TripleMu_12_10_5_v4',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v1',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v2',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v3',                'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v4',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v1',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v2',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v3',               'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v4',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v1',     'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v2',     'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v3',     'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v1',  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v2',  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v3',  'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v4',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3', 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
        'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v1',               'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v2',               'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v3',               'HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v4',
        'HLT_Mu17_Mu8_SameSign_DZ_v1',                        'HLT_Mu17_Mu8_SameSign_DZ_v2',                        'HLT_Mu17_Mu8_SameSign_DZ_v3',                        'HLT_Mu17_Mu8_SameSign_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_DZ_v1',                       'HLT_Mu20_Mu10_SameSign_DZ_v2',                       'HLT_Mu20_Mu10_SameSign_DZ_v3',                       'HLT_Mu20_Mu10_SameSign_DZ_v4',
        'HLT_Mu30_TkMu11_v1',                                 'HLT_Mu30_TkMu11_v2',                                 'HLT_Mu30_TkMu11_v3',                                 'HLT_Mu30_TkMu11_v4',
        'HLT_Mu40_TkMu11_v1',                                 'HLT_Mu40_TkMu11_v2',                                 'HLT_Mu40_TkMu11_v3',                                 'HLT_Mu40_TkMu11_v4',
        'HLT_DoubleMu8_Mass8_PFHT250_v1',                     'HLT_DoubleMu8_Mass8_PFHT250_v2',                     'HLT_DoubleMu8_Mass8_PFHT250_v3',                     'HLT_DoubleMu8_Mass8_PFHT250_v4',
        'HLT_DoubleMu8_Mass8_PFHT300_v1',                     'HLT_DoubleMu8_Mass8_PFHT300_v2',                     'HLT_DoubleMu8_Mass8_PFHT300_v3',                     'HLT_DoubleMu8_Mass8_PFHT300_v4',
		'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v1',             'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2',             'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v3',             'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v4',
		'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v1',           'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2',           'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v3',           'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v4',
		'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1', 'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2', 'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3', 'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
		'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v1',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v2',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v3',  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v4',
        ),

    trigger_path_el = cms.vstring(''),
    trigger_path_mu = cms.vstring(''),

    # PV cuts
    pv_cut         = cms.bool(True),
    flag_tag       = cms.InputTag('TriggerResults::PAT'),
    metfilters     = cms.bool(True),

    # Jet cuts
    jet_cuts                 = cms.bool(True),
    jet_minpt                = cms.double(30.0),
    jet_maxeta               = cms.double(5.0),
    min_jet                  = cms.int32(2),
    max_jet                  = cms.int32(4000),
    leading_jet_pt           = cms.double(30.0),

    # muon cuts
    muon_cuts                = cms.bool(True),
    muon_selector            = cms.bool(False),
    muon_selector_medium     = cms.bool(False),
    muon_useMiniIso          = cms.bool(True),
    muon_miniIso             = cms.double(0.2),
    loose_muon_miniIso       = cms.double(0.4),
    muon_reliso              = cms.double(0.2),
    muon_minpt               = cms.double(10.0),
    muon_maxeta              = cms.double(2.5),
    min_muon                 = cms.int32(0),
    loose_muon_selector      = cms.bool(False),
    loose_muon_selector_tight = cms.bool(False),
    loose_muon_reliso        = cms.double(0.4),
    loose_muon_minpt         = cms.double(10.0),
    loose_muon_maxeta        = cms.double(2.5),

    # electron cuts
    electron_cuts            = cms.bool(True),
    electron_minpt           = cms.double(10.0),
    electron_maxeta          = cms.double(2.5),
    electron_miniIso         = cms.double(0.1),
    min_electron             = cms.int32(0),
    loose_electron_minpt     = cms.double(10.0),
    loose_electron_maxeta    = cms.double(2.5),
    loose_electron_miniIso   = cms.double(0.4),
    electron_CutsPlusMVA     = cms.bool(False),
    UseElMVA_tight           = cms.bool(True),
    UseElMVA                 = cms.bool(True),
    tight_electron_mva_cuts  = cms.vdouble(0.967083,0.929117,0.726311), # ~80% el efficiency WP
    loose_electron_mva_cuts  = cms.vdouble(0.913286,0.805013,0.358969), # ~90% el efficiency WP

    ElMVAweightFiles = cms.vstring(
        relBase+'/src/LJMet/Com/weights/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        ),

    # more lepton cuts
    min_lepton               = cms.int32(0),    # checks (N tight mu + N tight el) >= cut
    max_lepton               = cms.int32(1000),    # checks (N tight mu + N tight el) <= cut
    min_loose_lepton         = cms.int32(3),
    max_loose_lepton         = cms.int32(1000),
    second_lepton_veto       = cms.bool(False),  #checks (N tight lep > 0) AND (N loose lep > 0), vetoes if there are loose leptons.
    tau_veto		     = cms.bool(False),

    # MET cuts
    met_cuts                 = cms.bool(True),
    min_met                  = cms.double(30.0),
    max_met                  = cms.double(99999999999.9),

    # Btagging cuts
    btagOP                   = cms.string('CSVM'),
    btag_min_discr           = cms.double(0.800),
    btag_cuts                = cms.bool(False),
    btag_1                   = cms.bool(False),
    btag_2                   = cms.bool(False),
    btag_3                   = cms.bool(False),

    # Define the branch names of object collections in the input miniAOD file
    trigger_collection       = cms.InputTag('TriggerResults::HLT'),
    pv_collection            = cms.InputTag('offlineSlimmedPrimaryVertices'),
    jet_collection           = cms.InputTag('slimmedJets'),
    muon_collection          = cms.InputTag('slimmedMuons'),
    electron_collection      = cms.InputTag('slimmedElectrons'),
    tau_collection	     = cms.InputTag('slimmedTaus'),
    met_collection           = cms.InputTag('slimmedMETs'),

    # Jet corrections are read from txt files which need updating!
    BTagUncertUp             = cms.bool(False),
    BTagUncertDown           = cms.bool(False),
    JECup                    = cms.bool(False),
    JECdown                  = cms.bool(False),
    JERup                    = cms.bool(False),
    JERdown                  = cms.bool(False),
    doNewJEC                 = cms.bool(True),
    doLepJetCleaning         = cms.bool(True),
    CleanLooseLeptons        = cms.bool(True),
    LepJetDR                 = cms.double(0.4),

    JEC_txtfile = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_Uncertainty_AK4PFchs.txt'),
    JERSF_txtfile = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_MC_SF_AK4PFchs.txt'),
    JER_txtfile = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_MC_PtResolution_AK4PFchs.txt'),
    JERAK8_txtfile = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_MC_PtResolution_AK8PFchs.txt'),

    MCL1JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L1FastJet_AK4PFchs.txt'),
    MCL2JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L2Relative_AK4PFchs.txt'),
    MCL3JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L3Absolute_AK4PFchs.txt'),

    MCL1JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L1FastJet_AK8PFchs.txt'),
    MCL2JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L2Relative_AK8PFchs.txt'),
    MCL3JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV1_MC_L3Absolute_AK8PFchs.txt'),

    DataL1JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L1FastJet_AK4PFchs.txt'),
    DataL2JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2Relative_AK4PFchs.txt'),
    DataL3JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L3Absolute_AK4PFchs.txt'),
    DataResJetPar            = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2L3Residual_AK4PFchs.txt'),

    DataL1JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L1FastJet_AK8PFchs.txt'),
    DataL2JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2Relative_AK8PFchs.txt'),
    DataL3JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L3Absolute_AK8PFchs.txt'),
    DataResJetParAK8         = cms.string(relBase+'/src/LJMet/Com/data/Fall15_25nsV2_DATA_L2L3Residual_AK8PFchs.txt')

    )


#######################################################
#
# Input files
#

process.inputs = cms.PSet (
    nEvents    = cms.int32(-1),
    skipEvents = cms.int32(0),
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
    fileNames  = cms.vstring('root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/0C628838-21B9-E511-9025-842B2B0A39C8.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/1E351482-E9B8-E511-A4C2-782BCB539AB1.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/38767B14-DBB8-E511-BFD5-B083FED04D68.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/3AD69826-85B9-E511-BB39-001EC94BE81B.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/4EAB922F-85B9-E511-8ED6-D4AE527F338C.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/645EA09E-F4B8-E511-97F0-141877410B85.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/74C162CE-1BB9-E511-B5D7-B083FED43141.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/76E24B21-85B9-E511-87C3-1418774124DE.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/9A532095-E9B8-E511-979D-D4AE526DF45D.root',
'root://cmseos.fnal.gov//store/mc/RunIIFall15MiniAODv2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/A4A1223E-2CB9-E511-BBFE-0019B9CAF827.root',
)
    )


# JSON
if (not process.ljmet.isMc==cms.bool(True)):
    JsonFile = relBase+'/src/LJMet/Com/data/json/'+condorJSON
    myList   = LumiList.LumiList(filename=JsonFile).getCMSSWString().split(',')
    process.inputs.lumisToProcess.extend(myList)


#######################################################
#
# Output
#
process.outputs = cms.PSet (
    outputName = cms.string('TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8_1'),
    treeName   = cms.string('ljmet'),
    )

#######################################################
#
# Object selector options
#
# Primary vertex
process.load('PhysicsTools.SelectorUtils.pvSelector_cfi')
process.pvSelector.pvSrc   = cms.InputTag('offlineSlimmedPrimaryVertices')
process.pvSelector.minNdof = cms.double(4.0)
process.pvSelector.maxZ    = cms.double(24.0)
process.pvSelector.maxRho  = cms.double(2.0)

# jets
process.load('PhysicsTools.SelectorUtils.pfJetIDSelector_cfi')
process.pfJetIDSelector.version = cms.string('FIRSTDATA')
process.pfJetIDSelector.quality = cms.string('LOOSE')

# Tight muon
process.load('LJMet.Com.pfMuonSelector_cfi') #not used

# Loose muon
process.LoosepfMuonSelector = process.pfMuonSelector.clone() #not used

# Tight electron for 25ns
process.load('LJMet.Com.TopElectronSelector_cfi')
process.TopElectronSelector.version = cms.string('NONE') #not used

#Loose electron for 25ns
process.LooseTopElectronSelector = process.TopElectronSelector.clone() #not used
process.LooseTopElectronSelector.version = cms.string('NONE')
