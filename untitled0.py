#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:39:26 2018

@author: max
"""
import os
def walkfs(startdir, findfile):
    output=[]
    for root, dirs, files in os.walk(startdir):
        if findfile in files:
            output.append(root)
            return root
