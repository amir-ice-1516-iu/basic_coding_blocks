#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:36:19 2021

@author: Khondokar amir hossain
@contact: amirkhondokar@gmail.com
@file: ListToIMAGE.py
@purpose: to convert 2D list into Image as Report
"""
from PIL import Image, ImageDraw, ImageFont
import PIL
import os
import copy
# import matplotlib


class ListToIMAGE(object):
    
    def __init__(self,imageFile="LTI.png", fontFilePath = "fonts"):
        self.imageFile = imageFile
        self.fontFilePath = fontFilePath
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
        self.PosYDefaultValue = 200
        self.PosX = 5
        self.PosY = self.PosYDefaultValue
        self.writingColumLables = False
        self.IMAGE = []
        self.minColumnLengths = []
        self.colStrings = None
        self.FONTS = ["FreeMono.ttf","Arialn.ttf","arial.ttf","ArialNarrow2.ttf","ArialNarrowBold.ttf","ArialNarrowBoldItalic.ttf",
                      "ArialNarrowFett.ttf","ArialNarrowFettKursiv.ttf","ArialNarrowFettKursiv2.ttf","ArialNarrowItalic.ttf",
                      "Arialnb.ttf","Arnar.ttf","Arnari.ttf"]
        self.FONT_INDEX = 0
        
        
    def generateImage(self,listData):
        self.selectedPage = 0
        # print(len(self.columLabels))
        self._setMaxValues(self.columLabels)
        # print("MaxValue col set")
        self._setMaxValues(listData)
        # print("MaxValue set")
        self._setupNumberOfPages(listData)
        # print("Number of pages set: ",self.numberOfPages)
        self._writeColumnLabels()
        # print("column label written")
        self._writeRows(listData)
        # print("data written")
        self._saveImages()
        # print("Images saved")
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
        if self.numberOfPages==0:
            self.numberOfPages = 1
        for newPage in range(self.numberOfPages):
            self.IMAGE.append(Image.new("RGB", (self.pageWidth,self.pageHeight), self.bgColor))
            self._IMD.append(ImageDraw.Draw(self.IMAGE[-1]))
        tempPath = os.path.join(self.fontFilePath,self.FONTS[self.FONT_INDEX])
        # tempPath = tempPath.replace("/","\\")
        print(tempPath)
        self.FONT = PIL.ImageFont.truetype(tempPath, self.fontSize)
    
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
        if type(self.colStrings)==type(None):
            self.colStrings = 0
            tempCols = 0
        else:
            tempCols = copy.deepcopy(self.colStrings)
            self.colStrings = 0
        for col in range(self.numberOfCollumns):
            if len(self.minColumnLengths) < self.numberOfCollumns:
                tempMinColLength = 0
            else:
                tempMinColLength = self.minColumnLengths[col]
            for row in range(self.numberOfRows):
                try:
                    if len(str(listData[row][col])) > tempMinColLength:
                        tempMinColLength = len(str(listData[row][col]))
                        print("tempMin "+str(tempMinColLength))
                except Exception:
                    pass
            if len(self.minColumnLengths)< self.numberOfCollumns:
                self.minColumnLengths.append(tempMinColLength)
            else:
                if self.minColumnLengths[col] < tempMinColLength:
                    self.minColumnLengths[col] = tempMinColLength
            self.colStrings += tempMinColLength
        if self.colStrings < tempCols:
            self.colStrings = copy.deepcopy(tempCols)
        self.pageWidth = int((self.colStrings*self.fontSize/1.26))
        self.pageHeight= int(self.pageWidth/1.4145161)
        
    def _writeColumnLabels(self):
        self.selectedPage = 0
        for i in range(self.numberOfPages):
            self.writingColumLables = True
            self.selectedPage = i
            self.PosY = self.PosYDefaultValue
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
            if len(row)!=len(self.minColumnLengths):
                print("Padding went wrong")
            else:
                print("Padding OK")
            for i, col in enumerate(row):
                if type(col) == type(None):
                    col = "-"
                if type(col) == type(int):
                    col = str(col)
                tempRow = tempRow + str(self._doPadding(col,self.minColumnLengths[i])) +"|"
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
                self.PosY = self.PosYDefaultValue+self.fontSize*3
                self.selectedPage += 1
                if self.selectedPage>=self.numberOfPages:
                    break
                
    def _doPadding(self,word, Length):
        if len(str(word))<=Length:
            Remaining = Length-len(str(word))
            Spaces = " "*(Remaining//2)
            if self.alignment=="LEFT":
                word = str(word)+Spaces+Spaces
            elif self.alignment=="CENTER":
                word = Spaces+str(word)+Spaces
            elif self.alignment=="RIGHT":
                word = Spaces+Spaces+str(word)
            if Remaining%2==1:
                word = word + " "
            return word
        else:
            return word
    
    def setImageFileName(self, imageFile):
        self.imageFile = imageFile
    def setColumColor(self,cColor):
        self.columColor=cColor
    def setColumLabels(self,Labels):
        self.columLabels = Labels
    def setBgColor(self,bgColor):
        self.bgColor = bgColor
    def setFontFilePath(self, newFontFilePath):
        self.fontFilePath = newFontFilePath
    def setFontSize(self,size):
        self.fontSize = size
    def setFontColor(self,color):
        self.fontColor = color
    def setAlignment(self,pos="LEFT"):
        self.alignment = pos
    def getImageFileName(self):
        return self.imageFile
    def getColumColor(self):
        return self.columColor
    def getAlignment(self):
        return self.alignment
    def getFontFilePath(self):
        return self.fontFilePath
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
    for i in range(65,79):
        Col.append(str(chr(i))*9)
        Pad.append("_"*9)
    Obj.setColumLabels([Pad,Col,Pad])
    #Obj.setAlignment("LEFT")
    Obj.setAlignment("CENTER")
    #Obj.setAlignment("RIGHT")
    
    for i in range(100):
        tempRow = []
        for j in range(13):
            if i*j%5!=0:
                tempRow.append(str(i*j))
            else:
                tempRow.append(None)
        L.append(tempRow)
    L.append(Pad)
    Obj.setFontSize(15)
    Obj.generateImage(L)
    

