# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:40:06 2019

@author: jkannenberg
"""

import time
import json
import random
import numpy
import datetime

class export_batch_events:
    """
    Describe class
    """

    def __init__(self, batch_size, interval, output_directory):
        
        self._batch_size = batch_size
        self._interval = interval
        self._output_directory = output_directory
        self._events = self.generate_batch_events()
        

    def generate_batch_events(self):
        
        list_out = []
        counter = 0
        
        while counter < self._batch_size: 

                order_id = random.randint(1,10*10)
               	
                list_out.append({'Type': 'OrderPlaced' , 
                                 'Data':{'OrderId': order_id,
                                         'TimestampUtc': str(datetime.datetime.now())
                                        }
                                 })
    
                list_out.append({'Type':numpy.random.choice(['OrderAccepted','OrderCancelled'], p=[0.8, 0.2]), 
                                 'Data':{'OrderId': order_id,
                                         'TimestampUtc': str(datetime.datetime.now())
                                        }
                                 })
    
                counter += 1
                time.sleep(self._interval)
                
        return list_out
    
    
    def export_json(self):
        
        output_filename = self._output_directory + 'orders' + str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S"))

        with open(output_filename, 'w') as outfile:
           for event in self._events:
               json.dump(event, outfile)
               outfile.write('\n')
           



