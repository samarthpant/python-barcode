# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:18:37 2020

@author: Samarth Pant
"""

import barcode
#a=input("Enter your choice of barcode from EAN-8,EAN-13,EAN-14,UPC-A,JAN,ISBN-10,ISBN-13,ISSN,Code 39,Code 128,PZN")
hr=barcode.get_barcode_class('ean13')
#b=input("Enter the input for type of barcode you chose")
Hr=hr('1234567891235')
#c=input("enter the name by which you want to save the barcode")
qr=Hr.save('123')