import FWCore.ParameterSet.Config as cms

hinClient = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/HIN/HLT_HIHFCoinc*"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
    outputFileName = cms.untracked.string(''),
    commands       = cms.vstring(),
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
        "effTESTHF 'Testing things' FromReco_Eff_nominator FromReco_Eff_denominator",
    ),
)

