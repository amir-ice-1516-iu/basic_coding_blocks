#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:25:58 2021

@author: amiriot
@contact: amirkhondokar@gmail.com
@file: MqttAgent.py
@purpose: to build a distributed network of communication over MQTT protocol
@methods:
    handShakeWith(address)
    
"""
import paho.mqtt
from AgentAccount import AgentAccount
from AgentWorker import AgentWorker
from AgentJob import AgentJob

class MqttAgent(object):
    
    def __init__(self, agent_account_config_file_name="agent_config.json"):
        self.agent_account = None
        self.agent_job = None
        self.agent_worker = None
        self.agent_config_file_name = agent_account_config_file_name
        
    
    def setAgentAccountConfigFileName(self, new_agent_account_config_file_name):
        self.agent_account = AgentAccount(new_agent_account_config_file_name)
        self.agent_config_file_name = new_agent_account_config_file_name
        self.agent_job = AgentJob()
        self.agent_job.setAgentAccount(self.agent_account)
        self.agent_worker = AgentWorker()
        self.agent_worker.setAgentAccount(self.agent_account)
        
    
    def getAgentAccount(self):
        return self.agent_account
    
    def __del__(self):
        pass #TODO free resources
    
if __name__=='__main__':
    Obj = MqttAgent()
    Obj.setAgentAccountConfigFileName("agent_config.json")


