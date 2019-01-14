#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:17:03 2018
Renames the files from the microscope into pattern: Well, Date, FoV, channel
@author: max
"""

import os
from os.path import isfile, join
import re
import sys


#%%
path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_28/Biosensor_package'
os.chdir(path)
os.listdir(path)
onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]    
#%%
def rename_tif(file):
    new=file.strip('TIF')
    new=new+'tif'
    new=os.path.join(path, new)
    old=os.path.join(path, file)
    return old, new

for i in onlyfiles: 
    if 'TIF' in i:
        try:
            oldname, newlocation=rename_tif(i)
            os.rename(oldname, newlocation)
        except:
            ('Error')
            next

        
                