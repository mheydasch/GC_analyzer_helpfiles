o#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:17:03 2018
Renames the files from the microscope into pattern: Well, Date, FoV, channel.
It replaces the well name by a random string of length 8 and creates a csv
file memorizing which string belongs to which well.
To be used before growth cone analyzer crops images to exclude personal bias
in picking the growth cones for each conditions.
@author: max
"""

import os
from os.path import isfile, join
import re
import sys
import string
import random
import pandas as pd

# =============================================================================
# path=sys.argv[1]
# try:
#     path=sys.argv[1]
#     print(path)
# except:
#     print('Please pass directory_name')
# =============================================================================
Experimentname= 'SiRNA_24'
path='/Users/max/Desktop/Office/Phd/Presentations/izb_meeting/test_GC/'
identifierpattern=re.compile('[a-z]{4,}', flags=re.IGNORECASE) #identifyimg tif files with a channelname
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
for i in onlyfiles:      
        identifier=re.search(identifierpattern, i).group()  #identifying relevant files
        
fovpattern=re.compile('[0-9]{4}_' + identifier) #identifying each pattern
wellpattern=re.compile('_[A-Z][0-9]_')
datepattern=re.compile('[0-9]{4}_[0-9]{2}_[0-9]{2}')


#%%
welllist=[]
identification=pd.DataFrame({'actual_name':["placeholder"], 'new_name':["placeholder"], 'blinded_well':["placeholder"]})
#iterator for location in dataframe
iterator=0
#recompiling names in the required order and saving them to new folder
for i in onlyfiles: 
      if identifier in i:
        print(i)
        identifier=re.search(identifierpattern, i).group() 
        fov = re.search(fovpattern, i).group().strip(identifier)
        date = re.search(datepattern, i).group().replace("_", "")
        well=re.search(wellpattern, i).group().strip('_') 
        file = os.path.join(path, i)
        actualname=well+'_'+date+'_'+fov+identifier
        #creates a 3 characters long random string of uppercase letters and digits and replaces the wellname with it
        blinded_well=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        blinded_count=identification['blinded_well'].str.contains(blinded_well).sum()
        while blinded_count>0:
            blinded_well=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            blinded_count=identification['blinded_well'].str.contains(blinded_well).sum()
        identification.loc[iterator,'blinded_well']= blinded_well
        newname=blinded_well+'_'+date+'_'+fov+identifier+'.tif'
        identification.loc[iterator,'actual_name']= actualname
        identification.loc[iterator,'new_name']=newname
        newlocation=os.path.join(path, newname) 
        oldname=os.path.join(path, i)
        print(newname)  
        os.rename(oldname, newlocation)
        iterator+=1 
identification.to_csv('{}{}identification.csv'.format(path, Experimentname))        
                