# Phase 2 L1 Calo Analyzer

## Description

   Adapted from: https://github.com/skkwan/phase2-l1Calo-analyzer .
   This repo is for running the Phase-2 calo emulator.

## Setup (do only once)

   ```
   cmsrel CMSSW_14_1_0_pre5
   cd CMSSW_14_1_0_pre5/src
   cmsenv
   git cms-init
   git cms-addpkg L1Trigger/L1TCalorimeter
   cd L1Trigger
   git clone git@github.com:pallabidas/L1CaloPhase2Analyzer.git -b 13_3_0_calojet
   cd ../
   scram b -j 12
   ```

## To run the emulator and create ntuples for the event display, efficiency plots

   For getting the ntuple:
   ```
   cd L1Trigger/L1CaloPhase2Analyzer/test/
   cmsRun test-analyzer.py
   ```

   For the GCT jet efficiency plots using the ntuple as input (changing file paths needed in plotting script):
   ```
   cd L1Trigger/L1CaloPhase2Analyzer/figures/efficiencyPlots/
   root -l -b -q makeEfficienciesPlotJet.cpp
   ```

   For the event display plots using the ntuple as input (changing file paths needed in plotting script):
   ```
   cd L1Trigger/L1CaloPhase2Analyzer/figures/eventDisplays/
   root -l -b -q plotEventDisplayPhaseIICaloJets.C
   ```
