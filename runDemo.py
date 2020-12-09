# -*- coding: utf-8 -*-
"""
Project Code: DBSCAN v1.1
@author: Deep.I Inc. @Jongwon Kim
Revision date: 2020-12-09
Contact Info: :
    https://deep-eye.tistory.com
    https://deep-i.net
"""

from dbscan import DBSCAN
from scipy import io

#%% Run DEMO
x = io.loadmat('./sample/sample.mat')['X']
# INIT DBSCAN
dbscan = DBSCAN(x,1.5,4)
# CLUSTERING
idx, noise = dbscan.run()
# SORTING
g_cluster, n_cluster = dbscan.sort()
# Visualization
dbscan.plot()