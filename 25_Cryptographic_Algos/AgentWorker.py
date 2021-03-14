#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:33:53 2021

@author: amiriot
@contact: amirkhondokar@gmail.com
@file: AgentWorker.py
@purpose: to build a distributed network of communication over MQTT protocol
@methods:
    processJobs()
    newJob(agentJob)
    getNextMessage()
    getTxBufferSize()
    setTxBufferSize(TxBufferSize)
    getRxBufferSize()
    setRxBufferSize(RxBufferSize)
    
"""
from threading import Thread
import multiprocessing
from AgentJob import AgentJob

class AgentWorker(object):
    
    def __init__(self):
        self.agent_account = None
        self.agent_job = None
        self.agent_job_queue = multiprocessing.Queue()
    
    def setAgentAccount(self, new_agent_account):
        self.agent_account = new_agent_account
        self.agent_job = AgentJob()
        self.agent_job.setAgentAccount(self.agent_account)
    
    def getAgentAccount(self):
        return self.agent_account
    
    def processJobs(self): #TODO process queued jobs symultaneously
        pass
    
    def newJob(self, new_job_for_agent):
        self.agent_job_queue.put(new_job_for_agent)
    
    def handShakeWith(self,address): #TODO handshake with other Agent
        pass
    
    def getNextMessage(self):
        pass
    
    def getTxBufferSize(self):
        self.agent_account.config["TX_BUFFER_SIZE"]
    
    def setTxBufferSize(self, new_tx_buffer_size):
        self.agent_account.config["TX_BUFFER_SIZE"] = new_tx_buffer_size
    
    def getRxBufferSize(self):
        self.agent_account.config["RX_BUFFER_SIZE"]
    
    def setRxBufferSize(self, new_rx_buffer_size):
        self.agent_account.config["RX_BUFFER_SIZE"] = new_rx_buffer_size
    
    def __del__(self):
        pass #TODO free resources

if __name__=='__main__':
    pass
