# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:57:10 2019

@author: jkannenberg
"""

import pytest
from export_batch_events import export_batch_events

list_of_dict = export_batch_events(batch_size=4, interval=1, output_directory='C:/Users/jkannenberg/Desktop').generate_batch_events()

#Test-Ideen: 
# Zwei konsektuvie Order_ids sind identsich
