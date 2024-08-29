# crab_template_cfg.py
# Variables like 'test_Analyzer_DoubleElectron_FlatPt-1To100-gun_Phase2Spring23DIGIRECOMiniAOD' are replaced using a configuration .yml
# and the parseYaml.py wrapper

from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = Configuration()

config.section_("General")
config.General.workArea     = 'crab_projects'
config.General.requestName  = 'test_Analyzer_DoubleElectron_FlatPt-1To100-gun_Phase2Spring23DIGIRECOMiniAOD'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = '/eos/user/a/aquinn/DigiCollection_25Jul24/CMSSW_14_1_0_pre5/src/L1Trigger/L1CaloPhase2Analyzer/test/test-analyzer_crab.py'
config.JobType.outputFiles = ['analyzer.root']

config.section_("Data")
config.Data.inputDataset = '/DoubleElectron_FlatPt-1To100-gun/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD'
# root://xrootd-cms.infn.it//store/mc/Phase2Spring23DIGIRECOMiniAOD/DoubleElectron_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/30000/9b330c43-b69f-40b8-bf04-40500eb7b017.root
config.Data.inputDBS     = 'global'
config.Data.unitsPerJob  = 2
config.Data.splitting    = 'FileBased'

config.Data.outLFNDirBase    = '/store/user/aquinn/DigiCollection_25Jul24/CrabOutput/'
config.Data.publication      = True
config.Data.outputDatasetTag = 'Analyzer_DoubleElectron_FlatPt-1To100-gun_Phase2Spring23DIGIRECOMiniAOD'

# config.JobType.maxJobRuntimeMin = 300
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 9000

config.section_("Site")
# config.Site.storageSite = "T2_US_Wisconsin"
config.Site.storageSite = "T3_CH_CERNBOX"
