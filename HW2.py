import csv
import collections
import unittest

def landlordWards(): # gets wards from Problem Landlord CSV file
    with open('Problem_Landlord_List_-_Map.csv') as csvfile:
        wardReader = csv.reader(csvfile, delimiter = ',')
        landlordWards = []
        for row in wardReader:
            landlordWards.append(row[5]) #5th row has ward numbers
        del landlordWards[0] #deletes the "WARD" row title
        return landlordWards
                

def crimeWards(): # get wards from crimes in the past year
    with open('Crimes_-_One_year_prior_to_present.csv') as csvfile:
        wardReader = csv.reader(csvfile, delimiter = ',')
        crimeWards = []
        for row in wardReader:
            crimeWards.append(row[10]) #10th row has ward numbers
        del crimeWards[0] #deletes the "WARD" row title
        return crimeWards

def main():
    landlordWardCount = []
    crimeWardCount = []

    landlordWardCount.append(collections.Counter(landlordWards()))
    crimeWardCount.append(collections.Counter(crimeWards()))


    print("The wards with the most to least notable problem landlords are: ", landlordWardCount) #prints out list of wards and number of instances
    print("The wards with the most to least crime in the past year are: ", crimeWardCount) #prints out list of wards and number of instances
    print("")
    print("There seems to be little correlation between the number of crimes and problematic landlords.")

main()

