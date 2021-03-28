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
    setConfigFile(new_config_file)
    getConfigFile()
    saveConfiguration()

@Design Rules:
    1. Class names & Exception names are allways in Camel case starting with upper case letter
    2. Method names allways in Camel case starting with lower case letter
    3. Variable names allways in lowercase with underscore seperated if required
"""
import json
import sys
import rsa

class AgentAccount(object):
    
    def __init__(self, config_file="agent_account_config.json"):
        self.config = None
        self.config_file = None
        self.setConfigFile(config_file)
    
    def generateAgentKey(self):
        _, self.config["AGENT_RSA_KEY"] =  rsa.newkeys(self.config["RSA_KEY_SIZE"])
        _, self.config["HOST_RSA_KEY"] = rsa.newkeys(self.config["RSA_KEY_SIZE"])
    
    def storeHostKey(self,key):
        self.config["HOST_RSA_KEY"].n = key["n"]
        self.config["HOST_RSA_KEY"].e = key["e"]
        
    def setConfigFile(self, new_config_file):
        self.config_file = new_config_file
        self._loadConfiguration()
    
    def _loadConfiguration(self):
        try:
            with open(self.config_file,"r") as fp:
                self.config = json.load(fp)
            self.generateAgentKey()
        except FileNotFoundError:
            sys.stderr("provided configuration json file not found")
            sys.exit(1)
    
    def saveConfiguration(self):
        try:
            with open(self.config_file,"w") as fp:
                json.dump(self.config,fp,indent=4) #TODO : json configuration file save
        except Exception as SaveError:
            sys.stderr("Unable to save")
            sys.stderr(SaveError)
            sys.exit(2)
    
    def __del__(self):
        pass #TODO free resources

                

if __name__=='__main__':
    agent_account = AgentAccount("agent_account_config.json")
    agent_account.config["VERSION"] = "0.0.1" # dummy test
    agent_account.saveConfiguration()
    pass