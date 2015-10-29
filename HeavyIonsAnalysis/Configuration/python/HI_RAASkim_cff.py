import FWCore.ParameterSet.Config as cms

# HLT jet trigger
import HLTrigger.HLTfilters.hltHighLevel_cfi
hltHIJet150 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltHIJet150.HLTPaths = ["HLT_HIJet150*","HLT_Jet150*"]
hltHIJet150.throw = False
hltHIJet150.andOr = True

HIJet150SkimSequence = cms.Sequence(
	hltHIJet150
)

#event content
hltHIJet150_EventContent = cms.PSet(
	outputCommands = cms.untracked.vstring(
		'drop *',
		#------- RAW content ------
		'keep L1GlobalTriggerObjectMapRecord_*_*',
		'keep edmTriggerResults_*_*',
		'keep triggerTriggerEvent_*_*',
		'keep FEDRawDataCollection_*_*',
		#------- CaloJet collections ------
		'keep recoCaloJets_ak2CaloJets_*_*',
		'keep recoCaloJets_ak3CaloJets_*_*',
		'keep recoCaloJets_ak4CaloJets_*_*',
		'keep recoCaloJets_ak5CaloJets_*_*',
		'keep recoCaloJets_ak6CaloJets_*_*',
		'keep recoCaloJets_akPu2CaloJets_*_*',
		'keep recoCaloJets_akPu3CaloJets_*_*',
		'keep recoCaloJets_akPu4CaloJets_*_*',
		'keep recoCaloJets_akPu5CaloJets_*_*',
		'keep recoCaloJets_akPu6CaloJets_*_*',
		#------- Tracks collection --------
		'keep recoTracks_generalTracks_*_*',
		#------- CaloTower collection -----
		'keep *_towerMaker_*_*',
		#------- Various collections ------
		'keep *_EventAuxilary_*_*',
		'keep *_offlinePrimaryVertices_*_*',
		'keep *_hcalnoise_*_*')
)
