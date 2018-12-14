#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:17:42 2018

@author: max
"""

'''
takes all segmentation representations burried deep in the folder of the GC output
and copies all of them to a single folder
moves all directories for which no segmentation could be found to a 'Not_segmented'
directory
with the -e option it accepts a text file as second input and moves all folders 
annotated in that file to a segmentation error directory.

'''
import os
import re
from shutil import copyfile
from shutil import move

import argparse
path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_28/timelapse/analyzed/GC_ran/'



def parseArguments():
  # Define the parser and read arguments
  parser = argparse.ArgumentParser(description='collect segmentation files into one directory')
  parser.add_argument('-d', '--dir', type=str, help='The directory where the knockdown folders are', required=True)
  parser.add_argument('-e', '--errors', type=str, help='The file from which to read segmentation errors', required=False)
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
    KD_pattern=re.compile('[A-Za-z0-9]+')
    #FOV_pattern=re.compile('[0-9]+')
    for i in onlydirs:
        #dont look in collection folder
        if i != newdir and 'Flatfield' not in i and 'Not_segmented' not in i and 'HierarchicalCluster' not in i and 'segmentation_errors' not in i:
            foldername = vars()['i'].split('/')[-1]
            matched_foldername=re.match(KD_pattern, foldername)
            if matched_foldername is not None:                           
                #look in each folder and create a list of the paths, if it is a folder
                i_dirs=[os.path.join(i, folder) for folder in os.listdir(i) if os.path.isdir(os.path.join(i, folder))]
                for item in i_dirs:
                    #get the identifier from the folder
                    pathlist=vars()['item'].split('/')
                    identifier=pathlist[-2]+'_'+pathlist[-1]
                    i_path=item+'/GrowthConeAnalyzer/GCAMainVisualization/filoLength/ForMainMovie_Feature_Movie/Channel1Detect_OverlaidOnChannel1__/'
                    print(i_path)
                    #get the folder inside                                      
                    try:
                        oldfiles=[os.path.join(i_path, f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                                  if re.search(tifind, f) is not None ]
                        newfiles=[os.path.join(newdir, identifier+'_'+f) for f in os.listdir(i_path) if os.path.isfile(os.path.join(i_path, f))\
                                  if re.search(tifind, f) is not None ]
                        print('copying png files to', path + 'Collection')
                        
                    except (NotADirectoryError, FileNotFoundError) as e :
                        print('Error in', i_path, '\n', 'no segmentation found')
                        
                        dump=os.path.join(path+'Not_segmented/')
                        createFolder(dump)
                        final_dump=os.path.join(dump+foldername+'/')
                        print(item, 'moved to', final_dump, '\n')
                        createFolder(final_dump)
                        move(item, final_dump)            
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

def read_text(errors):
    '''
    reads in a textfile with the names of folders that have segmentation errors.
    '''
    file= open(errors, 'r')
    #creates a list of lines from the file
    lines=file.readlines()
    for n, i in enumerate(lines):        
        lines[n]=i.replace('\n', '')    
    return lines

def move_errors(errors):
    lines=read_text(errors)
    if len(lines)>0:
        seg_dump=os.path.join(path, 'segmentation_errors')
        createFolder(seg_dump)
        for i in lines:
            try:
                item=os.path.join(path, i)
                kd = vars()['i'].split('/')[-2]        
                kd_dump=os.path.join(seg_dump, kd)
                createFolder(kd_dump)            
                move(item, kd_dump)
                print(item, 'was moved to', kd_dump, '\n')
            except Exception as e:
                print(e)

#%%%
if __name__ == '__main__':
    args=parseArguments()
    path=args.dir
    errors=args.errors
    if errors is None:
        copy_file(path)
    else:
        move_errors(errors)
    print(args)



#onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]
#
 