'''
Date         : 2023-10-12 14:56:26
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-13 16:24:05
LastEditors  : BDFD
Description  : 
FilePath     : \execdata\eda\_data_mining.py
Copyright (c) 2023 by BDFD, All Rights Reserved. 
'''
import numpy as np
import pandas as pd


def high_miss_rate_column(df, missing_rate_column, corresponding_name_column, miss_rate=5):
    # combine use with function[exe.analysis_graph.missing_value_analysis]
    filtered_df = df[df[missing_rate_column] > miss_rate]
    delete_column_name_list = filtered_df[corresponding_name_column].tolist()
    return delete_column_name_list

def numerical_features_list(df):
    # list for numerical variables
    numerical_features_list = [feature for feature in df.columns if df[feature].dtypes != 'O']
    print('Number of Numerical Variables:', len(numerical_features_list))

    #visualize the numerical variables
    print(df[numerical_features_list].head())
    return numerical_features_list

def categorical_features_list(df):
    # list for categorical variables
    categorical_features_list = [feature for feature in df.columns if df[feature].dtypes == 'O']
    print('Number of Categorical Variables:', len(categorical_features_list))

    #visualize the categorical variables
    print(df[categorical_features_list].head())
    return categorical_features_list


def column_identify(df, column_lists):
    column_indentify = {}
    for col in column_lists:
        num = len(df[col].unique().tolist())
        column_indentify[col] = num
    return column_indentify


def filtered_value_count(df, column, limit_number=10):
    '''
    用于过滤当前column每个种类少于10个分类
    '''
    value_counts_series = df[column].value_counts()
    filtered_value_counts = value_counts_series[value_counts_series < limit_number]
    return filtered_value_counts


def filtered_value_list(df, column, limit_number=10):
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
