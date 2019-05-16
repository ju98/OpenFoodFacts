# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:40:11 2019

@author: nadia
"""

from off import OFF
import pandas
 
df = pandas.read_csv('produit_pour_le_client_detail.csv', sep = ";", nrows = 100)
OpenFoodFacts = OFF(df)
allergens=input("Bonjour , veuillez nous indiquer les ingredients auxquels vous etes allergique (separes par une virgule s'il vous plait) afin de vous proposer des produits plus adapté : ")
allergens = allergens.split(",")
print("voici tous nos produits que vous pouvez consommer : ")
print(OpenFoodFacts.productsOk(allergens))
