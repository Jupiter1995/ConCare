import csv
import os
import shutil
import pandas as pd
import numpy as np
from pathlib import Path

ROOT_DIR = os.path.dirname(Path(__file__).parent)
DATA_DIR = os.path.join(ROOT_DIR, "data")
TRAIN_DATA_DIR = os.path.join(DATA_DIR, "train")
TEST_DATA_DIR = os.path.join(DATA_DIR, "test")
ALL_DATA_DIR = os.path.join(DATA_DIR, "all")

TRAIN_LIST = os.path.join(DATA_DIR, "train_listfile.csv")
TEST_LIST = os.path.join(DATA_DIR, "test_listfile.csv")
VAL_LIST = os.path.join(DATA_DIR, "val_listfile.csv")
TRAIN_VAL_LIST = os.path.join(DATA_DIR, "train_val_listfile.csv")


print(TRAIN_LIST)


def copy_check_files(list_file, origin, dest, check=True):
    if not os.path.exists(dest):
        os.makedirs(dest)

    with open(list_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for i, row in enumerate(datareader):
            if i == 0:
                continue
            src = os.path.join(origin, row[0])
            if check:
                if not os.path.exists(src):
                    print('Not there: {}'.format(src))
            else:
                dst = os.path.join(dest, row[0])
                shutil.copyfile(src, dst)
                print('Copied {} to {}'.format(src, dest))
        print('Total: {}'.format(i))


def split_samples(list_file, split=0.8):
    origin_pd = pd.read_csv(list_file)
    stay_se = origin_pd['stay'].unique()
    split_count = int(len(stay_se) * split)
    np.random.shuffle(stay_se)
    stay_p1, stay_p2 = stay_se[:split_count], stay_se[split_count:]

    stay_p1_pd = origin_pd.loc[origin_pd.stay.isin(stay_p1), :]
    stay_p2_pd = origin_pd.loc[origin_pd.stay.isin(stay_p2), :]

    stay_p1_pd.to_csv('{}_part1'.format(list_file), index=False)
    stay_p2_pd.to_csv('{}_part2'.format(list_file), index=False)


def split_list_file(list_file, suffix, total_split=1, train_split=0.82):
    origin_pd = pd.read_csv(list_file)
    stay_se = origin_pd['stay'].unique()
    np.random.shuffle(stay_se)
    total_split_count = int(len(stay_se) * total_split)
    stay_se = stay_se[:total_split_count]

    train_split_idx = int(len(stay_se) * train_split)
    #val_split_idx = train_split_idx + int(len(stay_se) * val_split)
    #val_split_count = stay_se.shape[0] - test_split_idx

    stay_train = stay_se[:train_split_idx]
    stay_val = stay_se[train_split_idx:]

    stay_train_pd = origin_pd.loc[origin_pd.stay.isin(stay_train), :]
    #stay_test_pd = origin_pd.loc[origin_pd.stay.isin(stay_test), :]
    stay_val_pd = origin_pd.loc[origin_pd.stay.isin(stay_val), :]

    stay_train_pd.to_csv(os.path.join(DATA_DIR, '{}_train_listfile.csv'.format(suffix)), index=False)
    #stay_test_pd.to_csv(os.path.join(DATA_DIR, '{}_test_listfile.csv'.format(suffix)), index=False)
    stay_val_pd.to_csv(os.path.join(DATA_DIR, '{}_val_listfile.csv'.format(suffix)), index=False)

    print(train_split_idx)


split_list_file(TRAIN_VAL_LIST, 'split0')
split_list_file(TRAIN_VAL_LIST, 'split1', total_split=0.9)
split_list_file(TRAIN_VAL_LIST, 'split2', total_split=0.8)
split_list_file(TRAIN_VAL_LIST, 'split3', total_split=0.7)
split_list_file(TRAIN_VAL_LIST, 'split4', total_split=0.6)
split_list_file(TRAIN_VAL_LIST, 'split5', total_split=0.5)
split_list_file(TRAIN_VAL_LIST, 'split6', total_split=0.4)

#copy_check_files(VAL_LIST, TRAIN_DATA_DIR, TRAIN_DATA_DIR)
#copy_check_files(VAL_LIST, ALL_DATA_DIR, TRAIN_DATA_DIR, check=True)
#copy_check_files(TEST_LIST, ALL_DATA_DIR, TEST_DATA_DIR)
#copy_check_files(TEST_LIST,TEST_DATA_DIR, TEST_DATA_DIR)

#Total: 14681
#Total: 3222