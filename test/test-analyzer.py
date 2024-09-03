import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
from Configuration.Eras.Modifier_phase2_ecal_devel_cff import phase2_ecal_devel
from Configuration.Eras.Modifier_phase2_ecalTP_devel_cff import phase2_ecalTP_devel

process = cms.Process('REPR',Phase2C17I13M9,phase2_ecal_devel,phase2_ecalTP_devel)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D95Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #'root://cms-xrd-global.cern.ch//store/mc/Phase2Spring23DIGIRECOMiniAOD/DoubleElectron_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/0083e06c-959e-4ea5-9190-fd73667fcc00.root'
                                #'file:/eos/user/a/aquinn/DigiCollection_25Jul24/CMSSW_14_1_0_pre5/src/L1Trigger/L1CaloTrigger/test/0083e06c-959e-4ea5-9190-fd73667fcc00.root',
                                'root://xrootd-cms.infn.it//store/mc/Phase2Spring23DIGIRECOMiniAOD/DoubleElectron_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/9b330c43-b69f-40b8-bf04-40500eb7b017.root',

                                                      ),
                            inputCommands = cms.untracked.vstring(
                                "keep *"
                            )
                        )

# process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange("1:3774")
# process.source.eventsToProcess = cms.untracked.VEventRange("1:667914")

# --------------------------------------------------------------------------------------------                                                    
#                                                                                                                                                            
# ----   Run the relevant algorithms
# ---- Global Tag :
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun4_realistic_v6', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')


# Add HCAL Transcoder
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load('CalibCalorimetry.CaloTPG.CaloTPGTranscoder_cfi')

# --------------------------------------------------------------------------------------------
#
# -----   Produce the L1EGCrystal clusters using Emulator

process.load('L1Trigger.L1CaloTrigger.l1tPhase2L1CaloEGammaEmulator_cfi')
process.load('L1Trigger.L1CaloPhase2Analyzer.l1TCaloEGammaAnalyzer_cfi')
process.load('L1Trigger.L1CaloTrigger.l1tEGammaCrystalsEmulatorProducer_cfi')
process.load('SimCalorimetry.EcalEBTrigPrimProducers.ecalEBTriggerPrimitivePhase2Digis_cfi')

process.digitisation_step = cms.Path(process.pdigi_valid)

process.pL1EG = cms.Path(process.simEcalEBTriggerPrimitivePhase2Digis * process.l1tPhase2L1CaloEGammaEmulator * process.l1tEGammaClusterEmuProducer * process.l1NtupleProducer)

# output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('/afs/cern.ch/user/a/aquinn/analyzer-NewECAL-test_all_14aug.root')
    #fileName = cms.string('/afs/cern.ch/user/a/aquinn/phase2L1EGammaAnalyzer.root')
)

process.Out = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "/afs/cern.ch/user/a/aquinn/phase2L1EGammaAnalyzer_6aug.root" ),
    outputCommands = cms.untracked.vstring(
        "drop *",
        "keep *_simEcalTriggerPrimitiveDigis_*_*",
        "keep *_simEcalEBTriggerPrimitivePhase2Digis_*_*"

     )
 )


process.end = cms.EndPath( process.Out )

#want new collection in output root file
process.schedule = cms.Schedule(process.digitisation_step, process.pL1EG)

#dump_file = open("dump_file.py", "w")
#dump_file.write(process.dumpPython())
