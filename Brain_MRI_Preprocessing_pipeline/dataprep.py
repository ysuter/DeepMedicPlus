#!/usr/bin/env python3

import json
import os.path

splitpath = "/home/yannick/PycharmProjects/brats-mets2023/experiments/ubelix/splitinfo.json"
dataroot = "/media/yannick/c4a7e8d3-9ac5-463f-b6e6-92e216ae6ac0/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData"
trainoutpath = "/home/yannick/PycharmProjects/DeepMedicPlus/DeepMedicPlus/examples/configFiles/deepMedicPlus/train"

with open(splitpath) as f:
    json_data = json.load(f)

trainoutfile_fold1 = os.path.join(trainoutpath, "trainChannels_t1c_fold0.cfg")
trainoutfile_gt_fold1 = os.path.join(trainoutpath, "trainGTLabels_fold0.cfg")
trainoutfile_fold2 = os.path.join(trainoutpath, "trainChannels_t1c_fold1.cfg")
trainoutfile_gt_fold2 = os.path.join(trainoutpath, "trainGTLabels_fold1.cfg")
trainoutfile_fold3 = os.path.join(trainoutpath, "trainChannels_t1c_fold2.cfg")
trainoutfile_gt_fold3 = os.path.join(trainoutpath, "trainGTLabels_fold2.cfg")

# training T1c channels
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

# validation T1c channels
valoutfile_fold1 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold0.cfg")
valoutfile_fold2 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold1.cfg")
valoutfile_fold3 = os.path.join(trainoutpath, 'validation', "validationChannels_t1c_fold2.cfg")

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

# test T1c channels
testoutfile = os.path.join(trainoutpath, '..', 'test', "testChannels_t1c_overall.cfg")

with open(testoutfile, "w") as f:
    for entry in json_data['overalltest']:
        print(entry)
        f.write(os.path.join(dataroot, entry, entry + "-t1c-biascorr-zscore.nii.gz") + '\n')