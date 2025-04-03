# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:13:59 2024

@author: mjmy0
"""
class Car:
    def __init__(self, model, color): #생성자
        self.model = model
        self.color = color
        
    def displayCar(self):
        print(self.model)
        print(self.color)