# -*- coding: utf-8 -*-
"""
Project Code: DBSCAN v1.0
@author: Deep.I Inc. @Jongwon Kim
Revision date: 2020-12-07
Contact Info: :
    https://deep-eye.tistory.com
    https://deep-i.net
"""

import numpy as np
from matplotlib import pyplot as plt

class DBSCAN(object):

    def __init__(self,x,epsilon,minpts): 
        # The number of input dataset
        self.n = len(x)
        # Euclidean distance
        p, q = np.meshgrid(np.arange(self.n), np.arange(self.n))
        self.dist = np.sqrt(np.sum(((x[p] - x[q])**2),2))
        # label as visited points and noise
        self.visited = np.full((self.n), False)
        self.noise = np.full((self.n),False)
        # DBSCAN Parameters
        self.epsilon = epsilon
        self.minpts = minpts 
        # Cluseter
        self.idx = np.full((self.n),0)
        self.C = 0
        self.input = x
        
    def run(self):
        # Clustering
        for i in range(len(self.input)):
            if self.visited[i] == False:
                self.visited[i] = True
                self.neighbors = self.regionQuery(i)
                if len(self.neighbors) >= self.minpts:    
                    self.C += 1    
                    self.expandCluster(i)    
                else : self.noise[i] = True 
        return self.idx,self.noise
                            
    def regionQuery(self, i):
        g = self.dist[i,:] < self.epsilon
        Neighbors = np.where(g)[0].tolist()
        return Neighbors     
    
    def expandCluster(self, i):
        self.idx[i] = self.C
        k = 0
       
        while True:
            try:
                j = self.neighbors[k]
            except: return
            if self.visited[j] != True:
                self.visited[j] = True
                
                self.neighbors2 = self.regionQuery(j)
                v = [self.neighbors2[i] for i in np.where(self.idx[self.neighbors2]==0)[0]]
               
                if len(self.neighbors2) >=  self.minpts:
                    self.neighbors = self.neighbors+v 
                    
            if self.idx[j] == 0 : self.idx[j] = self.C 
            
            k += 1
            if len(self.neighbors) < k-1:
                return
            
    def sort(self):
        
        cnum = np.max(self.idx)
        self.cluster = []
        self.noise = []
        for i in range(cnum):
           
            k = np.where(self.idx == (i+1))[0].tolist()
            self.cluster.append([self.input[k,:]])
       
        self.noise = self.input[np.where(self.idx == 0)[0].tolist(),:]
        return self.cluster, self.noise
              
    def plot(self):
        
        self.sort()
        fig, ax = plt.subplots()
        
        for idx,group in enumerate(self.cluster):
        
            ax.plot(group[0][:,0], 
                    group[0][:,1], 
                    marker='o', 
                    linestyle='',
                    label=idx) 
        ax.plot(self.noise[:,0], 
                self.noise[:,1], 
                marker='x', 
                linestyle='',
                label='noise')        

        ax.legend(fontsize=10, loc='upper left')
        plt.title('Scatter Plot of Clustering result', fontsize=15)
        plt.xlabel('X', fontsize=14)
        plt.ylabel('Y', fontsize=14)
        plt.show()


