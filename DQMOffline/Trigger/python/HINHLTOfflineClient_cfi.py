import FWCore.ParameterSet.Config as cms

hinClient = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/HIN/HLT_HIHFCoinc*",\
                                           "HLT/HIN/HLT_PuAK4CaloJet40_v*"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
    outputFileName = cms.untracked.string(''),
    commands       = cms.vstring(),
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
        "HFEffTEST 'Efficiency' FromReco_Eff_nominator FromReco_Eff_denominator",
        "EffVsLeading 'Efficiency' recoCaloJets_pt recoCaloJets_Eff_denominator_pt"
    ),
)

