#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:17:42 2018

@author: max
"""

'''
your file output is terrible!

'''
import os
import re
from shutil import copyfile
path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_28/Biosensor_package/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
#%%
#for filepath in glob.glob(path + '*{}'.format(identifier))
def get_move_paths(path):
    createFolder(path+'/Collection')
    onlydirs=[os.path.join(path, f) for f in os.listdir(path) if os.path.isdir]
    oldpath=[]
    newpath=[]
    tifind=re.compile('.tif')
    newdir=path+'Collection'
    for i in onlydirs:
        if i != newdir:
            pathlist=vars()['i'].split('/')
            identifier=pathlist[-1]
            i_path=i+'/BiosensorsPackage/ratio_tiffs/'
            
            try:
                oldfiles=[os.path.join(i_path, f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                          if re.search(tifind, f) is not None ]
                newfiles=[os.path.join(newdir, identifier+f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                          if re.search(tifind, f) is not None ]
               
            except NotADirectoryError :
                next
            [oldpath.append(f) for f in oldfiles]
            [newpath.append(f) for f in newfiles]
    return oldpath, newpath
def copy_file(oldpath, newpath):
    '''
    oldpath: list of paths+filename in which folders are seperated by '/'
            4th element from the back must be identifier of the file
    newpath: list of paths+filename. file must contain identifier
    '''
    for i1, i2 in zip(oldpath, newpath):
            if vars()['i1'].split('/')[-4] in vars()['i2'].split('/')[-1]:
                copyfile(i1, i2)

oldpath, newpath= get_move_paths(path)
copy_file(oldpath, newpath)




#onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]
#
 