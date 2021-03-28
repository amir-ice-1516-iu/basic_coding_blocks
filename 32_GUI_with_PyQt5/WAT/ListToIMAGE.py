#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:36:19 2021

@author: Khondokar amir hossain
@contact: amirkhondokar@gmail.com
@file: ListToIMAGE.py
@purpose: to co
"""
from PIL import Image, ImageDraw, ImageFont


class ListToIMAGE(object):
    
    def __init__(self,imageFile="LTI.png"):
        self.imageFile = imageFile
        self.fontSize = 20
        self.fontColor = (0,0,0)
        self.bgColor = (255,255,255)
        self.columColor = (167,6,208)
        self.maxCollumLength = 0
        self.numberOfCollumns = 1
        self.numberOfRows = 1
        self.numberOfPages = 1
        self.numberOfLinesPerPage = 40
        self.selectedPage = 0
        self.columLabels = []
        self.alignment = "LEFT"
        self.PosX = 5
        self.PosY = 0
        self.writingColumLables = False
        self.IMAGE = []
        
        
    def generateImage(self,listData):
        self.selectedPage = 0
        self._setMaxValues(self.columLabels)
        #print("MaxValue col set")
        self._setMaxValues(listData)
        #print("MaxValue set")        
        self._setupNumberOfPages(listData)
        #print("Number of pages set: ",self.numberOfPages)
        self._writeColumnLabels()
        #print("column label written")
        self._writeRows(listData)
        #print("data written")
        self._saveImages()
        #print("Images saved")
        #self._showImages()
        #print("Images Shown")
        
        
    def _showImages(self):
        for page in range(self.numberOfPages):
            self.IMAGE[page].show()
            
    def _saveImages(self):
        for page in range(self.numberOfPages):
            self.IMAGE[page].save(self.imageFile[:-4]+str(page)+self.imageFile[-4:])
    
    def _setupNumberOfPages(self,listData):
        self.numberOfPages = int(self.numberOfRows/self.numberOfLinesPerPage)
        self.numberOfPages = int(((self.numberOfRows+(self.numberOfPages*3))/self.numberOfLinesPerPage)+0.5)
        self.pageLoopingIndex = self.numberOfLinesPerPage
        
        self.IMAGE = []
        self._IMD = []
        for newPage in range(self.numberOfPages):
            self.IMAGE.append(Image.new("RGB", (self.pageWidth,self.pageHeight), self.bgColor))
            self._IMD.append(ImageDraw.Draw(self.IMAGE[-1]))
        self.FONT = ImageFont.truetype("Pillo/Tests/fonts/FreeMono.ttf",self.fontSize)
    
    def _setMaxValues(self,listData):
        if type(listData)!=type(list()):
            raise TypeError("parameter should be list type")
        else:
            self.numberOfRows = len(listData)
        self.maxCollumLength = 0
        self.numberOfRows = len(listData)
        for item in listData:
            if type(item)==type(list()):
                if len(item) > self.numberOfCollumns:
                    self.numberOfCollumns = len(item)
                for value in item:
                    if type(value)==type(str()):
                        if len(value) > self.maxCollumLength:
                            self.maxCollumLength = len(value)
                    else:
                        if len(str(value)) > self.maxCollumLength:
                            self.maxCollumLength = len(str(value))
            else:
                self.numberOfCollumns = len(listData)
                if type(item)==type(str()):
                    if len(item) > self.maxCollumnLength:
                        self.maxCollumLength = len(item)
                else:
                    if len(str(item)) > self.maxCollumLength:
                         self.maxCollumLength = len(str(item))
        self.pageWidth = int((self.maxCollumLength+0.35)*self.numberOfCollumns*self.fontSize*0.716)
        self.pageHeight= int(self.pageWidth*1.4145161)
        
    def _writeColumnLabels(self):
        self.selectedPage = 0
        for i in range(self.numberOfPages):
            self.writingColumLables = True
            self.selectedPage = i
            self.PosY = 0
            self._writeRows(self.columLabels)
            self.writingColumLables = False
        self.selectedPage = 0 
    
    def _writeRows(self,rows):
        tempRowWritten = 0
        for row in rows:
            tempRow = "|"
            if len(row)<self.numberOfCollumns:
                for i in range(len(row),self.numberOfCollumns):
                    row.append("-")
            for col in row:
                if col==None:
                    col = "-"
                tempRow = tempRow + self._doPadding(col) +"|"
            if self.writingColumLables:
                self._IMD[self.selectedPage].multiline_text((self.PosX,self.PosY), tempRow, font=self.FONT, fill=self.columColor)
            else:
                #print("Selected Page: ",self.selectedPage)
                #print("PosY: ",self.PosY)
                self._IMD[self.selectedPage].multiline_text((self.PosX,self.PosY), tempRow, font=self.FONT, fill=self.fontColor)
            self.PosY += self.fontSize
            if self.writingColumLables:
                continue
            else:
                tempRowWritten +=1
            if tempRowWritten>=self.pageLoopingIndex:
                tempRowWritten = 0
                self.PosY = self.fontSize*3
                self.selectedPage += 1
                if self.selectedPage>=self.numberOfPages:
                    break
                
    def _doPadding(self,word):
        if len(str(word))<self.maxCollumLength:
            word = str(word)+(" "*(self.maxCollumLength-len(str(word))))
            return word
        else:
            return word
    
    def setColumColor(self,cColor):
        self.columColor=cColor
    def setColumLabels(self,Labels):
        self.columLabels = Labels
    def setBgColor(self,bgColor):
        self.bgColor = bgColor
    def setFontSize(self,size):
        self.fontSize = size
    def setFontColor(self,color):
        self.fontColor = color
    def setAlignment(self,pos="LEFT"):
        self.alignment = pos
    def getColumColor(self):
        return self.columColor
    def getAlignment(self):
        return self.alignment
    def getFontColor(self):
        return self.fontColor
    def getFontSize(self):
        return self.fontSize
    def getBgColor(self):
        return self.bgColor
    def getColumLabels(self):
        return self.columLabels

if __name__=='__main__':
    Obj = ListToIMAGE()
    L = []
    Col = []
    Pad = []
    for i in range(65,80):
        Col.append(str(chr(i))*4)
        Pad.append("_"*4)
    Obj.setColumLabels([Pad,Col,Pad])
    for i in range(150):
        tempRow = []
        for j in range(12):
            if i*j%5!=0:
                tempRow.append(str(i*j))
            else:
                tempRow.append(None)
        L.append(tempRow)
    L.append(Pad)
    Obj.setFontSize(15)
    Obj.generateImage(L)
    

