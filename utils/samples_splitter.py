import csv
import os
import shutil
from pathlib import Path

ROOT_DIR = os.path.dirname(Path(__file__).parent)
DATA_DIR = os.path.join(ROOT_DIR, "data")
TRAIN_DATA_DIR = os.path.join(DATA_DIR, "train")
TEST_DATA_DIR = os.path.join(DATA_DIR, "test")
ALL_DATA_DIR = os.path.join(DATA_DIR, "all")

TRAIN_LIST = os.path.join(DATA_DIR, "train_listfile.csv")
TEST_LIST = os.path.join(DATA_DIR, "test_listfile.csv")
VAL_LIST = os.path.join(DATA_DIR, "val_listfile.csv")


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


#copy_check_files(VAL_LIST, TRAIN_DATA_DIR, TRAIN_DATA_DIR)
#copy_check_files(VAL_LIST, ALL_DATA_DIR, TRAIN_DATA_DIR, check=True)
#copy_check_files(TEST_LIST, ALL_DATA_DIR, TEST_DATA_DIR)
copy_check_files(TEST_LIST,TEST_DATA_DIR, TEST_DATA_DIR)

#Total: 14681
#Total: 3222