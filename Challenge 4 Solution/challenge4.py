import os 
from os import system
import math
from math import ceil

system('clear')
gallonPrice = 32
fname = input('Enter your first name so that I can address you properly >> ')
print(f'{fname}, great!! Let us grab some info on your wall!!')

def calculateGallons(a):
    numOfGallons = a/350
    return numOfGallons

def calculatePrice(l, w, h):
    area = 2 * l * (l + w)
    gallons = calculateGallons(area)
    priceToPaintWall = ceil(gallons) * gallonPrice
    return priceToPaintWall


length = float(input('Enter the length >> '))
width = float(input('Enter the width >> '))
height = float(input('Enter the height >> '))
price = calculatePrice(length, width, height)

print(f'The price to paint a {length} x {width} x {height} wall is ${price} dollars')