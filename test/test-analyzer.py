import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
from Configuration.Eras.Modifier_phase2_ecal_devel_cff import phase2_ecal_devel
from Configuration.Eras.Modifier_phase2_ecalTP_devel_cff import phase2_ecalTP_devel

process = cms.Process('REPR',eras.Phase2C17I13M9,phase2_ecal_devel,phase2_ecalTP_devel)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D86Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D86_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
#                                'root://cmsxrootd.fnal.gov///store/mc/Phase2HLTTDRWinter20DIGI/DoubleElectron_FlatPt-1To100/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/20000/40A5AD90-B259-4646-B473-2443964A1C15.root',
                                'root://cms-xrd-global.cern.ch///store/mc/Phase2Fall22DRMiniAOD/DoubleElectron_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0024ebea-73de-496a-9d75-6f0a7c3b2ba4.root'

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
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T25', '')


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
process.digi2raw_step = cms.Path(process.DigiToRaw)

process.pL1EG = cms.Path(process.simEcalEBTriggerPrimitivePhase2Digis * process.l1tPhase2L1CaloEGammaEmulator * process.l1tEGammaClusterEmuProducer * process.l1NtupleProducer)

# output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('analyzer-NewECAL-test.root')
)

process.Out = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "phase2L1EGammaAnalyzer.root" ),
    outputCommands = cms.untracked.vstring(
        "drop *"
        "keep *_l1tPhase2L1CaloEGammaEmulator_*_*",
        "keep *_simEcalEBTriggerPrimitivePhase2Digis_*_*",
# #        "keep *_Phase2L1CaloEGammaEmulatorProducer_*_*",
# #        "keep *_TriggerResults_*_*",
# #        "keep *_simHcalTriggerPrimitiveDigis_*_*",
# #        "keep *_EcalEBTrigPrimProducer_*_*"
     )
 )


# process.end = cms.EndPath( process.Out )

process.schedule = cms.Schedule(process.digitisation_step, process.digi2raw_step, process.pL1EG)

#dump_file = open("dump_file.py", "w")
#dump_file.write(process.dumpPython())
