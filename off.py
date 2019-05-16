# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:19:47 2019

@author: dupouyj
"""

import pandas


class OFF:
    
    def __init__(self, df):
        self.df = df


    def afficheNomColonnes(self):
        '''
            Affiche le nom des colonnes (176 colnnes ici)
        '''
        for x in self.df:
            print(x, "\n")


    def getColonne(self, nom):
        '''
            Retourne la colonne intitulée nom
        '''
        return self.df[nom]
    
        #df['A'][0:3] #les 3 premières valeurs des 3 premières lignes de la colonne 'A' 
    



    def productsOk(self, allergens):
        '''
            Retourne la liste des produits ne contenant pas les allergenes de la liste allergens
        '''
        products = []
        
        for x in self.df.itertuples(): #on parcourre les lignes du dataframe
            i = 0
            colonnes_a_verifier = [x.product_name,x.ingredients_text,x.allergens,x.allergens_en,x.traces,x.traces_en]
            
            for a in allergens: #pour tous les allergenes rentres :
                for c in colonnes_a_verifier: #on parcourre toutes les colonnes ou on doit verifier qui'il n'y a pas d'allergene
                    if a in str(c):
                        i+=1
            
            if i==0: #aucune des conditions precedente a ete verifiee
                products.append([x.product_name, x.ingredients_text])
                
        return products
    
    
    def getAllergenes(self):
        allergens = []
        
        for x in self.df.itertuples():
            if str(x.allergens) != "nan" :
                a = str(x.allergens).split(',') #lorsqu'il y a plusieurs allergenes, ils sont separes par des ",". On recupere donc chaque allergene
                for i in a:
                    if i != "," :
                        allergens.append(i)
        
        al = self.supprimeDoublons(allergens)
        return al



    def supprimeDoublons(self, L):
        '''
            L est une liste de String
        '''
        listeOK = []
        
        for elem in L:
            i=0
            for j in listeOK:
                if elem == j:
                    i+=1
            
            if i==0:
                listeOK.append(elem)
        
        return listeOK

    

# =============================================================================
# 
# =============================================================================
if __name__ == "__main__" :
    
    df = pandas.read_csv('produit_pour_le_client_detail.csv', sep = ";", nrows = 500)
    
    OpenFoodFacts = OFF(df)
    
    #OpenFoodFacts.afficheNomColonnes()
    
    #print(OpenFoodFacts.getColonne("product_name"))
    
    #print(OpenFoodFacts.productsOk(['rice']))  
    
    #print(OpenFoodFacts.getAllergenes())