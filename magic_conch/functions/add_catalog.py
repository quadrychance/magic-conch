import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import random
import pylab
import seaborn as sns
#import dask
from tqdm import tqdm
nova_EB = pd.read_csv('~/binary_planet_host_project/data/QVFlk0YH')
EB_KIC = pd.DataFrame(nova_EB[['KIC','period']])

def addEBCatalog(data):
    data['EB?'] = False
    data['period'] = 0
    data['AO'] = False
    u = 0
    for i in tqdm(EB_KIC['KIC']):
        morph = EB_KIC['period'].iloc[u]
        u+=1
        for k in range(0,len(data)):
            if i == data['kepid'].iloc[k]:
                data['EB?'].iloc[k]=True
                data['period'].iloc[k]=morph
    return data

def addAOCatalog(data):
    data['AO'] = False
    for i in tqdm(AO_table['kepid']):
        for k in range(0,len(data)):
            if i == data['kepid'].iloc[k]:
                data['AO'].iloc[k]=True

    return data
