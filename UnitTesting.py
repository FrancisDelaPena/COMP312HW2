import csv
import collections
import unittest
from HW2 import landlordWards
from HW2 import crimeWards
from HW2 import main

class TestAnalysis(unittest.TestCase):
    def testLLWards(self):
        self.assertNotEqual(landlordWards, 'true')
    def testCrimeWards(self):
        self.assertNotEqual(crimeWards, 'true')

unittest.main()
