import unittest
import datetime
from os import path
import shutil, tempfile
from unittest import mock
from report.validators import InputFile, OutputFolder

class TestValidators(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        #print(self.test_dir)
		
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_valid_filename(self):
        input = InputFile("2020_12_12_payment.csv")
        self.assertIsInstance(input, InputFile)

    def test_invalid_date_filename(self):
        with self.assertRaises(Exception):
            InputFile("2020_30_12_payment.csv")

    def test_invalid_filename(self):
        with self.assertRaises(Exception):
            InputFile("dd.csv")

    def test_get_date(self):
        input = InputFile("2020_12_12_payment.csv")
        self.assertIsInstance(input.getFileDate(), datetime.datetime)
        self.assertEqual(input.getFileDate().strftime("%Y-%m-%d") , "2020-12-12")

    def test_folder_dont_exist(self):
        OutputFolder(path.join(self.test_dir, 'somepath/'))

    def test_folder_exist(self):
        with self.assertRaises(Exception):
            OutputFolder(self.test_dir)

        