import os

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-whitegrid')

ROOT_DIR = os.path.dirname(Path(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

TEST_RES = os.path.join(DATA_DIR, "test_results.csv")
TEST_RESBOOT = os.path.join(DATA_DIR, "test_resultsboot.csv")
TEST_RES_BENCH = os.path.join(DATA_DIR, "test_results_bench.csv")
VAL_HISTORY = os.path.join(DATA_DIR, "splitc_history.csv")

test_res_pd = pd.read_csv(TEST_RES)
test_resboot_pd = pd.read_csv(TEST_RESBOOT)
test_res_bench_pd = pd.read_csv(TEST_RES_BENCH)
val_history_pd = pd.read_csv(VAL_HISTORY)


def show_grap(c):
    ds1 = c['data_sets'][0]
    x1 = ds1[c['xf']].to_numpy()
    y1 = ds1[c['yfs'][0]].to_numpy()
    plt.plot(x1, y1, '-o', label=c['line_lbl'][0], color='green')

    if len(c['yfs']) > 1:
        ds2 = c['data_sets'][1]
        x2 = ds2[c['xf']].to_numpy()
        y2 = ds2[c['yfs'][1]].to_numpy()
        plt.plot(x2, y2, ':o', label=c['line_lbl'][1], color='orange')

    if len(c['yfs']) > 2:
        ds3 = c['data_sets'][2]
        x3 = ds3[c['xf']].to_numpy()
        y3 = ds3[c['yfs'][2]].to_numpy()
        plt.plot(x3, y3, '-o', label=c['line_lbl'][2], color='#0343DF')

    plt.xlabel(c['x_lbl'])
    plt.ylabel(c['y_lbl'])
    plt.title("{} Vs. {}".format(c['x_lbl'], c['y_lbl']))
    plt.legend(loc='lower right')
    plt.show()


auprc_plot = {
    "xf": "train_samples",
    "yfs": ["auprc_m", "auprc", "auprc"],
    "line_lbl": ["ConCare Bootstrapped AUPRC", "Benchmark Test AUPRC", "ConCare Test AUPRC"],
    "x_lbl": "Training samples",
    "y_lbl": "AUPRC",
    "data_sets": [test_resboot_pd, test_res_bench_pd, test_res_pd]
}

auroc_plot = {
    "xf": "train_samples",
    "yfs": ["auroc_m", "auroc", "auroc"],
    "line_lbl": ["ConCare Bootstrapped AUROC", "Benchmark Test AUROC", "ConCare Test AUROC"],
    "x_lbl": "Training samples",
    "y_lbl": "AUROC",
    "data_sets": [test_resboot_pd, test_res_bench_pd, test_res_pd]
}

minpse_plot = {
    "xf": "train_samples",
    "yfs": ["minpse_m", "minpse", "minpse"],
    "line_lbl": ["ConCare Bootstrapped min(Se, P+)", "Benchmark Test min(Se, P+)", "ConCare Test min(Se, P+)"],
    "x_lbl": "Training samples",
    "y_lbl": "min(Se, P+)",
    "data_sets": [test_resboot_pd, test_res_bench_pd, test_res_pd]
}

acc_plot = {
    "xf": "train_samples",
    "yfs": ["acc", "acc"],
    "line_lbl": ["Test Accuracy", "Benchmark Test Accuracy"],
    "x_lbl": "Training samples",
    "y_lbl": "Accuracy",
    "data_sets": [test_res_pd, test_res_bench_pd]
}

prec1_plot = {
    "xf": "train_samples",
    "yfs": ["prec1", "prec1"],
    "line_lbl": ["ConCare Precision on class 1", "Benchmark Precision on class 1"],
    "x_lbl": "Training samples",
    "y_lbl": "Precision on class 1",
    "data_sets": [test_res_pd, test_res_bench_pd]
}

val_plot1 = {
    "xf": "epoch",
    "yfs": ["auprc"],
    "line_lbl": ["Validation AUPRC"],
    "x_lbl": "Epochs",
    "y_lbl": "Validation AUPRC",
    "data_sets": [val_history_pd]
}

val_plot2 = {
    "xf": "epoch",
    "yfs": ["prec1"],
    "line_lbl": ["Class 1 Precision"],
    "x_lbl": "Epochs",
    "y_lbl": "Class 1 Precision",
    "data_sets": [val_history_pd]
}

#show_grap(auprc_plot)
#show_grap(auroc_plot)
#show_grap(acc_plot)
#show_grap(minpse_plot)
#show_grap(prec1_plot)
show_grap(val_plot1)