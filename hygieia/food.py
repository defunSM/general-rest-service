from typing import List
from dataclasses import dataclass

import pandas as pd

@dataclass
class Food:
    name: str
    fat: float
    carb: float
    protein: float
    
    def display(self):
        print(f"{self.name} - FAT: {self.fat}g, CARB: {self.carb}g, PROTEIN: {self.protein}g")


def initialize_foods() -> List[Food]:
    """ A list of basic food names and their macros (fat, carb, protein) in grams
    
    """