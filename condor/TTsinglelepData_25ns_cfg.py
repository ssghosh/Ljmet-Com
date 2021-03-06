import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

# Define the base process
process = cms.Process("LJMetCom")

#Arguments from condor submit script which are used more than once
condorIsMC = bool(CONDOR_ISMC)
relBase    = str('CONDOR_RELBASE')
condorJSON = str('CONDOR_JSON')
############################################################
#
# FWLite application options
process.load('LJMet.Com.ljmet_cfi')
process.ljmet.isMc = cms.bool(condorIsMC)

# Exclude some unnecessary calculators from the process
process.ljmet.excluded_calculators = cms.vstring(
    #'TpTpCalc',
    'PileUpCalc',
#    'BTagSFCalc',
    'TprimeCalc',
    'DileptonCalc',
    'CATopoCalc',
    'DileptonEventSelector',
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
process.singleLepCalc.saveLooseLeps     = cms.bool(False)

# Jet substructure calculator options
process.load('LJMet.Com.JetSubCalc_cfi')
process.JetSubCalc.useHTT = cms.bool(False)
process.JetSubCalc.killHF = cms.bool(True)
process.JetSubCalc.doNewJEC = cms.bool(True)
process.JetSubCalc.useL2L3Mass = cms.bool(True)
process.JetSubCalc.isMc = cms.bool(condorIsMC)
process.JetSubCalc.JECup = cms.bool(False)
process.JetSubCalc.JECdown = cms.bool(False)
process.JetSubCalc.MCL2JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L2Relative_AK8PFchs.txt')
process.JetSubCalc.MCL3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L3Absolute_AK8PFchs.txt')
process.JetSubCalc.DataL2JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2Relative_AK8PFchs.txt')
process.JetSubCalc.DataL3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L3Absolute_AK8PFchs.txt')
process.JetSubCalc.DataL2L3JetParAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2L3Residual_AK8PFchs.txt')
process.JetSubCalc.UncertaintyAK8 = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_Uncertainty_AK8PFchs.txt')

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

    trigger_path_el = cms.vstring(
        'HLT_Ele105_CaloIdVT_GsfTrkIdT_v1',                          'HLT_Ele105_CaloIdVT_GsfTrkIdT_v2',                          'HLT_Ele105_CaloIdVT_GsfTrkIdT_v3',                          'HLT_Ele105_CaloIdVT_GsfTrkIdT_v4',                          
        'HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v1','HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v2','HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v3','HLT_Ele10_CaloIdM_TrackIdM_CentralPFJet30_BTagCSV0p54PF_v4',
        'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v1',                  'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v2',                  'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v3',                  'HLT_Ele15_IsoVVVL_BTagCSV0p72_PFHT400_v4',                  
        'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v1',                      'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v2',                      'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v3',                      'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v4',                      
        'HLT_Ele15_IsoVVVL_PFHT350_v1',                              'HLT_Ele15_IsoVVVL_PFHT350_v2',                              'HLT_Ele15_IsoVVVL_PFHT350_v3',                              'HLT_Ele15_IsoVVVL_PFHT350_v4',                              
        'HLT_Ele15_IsoVVVL_PFHT600_v1',                              'HLT_Ele15_IsoVVVL_PFHT600_v2',                              'HLT_Ele15_IsoVVVL_PFHT600_v3',                              'HLT_Ele15_IsoVVVL_PFHT600_v4',                              
        'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v1',                       'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v2',                       'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v3',                       'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v4',                       
        'HLT_Ele22_eta2p1_WPLoose_Gsf_v1',                           'HLT_Ele22_eta2p1_WPLoose_Gsf_v2',                           'HLT_Ele22_eta2p1_WPLoose_Gsf_v3',                           'HLT_Ele22_eta2p1_WPLoose_Gsf_v4',                           
        'HLT_Ele22_eta2p1_WPTight_Gsf_v1',                           'HLT_Ele22_eta2p1_WPTight_Gsf_v2',                           'HLT_Ele22_eta2p1_WPTight_Gsf_v3',                           'HLT_Ele22_eta2p1_WPTight_Gsf_v4',                           
        'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCVS07_v1',         'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCVS07_v2',         'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCVS07_v3',         'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCVS07_v4',         
        'HLT_Ele23_WPLoose_Gsf_TriCentralPFJet50_40_30_v1',          'HLT_Ele23_WPLoose_Gsf_TriCentralPFJet50_40_30_v2',          'HLT_Ele23_WPLoose_Gsf_TriCentralPFJet50_40_30_v3',          'HLT_Ele23_WPLoose_Gsf_TriCentralPFJet50_40_30_v4',          
        'HLT_Ele23_WPLoose_Gsf_v1',                                  'HLT_Ele23_WPLoose_Gsf_v2',                                  'HLT_Ele23_WPLoose_Gsf_v3',                                  'HLT_Ele23_WPLoose_Gsf_v4',                                  
        'HLT_Ele27_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',         'HLT_Ele27_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v2',         'HLT_Ele27_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v3',         'HLT_Ele27_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v4',         
        'HLT_Ele27_WPLoose_Gsf_TriCentralPFJet50_40_30_v1',          'HLT_Ele27_WPLoose_Gsf_TriCentralPFJet50_40_30_v2',          'HLT_Ele27_WPLoose_Gsf_TriCentralPFJet50_40_30_v3',          'HLT_Ele27_WPLoose_Gsf_TriCentralPFJet50_40_30_v4',          
        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v1',                        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v2',                        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v3',                        'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v4',                        
        'HLT_Ele27_WPLoose_Gsf_v1',                                  'HLT_Ele27_WPLoose_Gsf_v2',                                  'HLT_Ele27_WPLoose_Gsf_v3',                                  'HLT_Ele27_WPLoose_Gsf_v4',                                  
        'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v1',                     'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v2',                     'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v3',                     'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v4',                     
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v1',                           'HLT_Ele27_eta2p1_WPLoose_Gsf_v2',                           'HLT_Ele27_eta2p1_WPLoose_Gsf_v3',                           'HLT_Ele27_eta2p1_WPLoose_Gsf_v4',                           
        'HLT_Ele27_eta2p1_WPTight_Gsf_v1',                           'HLT_Ele27_eta2p1_WPTight_Gsf_v2',                           'HLT_Ele27_eta2p1_WPTight_Gsf_v3',                           'HLT_Ele27_eta2p1_WPTight_Gsf_v4',                           
        'HLT_Ele30WP60_SC4_Mass55_v1',                               'HLT_Ele30WP60_SC4_Mass55_v2',                               'HLT_Ele30WP60_SC4_Mass55_v3',                               'HLT_Ele30WP60_SC4_Mass55_v4',                               
        'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',  'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v2',  'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v3',  'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v4',  
        'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v1',         'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v2',         'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v3',         'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v4',         
        'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v1',   'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v2',   'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v3',   'HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v4',   
        'HLT_Ele32_eta2p1_WPLoose_Gsf_v1',                           'HLT_Ele32_eta2p1_WPLoose_Gsf_v2',                           'HLT_Ele32_eta2p1_WPLoose_Gsf_v3',                           'HLT_Ele32_eta2p1_WPLoose_Gsf_v4',                           
        'HLT_Ele32_eta2p1_WPTight_Gsf_v1',                           'HLT_Ele32_eta2p1_WPTight_Gsf_v2',                           'HLT_Ele32_eta2p1_WPTight_Gsf_v3',                           'HLT_Ele32_eta2p1_WPTight_Gsf_v4',                           
        'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1',          'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v2',          'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v3',          'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v4',          
        ),
    trigger_path_mu = cms.vstring(
        'HLT_IsoMu18_CentralPFJet30_BTagCSV07_v1',       'HLT_IsoMu18_CentralPFJet30_BTagCSV07_v2',       'HLT_IsoMu18_CentralPFJet30_BTagCSV07_v3',       'HLT_IsoMu18_CentralPFJet30_BTagCSV07_v4',       
        'HLT_IsoMu18_TriCentralPFJet50_40_30_v1',        'HLT_IsoMu18_TriCentralPFJet50_40_30_v2',        'HLT_IsoMu18_TriCentralPFJet50_40_30_v3',        'HLT_IsoMu18_TriCentralPFJet50_40_30_v4',        
        'HLT_IsoMu18_v1',                                'HLT_IsoMu18_v2',                                'HLT_IsoMu18_v3',                                'HLT_IsoMu18_v4',                                
        'HLT_IsoMu20_v1',                                'HLT_IsoMu20_v2',                                'HLT_IsoMu20_v3',                                'HLT_IsoMu20_v4',                                
        'HLT_IsoTkMu20_v1',                                'HLT_IsoTkMu20_v2',                                'HLT_IsoTkMu20_v3',                                'HLT_IsoTkMu20_v4',                                
        'HLT_IsoMu22_CentralPFJet30_BTagCSV07_v1',       'HLT_IsoMu22_CentralPFJet30_BTagCSV07_v2',       'HLT_IsoMu22_CentralPFJet30_BTagCSV07_v3',       'HLT_IsoMu22_CentralPFJet30_BTagCSV07_v4',       
        'HLT_IsoMu22_TriCentralPFJet50_40_30_v1',        'HLT_IsoMu22_TriCentralPFJet50_40_30_v2',        'HLT_IsoMu22_TriCentralPFJet50_40_30_v3',        'HLT_IsoMu22_TriCentralPFJet50_40_30_v4',        
        'HLT_IsoMu22_v1',                                'HLT_IsoMu22_v2',                                'HLT_IsoMu22_v3',                                'HLT_IsoMu22_v4',                                
        'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v1','HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v2','HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v3','HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v4',
        'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v1',       'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v2',       'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v3',       'HLT_IsoMu24_eta2p1_TriCentralPFJet30_v4',       
        'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v1', 'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v2', 'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v3', 'HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v4', 
        'HLT_IsoMu27_v1',                                'HLT_IsoMu27_v2',                                'HLT_IsoMu27_v3',                                'HLT_IsoMu27_v4',                                
        'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v1',       'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v2',       'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v3',       'HLT_Mu15_IsoVVVL_BTagCSV0p72_PFHT400_v4',       
        'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v1',           'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v2',           'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v3',           'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v4',           
        'HLT_Mu15_IsoVVVL_PFHT350_v1',                   'HLT_Mu15_IsoVVVL_PFHT350_v2',                   'HLT_Mu15_IsoVVVL_PFHT350_v3',                   'HLT_Mu15_IsoVVVL_PFHT350_v4',                   
        'HLT_Mu15_IsoVVVL_PFHT600_v1',                   'HLT_Mu15_IsoVVVL_PFHT600_v2',                   'HLT_Mu15_IsoVVVL_PFHT600_v3',                   'HLT_Mu15_IsoVVVL_PFHT600_v4',                   
        'HLT_Mu17_TrkIsoVVL_v1',                         'HLT_Mu17_TrkIsoVVL_v2',                         'HLT_Mu17_TrkIsoVVL_v3',                         'HLT_Mu17_TrkIsoVVL_v4',                         
        'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1',           'HLT_Mu40_eta2p1_PFJet200_PFJet50_v2',           'HLT_Mu40_eta2p1_PFJet200_PFJet50_v3',           'HLT_Mu40_eta2p1_PFJet200_PFJet50_v4',           
        'HLT_Mu45_eta2p1_v1',                            'HLT_Mu45_eta2p1_v2',                            'HLT_Mu45_eta2p1_v3',                            'HLT_Mu45_eta2p1_v4',                            
        'HLT_Mu50_v1',                                   'HLT_Mu50_v2',                                   'HLT_Mu50_v3',                                   'HLT_Mu50_v4',                                   
        'HLT_Mu55_v1',                                   'HLT_Mu55_v2',                                   'HLT_Mu55_v3',                                   'HLT_Mu55_v4',                                   
        ),   
    
    mctrigger_path_el = cms.vstring(''),
    mctrigger_path_mu = cms.vstring(''),   
    
    # PV cuts
    pv_cut         = cms.bool(True),
    hbhe_cut       = cms.bool(True),
    hbheiso_cut    = cms.bool(True),
    hbhe_cut_value = cms.string('Run2Loose'),
    csc_cut        = cms.bool(False),
    flag_tag       = cms.InputTag('TriggerResults::RECO'),
    eesc_cut       = cms.bool(True),
    
    # Jet cuts
    jet_cuts                 = cms.bool(True),
    jet_minpt                = cms.double(30.0),
    jet_maxeta               = cms.double(2.4),
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
#    muon_reliso              = cms.double(0.12),
    muon_minpt               = cms.double(30.0),
    muon_maxeta              = cms.double(2.4),
    min_muon                 = cms.int32(0),
    loose_muon_selector      = cms.bool(False),
    loose_muon_selector_tight = cms.bool(False),
    loose_muon_reliso        = cms.double(0.4),
#    loose_muon_reliso        = cms.double(0.2),
    loose_muon_minpt         = cms.double(10.0),
    loose_muon_maxeta        = cms.double(2.4),
    
    # electron cuts
    electron_cuts            = cms.bool(True),
    electron_minpt           = cms.double(30.0),
    electron_maxeta          = cms.double(2.1),
    electron_miniIso         = cms.double(0.1),
#    electron_miniIso         = cms.double(-1), #not used
    electron_CutsPlusMVA     = cms.bool(False),
    min_electron             = cms.int32(0),
    loose_electron_minpt     = cms.double(10.0),
    loose_electron_maxeta    = cms.double(2.1),
    loose_electron_miniIso   = cms.double(0.4),
#    loose_electron_miniIso   = cms.double(-1), #not used
    UseElMVA                 = cms.bool(True),
    UseElMVA_tight           = cms.bool(True),
    tight_electron_mva_cuts  = cms.vdouble(0.967083,0.929117,0.726311), # ~80% el efficiency WP
    loose_electron_mva_cuts  = cms.vdouble(0.913286,0.805013,0.358969), # ~90% el efficiency WP

    ElMVAweightFiles = cms.vstring(
        relBase+'/src/LJMet/Com/weights/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml',
        relBase+'/src/LJMet/Com/weights/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml',
        ),

    # more lepton cuts
    min_lepton               = cms.int32(1),    # checks (N tight mu + N tight el) >= cut
    max_lepton               = cms.int32(1),    # checks (N tight mu + N tight el) <= cut
    min_loose_lepton         = cms.int32(0),
    max_loose_lepton         = cms.int32(1000),
    second_lepton_veto       = cms.bool(True),  #checks (N tight lep > 0) AND (N loose lep > 0), vetoes if there are loose leptons.
    tau_veto		     = cms.bool(False),
    
    # MET cuts
    met_cuts                 = cms.bool(True),
    min_met                  = cms.double(20.0),
    max_met                  = cms.double(99999999999.0),
    
    # Btagging cuts
    btagOP                   = cms.string('CSVM'),
    btag_min_discr           = cms.double(0.890),
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
    JEC_txtfile = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_UncertaintySources_AK4PFchs.txt'),
    doNewJEC                 = cms.bool(True),
    doLepJetCleaning         = cms.bool(True),
    
    MCL1JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L1FastJet_AK4PFchs.txt'),
    MCL2JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L2Relative_AK4PFchs.txt'),
    MCL3JetPar               = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L3Absolute_AK4PFchs.txt'),

    MCL1JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L1FastJet_AK8PFchs.txt'),
    MCL2JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L2Relative_AK8PFchs.txt'),
    MCL3JetParAK8            = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_MC_L3Absolute_AK8PFchs.txt'),

    DataL1JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L1FastJet_AK4PFchs.txt'),
    DataL2JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2Relative_AK4PFchs.txt'),
    DataL3JetPar             = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L3Absolute_AK4PFchs.txt'),
    DataResJetPar            = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2L3Residual_AK4PFchs.txt'),

    DataL1JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L1FastJet_AK8PFchs.txt'),
    DataL2JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2Relative_AK8PFchs.txt'),
    DataL3JetParAK8          = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L3Absolute_AK8PFchs.txt'),
    DataResJetParAK8         = cms.string(relBase+'/src/LJMet/Com/data/Summer15_25nsV7_DATA_L2L3Residual_AK8PFchs.txt')

    )


