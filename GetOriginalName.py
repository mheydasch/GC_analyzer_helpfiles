#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:07:09 2018

@author: max
To be used after Growth Cone analyzer has cropped the blinded videos
to get back the original well names.


"""
import pandas as pd
import re
import os
import shutil



file_path='/Users/max/Desktop/Office/Phd/Presentations/izb_meeting/test_GC/SiRNA_24identification.csv'
data=pd.read_csv(file_path)
path=file_path.strip('SiRNA_24identification.csv')

wellpattern=re.compile('^[A-Z][0-9]_')

for index, row in data.iterrows(): 
    #gets the well name of the current row     
    well=re.search(wellpattern, data.loc[index,'actual_name']).group().strip('_')
    try:
        #creates directory based on well name
        os.mkdir(path+well)
    except FileExistsError:
        pass
    #gets the directory corresponding to the well
    try:
        dir_list=os.listdir(path+data.loc[index, 'blinded_well'])
        dir_list=[x for x in dir_list if dir_list if x !='.DS_Store']
        move_dir=path+data.loc[index, 'blinded_well']
        #directory to move to (welldirectory)
        dest_dir=path+well +'/'
        for sub_dir in dir_list:
            try:
                shutil.move(move_dir+'/'+sub_dir, dest_dir)
           #if directory already exists this will take the subdirectories and pass them into that directory
            except: 
                nested_dir=os.listdir(move_dir+'/'+sub_dir)
                nested_dir=[x for x in nested_dir if nested_dir if x !='.DS_Store']
                for folder in nested_dir:
                    shutil.move(move_dir+'/'+sub_dir+'/'+folder, dest_dir+sub_dir)
    except FileNotFoundError:
            pass
#removes the blinded folders
for folder in data['blinded_well']:
    if os.path.isdir(path+folder):
        shutil.rmtree(path+folder)   
     