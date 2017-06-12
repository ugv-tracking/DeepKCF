# Deep KCF trackers

This tracker is KCF based one with CNN features, and this version is made for both OTB and VOT evaluation.

## Eval on OTB

* Download the OTB evaluation benchmark
	git clone git@github.com:ugv-tracking/OTB_Tracker.git
	
* Download the OTB sequence from the OTB website.

* Download the DeepKCF
	cd OTB_Tracker/trackers
	git clone git@github.com:ugv-tracking/DeepKCF.git

* Evaluation 
	open Matlab and change the dir to OTB_Tracker
	run main_running.m
	
* Configure the images sequences and compartive trackers
	check util/configSeqs.m
	check util/configTrackers.m

* Draw figures
	run perfPlot.m

## Eval on VOT

* Download VOT evaluation benchmark
	git clone git@github.com:ugv-tracking/VOT-Tracker.git

* Download Tracker 
	cd VOT-Tracker/workspace_DKCF
	git clone git@github.com:ugv-tracking/DeepKCF.git

* Evaluation
	cd VOT-Tracker/workspace_DKCF
	run_experiments.m % This script can be used to execute the experiments for a single tracker
	run_test.m % This script can be used to test the integration of a tracker to the framework.
	run_analysis.m % This script can be used to perform a comparative analyis of the experiments in the same manner as for the VOT challenge.

## Modify Tracker

Check tracker.py, DeepKCF_OTB.py and DeepKCF_VOT.py

