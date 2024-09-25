import unittest
import os
from analyze import *


class TestAnalyze(unittest.TestCase):
    def test_A_string(self):
        
        fund_freq, string = find_frequency_and_string(f'./guitar_strings/A_string.wav')
        self.assertEqual(string, "A string")


    def test_all_strings(self):
        string_files = os.listdir('./guitar_strings')
    
        for file in string_files:
            # print("\nFilename: ", file)
            fund_freq, string = find_frequency_and_string(f"./guitar_strings/{file}")
            # print("Frequency found: ", fund_freq)
            # print("Guessed String: ", string)

            self.assertEqual(file[0], string[0])

        
if __name__ == "__main__":
    unittest.main()