import csv
from os import path
import datetime
from pathlib import Path

class Args:
    """ Validate File and Folder Arguments """
    def __init__(self, sys):
        self.sys = sys

    def getArgs(self):
        if len(self.sys.argv) < 3:
            raise Exception("Sorry, An input file and out folder paths arguments are required")

        return (self.sys.argv[1], self.sys.argv[2])

class InputFile:
    """ Validate the Input File """
    def __init__(self, input_file):
        self.input_file = input_file
        self.validate()

    def validate(self):
        # Check the file name is a valid date
        # YYYY_MM_DD_payments.csv file format
        try:
            file_name = Path(self.input_file).name
            split = file_name.split("_")
            date_text = "{}-{}-{}".format(split[0],split[1], split[2])
            self.date = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect file name format, should be YYYY_MM_DD_payments.csv file format")
            pass
        except Exception as e:
            raise Exception("Incorrect file name format, should be YYYY_MM_DD_payments.csv file format")
        return True

    def getFileDate(self):
        # Check the file name is a valid date
        # YYYY_MM_DD_payments.csv file format
        return self.date

class OutputFolder:
    """ Validate the Input File """
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.validate()

    def validate(self):
        # Check the folder does not exist
        if path.exists(self.output_folder): 
            raise Exception("Sorry, The output folder must not exist. Please select a different folder path")

class CSVFields:
    """ Validate the Input File """
    def __init__(self, input_file):
        self.input_file = input_file
        self.validate()
    
    def validate(self):
        validateHeaders = ['id', 'payment_type', 'payment_amount', 'payment_signature_image', 'payment_photo', 'created', 'status', 'notes', 'agent_user_id', 'device_id']
        with open(self.input_file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            reader = csv.reader(csv_file)
            data = []
            line_count = 0
            for row in csv_reader:
                #print(row['payment_type'])
                if line_count == 0:
                    if list(row.keys()) != validateHeaders:
                        raise Exception("The following headers are valid: id, payment_type, payment_amount, payment_signature_image, payment_photo, created, status, notes, agent_user_id, device_id")
                line_count += 1
                data.append(row)
            print(f' [x] Processed {line_count} lines.')
            if line_count > 100000:
                raise Exception("Sorry, we are limiting the number of records to 100 000 for now")
            self.data = data

    def getData(self):
        return self.data