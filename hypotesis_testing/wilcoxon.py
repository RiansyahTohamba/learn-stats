import numpy as np
from scipy.stats import ttest_1samp, wilcoxon, ttest_ind, mannwhitneyu
import random
# kelas terdampak ditampilkan juga?,
# cari lagi kelas yg high-coupling,
cls_before = np.append(np.array([21,20,21,26,53,21,48]), np.random.randint(40, high=56, size=500)) 
cls_after = np.append(np.array([21,20,21,26,52,21,48]),np.random.randint(40, high=56, size=500))
np.random.seed(0)
# cls_before = np.random.randint(40, high=56, size=500)
# cls_after = np.random.randint(40, high=56, size=500)
z_statistic, p_value = wilcoxon(cls_after - cls_before)
print("cls before :", cls_before)
print("cls after :", cls_after)
print("p-value :", p_value)