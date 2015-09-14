import csv
import collections
import unittest

def landlordWards(): # gets wards from Problem Landlord CSV file
    with open('Problem_Landlord_List_-_Map.csv') as csvfile:
        wardReader = csv.reader(csvfile, delimiter = ',')
        landlordWards = []
        for row in wardReader:
            landlordWards.append(row[5]) #5th row has ward numbers
        return landlordWards
                

def crimeWards(): # get wards from crimes in the past year
    with open('Crimes_-_One_year_prior_to_present.csv') as csvfile:
        wardReader = csv.reader(csvfile, delimiter = ',')
        crimeWards = []
        for row in wardReader:
            crimeWards.append(row[10]) #10th row has ward numbers
        return crimeWards

class TestAnalysis(unittest.TestCase):
    def testLLWards(self):
        self.assertNotEqual(landlordWards, 'true')
    def testCrimeWards(self):
        self.assertNotEqual(crimeWards, 'true')

def main():
    landlordWardCount = []
    crimeWardCount = []

    landlordWardCount.append(collections.Counter(landlordWards()))
    crimeWardCount.append(collections.Counter(crimeWards()))


    print("The wards with notable problem landlords are: ", landlordWardCount) #prints out list of wards and number of instances
    print("The wards with the most crime in the past year are: ", crimeWardCount) #prints out list of wards and number of instances

main()
unittest.main()

