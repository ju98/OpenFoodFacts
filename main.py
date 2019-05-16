# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:40:11 2019

@author: nadia
"""

from off import OFF
import pandas


if __name__ == "__main__" : 
    
    df = pandas.read_csv('produit_pour_le_client_detail.csv', sep = ";", nrows = 100)
    OpenFoodFacts = OFF(df)
    
#    print("Exemple d'allergenes :")
#    
#    al = OpenFoodFacts.getAllergenes()
#    print(al)

    
    allergens = input("Bonjour , veuillez nous indiquer les ingredients auxquels vous etes allergique (separes par une virgule s'il vous plait) afin de vous proposer des produits plus adapté : ")
    allergens = allergens.split(",")
    
    print("\n\nvoici tous nos produits que vous pouvez consommer : \n")
    products = OpenFoodFacts.productsOk(allergens)
    for p in products:
        if str(p[0]) != "nan" :
            print("\t",p[0])
