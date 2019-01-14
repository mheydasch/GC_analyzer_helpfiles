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



path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_20/3_hours_timelapse_40x/adjusted/'
identifierpattern=re.compile('[a-z]{4,}\.tif$', flags=re.IGNORECASE) #identifyimg tif files with a channelname
os.chdir(path)

    
os.listdir(path)
onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]    



for i in onlyfiles: 
    try:
        identifier=re.search(identifierpattern, i).group()  #identifying relevant files
        break 
    except:
        next
fovpattern=re.compile('[0-9]{4}_' + identifier) #identifying each pattern
wellpattern=re.compile('_[A-Z][0-9]_')
datepattern=re.compile('[0-9]{4}_[0-9]{2}_[0-9]{2}')


#%%
welllist=[]
for i in onlyfiles: #recompiling names in the required order and saving them to new folder
      if identifier in i:
        print(i)
        identifier=re.search(identifierpattern, i).group() 
        fov = re.search(fovpattern, i).group().strip(identifier)
        date = re.search(datepattern, i).group().replace("_", "")
        well=re.search(wellpattern, i).group().strip('_') 
        file = os.path.join(path, i)
        newname=well+'_'+date+'_'+fov+identifier
        newlocation=os.path.join(path, newname)
        oldname=os.path.join(path, i)
        os.rename(oldname, newlocation)
        
                