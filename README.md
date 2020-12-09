# DBSCAN
## General description
Python implementation of 'DBSCAN' Algorithm using only Numpy and Matplotlib.
## Requirements
You should install **numpy** and **matplotlib** for clustering and visualization. If you want to load sample data (sample.mat), you also need to install **scipy**. Although it is ironic that there is a dbscan function in the scipy... :) **I've reinvented the wheel**

    pip3 install numpy scipy matplotlib
## Usage
### Initialize DBSCAN
    dbscan = dbscan(x, eplison, minPts)
### Run DBSCAN
    idx, noise = dbscan.run()
### Result Sorting
    cluster, noise = dbscan.sort()
### Visualize results
    dbscan.plot()
## Test DBSCAN
Open the **runDemo file**. You can just click **F5** in an **IDE environment** to see the sample data results.
1. sample data load

	   x = io.loadmat('./sample/sample.mat')['X']
2. Init  parameters

       dbscan = DBSCAN(x,1.5,4)

3. Run DBSCAN

       idx,noise = dbscan.run()

4. Sorting

       g_cluster,n_cluster = dbscan.sort()

5. Visualization

       dbscan.plot()
![results](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbK7xFY%2FbtqPql2AOLg%2Fd5xENNFkVXjW0UQVVvzVb0%2Fimg.png)
## Author
Jongwon Kim : [https://deep-eye.tistory.com/](https://deep-eye.tistory.com/)