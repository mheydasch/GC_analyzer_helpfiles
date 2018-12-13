#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:17:42 2018

@author: max
"""

'''
takes all segmentation representations burried deep in the folder of the GC output
and moves all of them to a single folder

'''
import os
import re
from shutil import copyfile
import argparse
path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_28/timelapse/analyzed/GC_ran/'



def parseArguments():
  # Define the parser and read arguments
  parser = argparse.ArgumentParser(description='collect segmentation files into one directory')
  parser.add_argument('-d', '--dir', type=str, help='The directory where the knockdown folders are', required=True)
  args = parser.parse_args()
  return(args)

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
    onlydirs=[os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    oldpath=[]
    newpath=[]
    tifind=re.compile('.png')
    newdir=path+'Collection'
    oldfiles=[]
    newfiles=[]
    for i in onlydirs:
        #dont look in collection folder
        if i != newdir:
            
            #look in each folder and create a list of the paths, if it is a folder
            i_dirs=[os.path.join(i, folder) for folder in os.listdir(i) if os.path.isdir(os.path.join(i, folder))]
            for item in i_dirs:
                #get the identifier from the folder
                pathlist=vars()['item'].split('/')
                identifier=pathlist[-2]+'_'+pathlist[-1]
                #get the folder inside
                i_path=item+'/Channels/GCAMainVisualization/filoLength/ForMainMovie_Feature_Movie/Channel1Detect_OverlaidOnChannel1/'
                
                try:
                    oldfiles=[os.path.join(i_path, f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                              if re.search(tifind, f) is not None ]
                    newfiles=[os.path.join(newdir, identifier+f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                              if re.search(tifind, f) is not None ]
                    
                except (NotADirectoryError, FileNotFoundError) as e :
                    print(i_path)
                    next
                [oldpath.append(f) for f in oldfiles]
                [newpath.append(f) for f in newfiles]
    #print(oldpath, newpath)
    return oldpath, newpath

def copy_file(path):
    '''
    oldpath: list of paths+filename in which folders are seperated by '/'
            4th element from the back must be identifier of the file
    newpath: list of paths+filename. file must contain identifier
    '''
    oldpath, newpath=get_move_paths(path)
    for i1, i2 in zip(oldpath, newpath):
            if vars()['i1'].split('/')[-7] in vars()['i2'].split('/')[-1]:
                copyfile(i1, i2)



if __name__ == '__main__':
    args=parseArguments()
    path=args.dir
    copy_file(path)
    print(args)



#onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]
#
 