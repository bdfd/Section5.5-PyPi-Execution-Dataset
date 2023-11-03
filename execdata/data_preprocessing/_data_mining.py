'''
Date         : 2023-10-12 14:56:26
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-30 14:34:14
LastEditors  : BDFD
Description  : 
FilePath     : \execdata\data_mining.py
Copyright (c) 2023 by BDFD, All Rights Reserved. 
'''
import numpy as np
import pandas as pd


def column_identify(df, column_lists):
    column_indentify = {}
    for col in column_lists:
        num = len(df[col].unique().tolist())
        column_indentify[col] = num
    return column_indentify


def filtered_value_count(df, column, limit_number):
    value_counts_series = df[column].value_counts()
    filtered_value_counts = value_counts_series[value_counts_series < limit_number]
    return filtered_value_counts


def filtered_value_list(df, column, limit_number):
    value_counts_series = df[column].value_counts()
    filtered_value_counts = value_counts_series[value_counts_series < limit_number]
    filtered_value_counts_list = filtered_value_counts.index.values.tolist()
    return filtered_value_counts_list


def majority_target_variable(df, target_feature, majornity_target_value):
    majornity_target_value_count = df.loc[df[target_feature] == majornity_target_value].count()[
        0]
    number_of_value = len(df[target_feature].unique())
    data_length = len(df[target_feature])
    target_value_percentage = (majornity_target_value_count/data_length)
    upper_limit = round(data_length/number_of_value*1.3)
    lower_limit = round(data_length/number_of_value*0.7)
    # print(lower_limit, upper_limit)
    print('The Dataframe Value Count is:', data_length,
          ', and includes', number_of_value, 'values')
    print('The Majornity Target Value Count is:', majornity_target_value_count)
    # print('The Majornity Target Value Percentage is:', target_value_percentage)
    print(
        f"Majornity Target Value Percentage: {np.round(target_value_percentage*100,2)}%")
    if lower_limit <= target_value_percentage <= upper_limit:
        print("This is a balance dataset.")
    else:
        print("This is a imbalance dataset.")
    return target_value_percentage