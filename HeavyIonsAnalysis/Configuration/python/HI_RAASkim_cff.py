import FWCore.ParameterSet.Config as cms

# HLT jet trigger
import HLTrigger.HLTfilters.hltHighLevel_cfi
hltHIJet150 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltHIJet150.HLTPaths = ["HLT_PuAK4CaloJet150*","HLT_AK4CaloJet150_*"]
hltHIJet150.throw = False
hltHIJet150.andOr = True

HIJet150SkimSequence = cms.Sequence(
	hltHIJet150
)
