#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:46:15 2021

@author: amiriot
@contact: amirkhondokar@gmail.com
@file: AgentJob.py
@purpose: to build a distributed network of communication over MQTT protocol
@methods:
    
"""
import rsa

class AgentJob(object):
    
    def __init__(self):
        self.agent_account = None
        
    def setAgentAccount(self, new_agent_account):
        self.agent_account = new_agent_account
        
    def getAgentAccount(self):
        return self.agent_account
    
    def __del__(self):
        pass


if __name__=='__main__':
    pass