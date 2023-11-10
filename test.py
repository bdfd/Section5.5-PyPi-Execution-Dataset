'''
Date         : 2022-10-26 11:24:35
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-09 17:16:48
LastEditors  : BDFD
Description  : 
FilePath     : \test.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
import execdata as exe
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

data_path = "https://raw.githubusercontent.com/bdfd/Section6.Project03-House_Price_Prediction/main/1.0%20dataset/train.csv"
df = pd.read_csv(data_path, encoding='utf-8')
print(df.head())
column_list = exe.analysis_graph.missing_value_analysis(df)
print(column_list)
