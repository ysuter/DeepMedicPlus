#!/usr/bin/env python3

import json
import os.path

# splitpath = "/home/yannick/PycharmProjects/brats-mets2023/experiments/ubelix/splitinfo.json"
splitpath = "/home/ysuter/brats-mets/data/splitinfo.json"
# dataroot = "/media/yannick/c4a7e8d3-9ac5-463f-b6e6-92e216ae6ac0/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData"
dataroot = "/home/ysuter/brats-mets/data/trainingdata"
trainoutpath = "/home/yannick/PycharmProjects/DeepMedicPlus/DeepMedicPlus/examples/configFiles/deepMedicPlus/train"

# create train T1c channel configs for all splits
with open(splitpath) as f:
    json_data = json.load(f)

trainoutfile_fold1 = os.path.join(trainoutpath, "trainChannels_t1c_fold0.cfg")
trainoutfile_gt_fold1 = os.path.join(trainoutpath, "trainGTLabels_fold0.cfg")
trainoutfile_fold2 = os.path.join(trainoutpath, "trainChannels_t1c_fold1.cfg")
trainoutfile_gt_fold2 = os.path.join(trainoutpath, "trainGTLabels_fold1.cfg")
trainoutfile_fold3 = os.path.join(trainoutpath, "trainChannels_t1c_fold2.cfg")
trainoutfile_gt_fold3 = os.path.join(trainoutpath, "trainGTLabels_fold2.cfg")

with open(trainoutfile_fold1, "w") as f:
    for entry in json_data['0']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')

with open(trainoutfile_fold2, "w") as f:
    for entry in json_data['1']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')


with open(trainoutfile_fold3, "w") as f:
    for entry in json_data['2']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')

# Training GT paths
with open(trainoutfile_gt_fold1, "w") as f:
    for entry in json_data['0']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

with open(trainoutfile_gt_fold2, "w") as f:
    for entry in json_data['1']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

with open(trainoutfile_gt_fold3, "w") as f:
    for entry in json_data['2']['train']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

# validation T1c channels
valoutfile_fold1 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold0.cfg")
valoutfile_fold2 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold1.cfg")
valoutfile_fold3 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold2.cfg")
valoutfile_gt_fold1 = os.path.join(trainoutpath, 'validation', "validationGTLabels_fold0.cfg")
valoutfile_gt_fold2 = os.path.join(trainoutpath, 'validation', "validationGTLabels_fold1.cfg")
valoutfile_gt_fold3 = os.path.join(trainoutpath, 'validation', "validationGTLabels_fold2.cfg")

with open(valoutfile_fold1, "w") as f:
    for entry in json_data['0']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')

with open(valoutfile_fold2, "w") as f:
    for entry in json_data['1']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')


with open(valoutfile_fold3, "w") as f:
    for entry in json_data['2']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')

# Validation GT paths
with open(valoutfile_gt_fold1, "w") as f:
    for entry in json_data['0']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

with open(valoutfile_gt_fold2, "w") as f:
    for entry in json_data['1']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

with open(valoutfile_gt_fold3, "w") as f:
    for entry in json_data['2']['test_cv']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')


# test T1c channels
testoutfile = os.path.join(trainoutpath, '..', 'test', "testChannels_t1c_overall.cfg")
testoutfile_gt = os.path.join(trainoutpath, '..', 'test', "testGtLabels_overall.cfg")

with open(testoutfile, "w") as f:
    for entry in json_data['overalltest']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')

with open(testoutfile_gt, "w") as f:
    for entry in json_data['overalltest']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-seg_cet.nii.gz") + '\n')

# Prior channels
priorchannels_train_fold1 = os.path.join(trainoutpath, "trainPriorChannels_fold0.cfg")
priorchannels_train_fold2 = os.path.join(trainoutpath, "trainPriorChannels_fold1.cfg")
priorchannels_train_fold3 = os.path.join(trainoutpath, "trainPriorChannels_fold2.cfg")

priorchannels_val_fold1 = os.path.join(trainoutpath, "validation", "validationPriorChannels_fold0.cfg")
priorchannels_val_fold2 = os.path.join(trainoutpath, "validation", "validationPriorChannels_fold1.cfg")
priorchannels_val_fold3 = os.path.join(trainoutpath, "validation", "validationPriorChannels_fold2.cfg")

testpriorchannels = os.path.join(trainoutpath, '..', 'test', "testPriorChannels_overall.cfg")

with open(priorchannels_train_fold1, "w") as f:
    for entry in json_data['0']['train']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(priorchannels_train_fold2, "w") as f:
    for entry in json_data['1']['train']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(priorchannels_train_fold3, "w") as f:
    for entry in json_data['2']['train']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(priorchannels_val_fold1, "w") as f:
    for entry in json_data['0']['test_cv']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(priorchannels_val_fold2, "w") as f:
    for entry in json_data['1']['test_cv']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(priorchannels_val_fold3, "w") as f:
    for entry in json_data['2']['test_cv']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

with open(testpriorchannels, "w") as f:
    for entry in json_data['overalltest']:
        f.write("/home/ysuter/brats-mets/data/!!AAZero_Volume.nii.gz" +  +"\n")

# ROI masks
trainroimask_fold1 = os.path.join(trainoutpath, "trainRoiMasks_fold0.cfg")
trainroimask_fold2 = os.path.join(trainoutpath, "trainRoiMasks_fold1.cfg")
trainroimask_fold3 = os.path.join(trainoutpath, "trainRoiMasks_fold2.cfg")

valroimask_fold1 = os.path.join(trainoutpath, 'validation', "validationRoiMasks_fold0.cfg")
valroimask_fold2 = os.path.join(trainoutpath, 'validation', "validationRoiMasks_fold1.cfg")
valroimask_fold3 = os.path.join(trainoutpath, 'validation', "validationRoiMasks_fold2.cfg")

testroimask = os.path.join(trainoutpath, '..', 'test', "testRoiMasks_overall.cfg")

with open(trainroimask_fold1, "w") as f:
    for entry in json_data['0']['train']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(trainroimask_fold2, "w") as f:
    for entry in json_data['1']['train']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(trainroimask_fold3, "w") as f:
    for entry in json_data['2']['train']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(valroimask_fold1, "w") as f:
    for entry in json_data['0']['test_cv']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(valroimask_fold2, "w") as f:
    for entry in json_data['1']['test_cv']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(valroimask_fold3, "w") as f:
    for entry in json_data['2']['test_cv']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

with open(testroimask, "w") as f:
    for entry in json_data['overalltest']:
        f.write(os.path.join(dataroot, entry, entry + "-brainmask.nii.gz") + '\n')

# prediction names
valprednames_fold1 = os.path.join(trainoutpath, 'validation', "validationNamesOfPredictions_fold0.cfg")
valprednames_fold2 = os.path.join(trainoutpath, 'validation', "validationNamesOfPredictions_fold1.cfg")
valprednames_fold3 = os.path.join(trainoutpath, 'validation', "validationNamesOfPredictions_fold2.cfg")

testprednames = os.path.join(trainoutpath, '..', 'test', "testNamesOfPrediction_overall.cfg")

with open(valprednames_fold1, "w") as f:
    for entry in json_data['0']['test_cv']:
        f.write(entry + "\n")

with open(valprednames_fold2, "w") as f:
    for entry in json_data['1']['test_cv']:
        f.write(entry + "\n")

with open(valprednames_fold3, "w") as f:
    for entry in json_data['2']['test_cv']:
        f.write(entry + "\n")

with open(testpriorchannels, "w") as f:
    for entry in json_data['overalltest']:
        f.write(entry + "\n")
