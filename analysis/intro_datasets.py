'''
Author: Em
Date: 10-11-22
Purpose: To provide some insight into the data that we currently have and start to visualize it
'''
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#need to import the files
f = open("./data/jun17_nov21_nft_sales.csv",'r')
nft = pd.read_csv(f)
nft.head()
