import unittest, csv
from os import path
import datetime
import shutil, tempfile
from report.validators import CSVFields
from report.reports import Suspension, AgentCollection, PaymentType

class TestReports(unittest.TestCase):
    test_data_file_path = './__unittests__/2019_03_08_payments.csv'

    def setUp(self):
        # Create a temporary directory
        self.tempdir = tempfile.mkdtemp()
        self.output_folder =path.join(self.tempdir, 'somepath/')
        
        #print(self.test_dir)
        fields = CSVFields(self.test_data_file_path)
        self.data = fields.getData()
        self.report_date = datetime.datetime(2019,4,8)

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.tempdir)

    def test_suspension_report(self):
        sr = Suspension( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        self.assertEqual(sr.process(), 97)

    def test_agent_report(self):
        ar = AgentCollection( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        self.assertEqual(ar.process(), 39)
    
    def test_agent_report(self):
        pr = PaymentType( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        self.assertEqual(pr.process(), 5)