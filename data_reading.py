# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:48:52 2020

@author: Mircea Davidescu
"""
import os


data_path = os.path.expanduser('~')+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default"


files = os.listdir(data_path)
history_db = os.path.join(data_path, 'History')