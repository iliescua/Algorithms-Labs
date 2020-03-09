import unittest

import random

from sorting import insertion_sort

N_NUMBERS = 100

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_random(self):
        """
        Tests insertion sort using a list of randomly-ordered
        numbers.
        """
        
        numbers = [random.random() for i in range(N_NUMBERS)]
        
        
        # make a copy of the list
        observed = numbers[:]
        insertion_sort(observed)
        
        # make a copy of the list
        # and sort using built-in function
        expected = numbers[:]
        expected.sort()
        
        self.assertEqual(observed, expected)
        
    def test_insertion_sort_sorted(self):
        """
        Tests insertion sort using a list of sorted
        numbers.  Ensures that insertion sort maintains
        the sorted property.
        """
        
        numbers = [random.random() for i in range(N_NUMBERS)]
        numbers.sort()
        
        # make a copy of the list
        expected = numbers[:]
       
        # make a copy of the list
        observed = numbers[:]
        insertion_sort(observed)
        
        self.assertEqual(observed, expected)
        
if __name__ == "__main__":
    unittest.main()
