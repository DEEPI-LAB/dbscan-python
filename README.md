# DBSCAN

## General description

Python implementation of 'DBSCAN' Algorithm using only Numpy and Matplotlib.

## Requirements

    pip3 install numpy scipy matplotlib
    
## Usage

### Initialize DBSCAN

You should install **numpy** and **matplotlib** for clustering and visualization. If you want to load sample data (sample.mat), you also need to install **scipy**. Although it is ironic that there is a dbscan function in the scipy... :) **I've reinvented the wheel**

    dbscan = dbscan(x, eplison, minPts)
    
### Run DBSCAN


    idx, noise = dbscan.run()

### Result Grouping

    cluster, noise = dbscan.sort()

### Visualize results

    dbscan.plot()

## Author

Jongwon Kim : [https://deep-eye.tistory.com/](https://deep-eye.tistory.com/)