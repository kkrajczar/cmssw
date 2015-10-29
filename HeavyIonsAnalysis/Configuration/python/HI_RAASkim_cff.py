import FWCore.ParameterSet.Config as cms

# HLT jet trigger
import HLTrigger.HLTfilters.hltHighLevel_cfi
hltHIJet150 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltHIJet150.HLTPaths = ["HLT_PuAK4CaloJet150*"]
hltHIJet150.throw = False
hltHIJet150.andOr = True

hltJet150 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltJet150.HLTPaths = ["HLT_AK4CaloJet150_*"]
hltJet150.throw = False
hltJet150.andOr = True

# selection of valid vertex
primaryHIVertexFilterForJets = cms.EDFilter("VertexSelector",
    src = cms.InputTag("hiSelectedVertex"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2"), 
    filter = cms.bool(True),   # otherwise it won't filter the events
    )

primaryPPVertexFilterForJets = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVerticesWithBS"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2"), 
    filter = cms.bool(True),   # otherwise it won't filter the events
    )

HIJet150SkimSequence = cms.Sequence(
        primaryHIVertexFilterForJets *
	hltHIJet150
)

Jet150SkimSequence = cms.Sequence(
        primaryPPVertexFilterForJets *
	hltJet150
)
