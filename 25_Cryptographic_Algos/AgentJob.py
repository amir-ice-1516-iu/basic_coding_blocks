#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:46:15 2021

@author: amiriot
@contact: amirkhondokar@gmail.com
@file: AgentJob.py
@purpose: to build a distributed network of communication over MQTT protocol
@methods:
    
@Design Rules:
    1. Class names & Exception names are allways in Camel case starting with upper case letter
    2. Method names allways in Camel case starting with lower case letter
    3. Variable names allways in lowercase with underscore seperated if required
"""
import rsa
import sys

class AgentJob(object):
    
    def __init__(self):
        self.agent_account = None
        self.done = False
        #self.agent_public_key = None
        #self.agent_private_key= None
        #self.host_public_key = None
        #self.host_private_key= None
        
    def encryptMessage(self, message):
        if self.agent_account.config["HAND_SHAKED"]:
            try:
                encrypted = rsa.encrypt(message.encode('utf-16'), self.host_public_key)
                return encrypted
            except Exception as eEncryptMessage:
                sys.stderr(eEncryptMessage)
        else:
            sys.stderr("Key not handshaked . trying to handshake")
            if self.handShakeWith(self.agent_account.config["HOST_ADDRESS"]):
                pass
            else:
                sys.stderr("handshake failed ")
    
    def decryptMessage(self, message):
        if self.agent_account.config["HAND_SHAKED"]:
            try:
                decrypted = rsa.decrypt(message, self.agent_private_key).decode('utf-16')
                return decrypted
            except Exception as eEncryptMessage:
                sys.stderr(eEncryptMessage)
        else:
            sys.stderr("Key not handshaked . trying to handshake")
            if self.handShakeWith(self.agent_account.config["HOST_ADDRESS"]):
                pass
            else:
                sys.stderr("handshake failed ")

    def handShakeWith(self, address): #TODO handshake with other Agent
        pass            
        
    def setAgentAccount(self, new_agent_account):
        self.agent_account = new_agent_account
        self.agent_public_key = rsa.key.PublicKey(self.agent_account.config["AGENT_RSA_KEY"].n, self.agent_account.config["AGENT_RSA_KEY"].e)
        self.agent_private_key= rsa.key.PrivateKey(self.agent_account.config["AGENT_RSA_KEY"])
        self.host_public_key = rsa.key.PublicKey(self.agent_account.config["HOST_RSA_KEY"].n, self.agent_account.config["HOST_RSA_KEY"].e)
        
    def getAgentAccount(self):
        return self.agent_account
    
    def __del__(self):
        pass


if __name__=='__main__':
    pass