#######################################################
#
# Input files
#

process.inputs = cms.PSet (
    nEvents    = cms.int32(-1),
    skipEvents = cms.int32(0),
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
    fileNames  = cms.vstring(CONDOR_FILELIST)
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
    outputName = cms.string('CONDOR_OUTFILE'),
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
process.load('LJMet.Com.pfMuonSelector_cfi') 
#process.pfMuonSelector.cutsToIgnore = cms.vstring('maxPfRelIso')

# Loose muon
process.LoosepfMuonSelector = process.pfMuonSelector.clone()
process.LoosepfMuonSelector.Chi2 = cms.double(50.0)
process.LoosepfMuonSelector.maxIp = cms.double(2.0)
process.LoosepfMuonSelector.maxPfRelIso = cms.double(0.2)
process.LoosepfMuonSelector.cutsToIgnore = cms.vstring('minMatchedStations','minTrackerLayers') #,'maxPfRelIso')

# Tight electron for 25ns
process.load('LJMet.Com.TopElectronSelector_cfi')
process.TopElectronSelector.version = cms.string('NONE')
#process.TopElectronSelector.cutsToIgnore = cms.vstring('reliso_EE','reliso_EB')
process.TopElectronSelector.deta_EB	  = cms.double(0.00926) #abs(dEtaIn)
process.TopElectronSelector.dphi_EB	  = cms.double(0.0336) #abs(dPhiIn) 
process.TopElectronSelector.sihih_EB	  = cms.double(0.0101) #full5x5_sigmaIetaIeta 
process.TopElectronSelector.hoe_EB	  = cms.double(0.0597) #hOverE 
process.TopElectronSelector.d0_EB	  = cms.double(0.0111) #abs(d0) 
process.TopElectronSelector.dZ_EB	  = cms.double(0.0466) #abs(dz)  
process.TopElectronSelector.ooemoop_EB	  = cms.double(0.012) #ooEmooP 
process.TopElectronSelector.reliso_EB	  = cms.double(0.0354) #relIsoWithEA 
process.TopElectronSelector.deta_EE	  = cms.double(0.00724) #abs(dEtaIn)
process.TopElectronSelector.dphi_EE	  = cms.double(0.0918) #abs(dPhiIn)  
process.TopElectronSelector.sihih_EE	  = cms.double(0.0279) #full5x5_sigmaIetaIeta
process.TopElectronSelector.hoe_EE	  = cms.double(0.0615) #hOverE
process.TopElectronSelector.d0_EE	  = cms.double(0.0351) #abs(d0) 
process.TopElectronSelector.dZ_EE	  = cms.double(0.417) #abs(dz) 
process.TopElectronSelector.ooemoop_EE	  = cms.double(0.00999) #ooEmooP 
process.TopElectronSelector.reliso_EE	  = cms.double(0.0646) #relIsoWithEA
                   	       
#Loose electron for 25ns
process.LooseTopElectronSelector = process.TopElectronSelector.clone()
process.LooseTopElectronSelector.version = cms.string('NONE')
 #process.LooseTopElectronSelector.cutsToIgnore = cms.vstring('reliso_EE','reliso_EB')
process.LooseTopElectronSelector.deta_EB	  = cms.double(0.0105) #abs(dEtaIn)
process.LooseTopElectronSelector.dphi_EB	  = cms.double(0.115) #abs(dPhiIn) 
process.LooseTopElectronSelector.sihih_EB	  = cms.double(0.0103) #full5x5_sigmaIetaIeta 
process.LooseTopElectronSelector.hoe_EB           = cms.double(0.104) #hOverE 
process.LooseTopElectronSelector.d0_EB		  = cms.double(0.0261) #abs(d0) 
process.LooseTopElectronSelector.dZ_EB		  = cms.double(0.41) #abs(dz)  
process.LooseTopElectronSelector.ooemoop_EB	  = cms.double(0.102) #ooEmooP 
process.LooseTopElectronSelector.reliso_EB	  = cms.double(0.0893) #relIsoWithEA 
process.LooseTopElectronSelector.deta_EE	  = cms.double(0.00814) #abs(dEtaIn)
process.LooseTopElectronSelector.dphi_EE	  = cms.double(0.182) #abs(dPhiIn)  
process.LooseTopElectronSelector.sihih_EE	  = cms.double(0.0301) #full5x5_sigmaIetaIeta
process.LooseTopElectronSelector.hoe_EE	          = cms.double(0.0897) #hOverE
process.LooseTopElectronSelector.d0_EE		  = cms.double(0.118) #abs(d0) 
process.LooseTopElectronSelector.dZ_EE		  = cms.double(0.822) #abs(dz) 
process.LooseTopElectronSelector.ooemoop_EE	  = cms.double(0.126) #ooEmooP 
process.LooseTopElectronSelector.reliso_EE	  = cms.double(0.121) #relIsoWithEA


