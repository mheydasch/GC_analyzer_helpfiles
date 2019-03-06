#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:30:32 2019

@author: max
"""

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


path='/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_36/'
faulty_name='Dock9'
correct_name='DOCK9'
identifierpattern=re.compile(faulty_name, flags=re.IGNORECASE) #identifyimg tif files with a channelname
os.chdir(path)

    
os.listdir(path)
onlyfiles=[f for f in os.listdir(path) if isfile(join(path, f))]    

#%%
for i in onlyfiles: #recompiling names in the required order and saving them to new folder
      if faulty_name in i:
        print(i)
        identifier=re.search(identifierpattern, i).group()   
        newname=i.replace(identifier, 'DOCK9')
        newlocation=os.path.join(path, newname)
        oldname=os.path.join(path, i)
        os.rename(oldname, newlocation)
        
                