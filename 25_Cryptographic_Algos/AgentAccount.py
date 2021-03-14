#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:12:41 2021

@author: amiriot
@contact: amirkhondokar@gmail.com
@file: AgentAccount.py
@purpose: to build a distributed network of communication over MQTT protocol
@methods:
    loadConfiguration()
"""
import json
import sys

class AgentAccount(object):
    
    def __init__(self, config_file="agent_config.json"):
        self.config = None
        self.config_file = None
        self.setConfigFile(config_file)
    
    def setConfigFile(self, new_config_file):
        self.config_file = new_config_file
        self.loadConfiguration()
        
    def getCofig(self):
        return self.config
    
    def loadConfiguration(self):
        try:
            with open(self.config_file,"r") as fp:
                self.config = json.load(fp)
        except FileNotFoundError:
            sys.stderr("provided configuration json file not found")
            sys.exit(1)
    
    def saveConfiguration(self):
        pass #TODO : json configuration file save 
    
    def __del__(self):
        pass #TODO free resources

                

if __name__=='__main__':
    pass