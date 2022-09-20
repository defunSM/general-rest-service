from typing import List
from dataclasses import dataclass

import pandas as pd
import csv

@dataclass
class Food:
    name: str
    fat: float
    carb: float
    protein: float
    
    def display(self):
        print(f"{self.name} - FAT: {self.fat}g, CARB: {self.carb}g, PROTEIN: {self.protein}g")

def initialize_foods() -> dict:
    """ A list of basic food names and their macros (fat, carb, protein) in grams
    
    """
    
    food_csv = pd.read_csv('food.csv')
    print(food_csv[['Category', 'Data.Carbohydrate', 'Data.Fat.Total Lipid', 'Data.Protein']])
    
def search_food_api_call(name: str):
    """_summary_

    Args:
        name (str): _description_
    """
    
    
    
if __name__ == '__main__':
    initialize_foods()