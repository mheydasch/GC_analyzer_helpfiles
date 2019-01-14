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



path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_28/timelapse/'
identifierpattern=re.compile('.tif$', flags=re.IGNORECASE) #identifyimg tif files with a channelname
os.chdir(path)
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
    
os.listdir(path)
onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]    



# =============================================================================
# for i in onlyfiles: 
#     try:
#         identifier=re.search(identifierpattern, i).group()  #identifying relevant files
#         break 
#     except:
#         next
# =============================================================================
identifier='.TIF'
stackpattern=re.compile('_t[0-9]')        
fovpattern=re.compile('_[0-9]{1,}_') #identifying each pattern
wellpattern=re.compile('^.+?(?=_)')
channelpattern=re.compile('[^_]*$')
datepattern=re.compile('[0-9]{4}_[0-9]{2}_[0-9]{2}')
#%%
def rename_tif(file):
    fov = re.search(fovpattern, file).group().strip(identifier)
    stack= re.search(stackpattern, file).group().strip(identifier)
    channel = re.search(channelpattern, file.strip(stack+identifier)).group().strip(stack+identifier).replace('-','').replace('_', '')
    #channel=re.sub(r'(w[0-9])', r'\1_', channel) #for gca
    well= re.search(wellpattern, file).group().strip(identifier)

    date='_20181112'
    new=well+fov+channel+'.tif' #for GC
    #new=well+fov+channel+stack+'.tif' #for CP
    new=os.path.join(path, new)
    old=os.path.join(path, file)
    return old, new
for i in onlyfiles: 
     if identifier in i:
        try:
             oldname, newlocation=rename_tif(i)
             os.rename(oldname, newlocation)
        except AttributeError:
            next


# =============================================================================
# for i in onlyfiles: 
#     if identifier in i:
#         try:
#             oldname, newlocation=rename_tif(i)
#             os.rename(oldname, newlocation)
#         except:
#             ('Error')
#             next
# =============================================================================
#%%
# =============================================================================
# welllist=[]
# for i in onlyfiles: #recompiling names in the required order and saving them to new folder
#       if identifier in i:
#         print(i)
#         identifier=re.search(identifierpattern, i).group() 
#         fov = re.search(fovpattern, i).group().strip(identifier)
#         date = re.search(datepattern, i).group().replace("_", "")
#         well=re.search(wellpattern, i).group().strip('_') 
#         file = os.path.join(path, i)
#         newname=well+'_'+date+'_'+fov+identifier
#         newlocation=os.path.join(path, newname)
#         oldname=os.path.join(path, i)
#         os.rename(oldname, newlocation)
#         
# =============================================================================
                