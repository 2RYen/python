# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:30:26 2024

@author: mjmy0
"""

class TempratureConverter:
    def __init__(self, temperature): #생성자
        self.temperature = temperature
    def celsius2fagrenheit(self): #메소드
        return self.temperature * 9/5 + 32
    def farenheit2celsius(self): #메소드
        return (self.temperature - 32) * 5/9