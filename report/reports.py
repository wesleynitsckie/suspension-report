from datetime import date, time, datetime
from .utilities import Utilities

class Suspension:

    def __init__(self, data, output_folder, report_date):
        self.data = data
        self.report_date = report_date
        self.output_folder = output_folder
        self.report_data = {}

    def process(self):
        for row in self.data:
            if row['status'] != 'SUCCESSFUL':
                continue
            self.report_data[row['device_id']] = self.days_from_suspension(row)
            
        # Sort by days suspended desc
        sorted_data = self.getSorted() 

        #Write to file
        Utilities.writeToFile(
            output_folder=self.output_folder, 
            output_file='days_from_suspension_report.csv', 
            data=sorted_data
        )
        print( f" [x] Suspension Report [{len(self.report_data)} entries] .... ")
        return len(self.report_data)

    def getSorted(self):
        formattedList = []
        for item in self.report_data:
            formattedList.append([item, str(self.report_data[item])])
        formattedList.sort(key=lambda t: t[1], reverse=True)
        print(formattedList)
        return formattedList

    def days_from_suspension(self, row):
        # Only Allow successful payments to be checked
        if row['status'] != "SUCCESSFUL":
            return (False, 0)

        # Get the Last Payment Date 
        last_payment_date = datetime.strptime(row['created'], "%Y-%m-%d %H:%M:%S")

        # Get the days since last payment
        days_since_last_payment = (self.report_date - last_payment_date).days
        return int(days_since_last_payment + 90)
        

class AgentCollection:
    def __init__(self, data, output_folder, report_date):
        self.data = data
        self.report_date = report_date
        self.output_folder = output_folder
        self.report_data = {}
        #self.process()

    def process(self):
        for row in self.data:
            # Ignore unsuccessful payments
            if row['status'] != 'SUCCESSFUL':
                continue
            key = self.getKey(row)
            if key in self.report_data:
                self.report_data[key] = int(self.report_data[key]) + int(row['payment_amount'])
            else:
                self.report_data[key] = row['payment_amount']

        sorted_list = self.getSorted()
        
        #Write to file
        Utilities.writeToFile(
            output_folder=self.output_folder, 
            output_file='agent_collection_report.csv', 
            data=sorted_list
        )
        print( f" [x] Agent Collect Report [{len(self.report_data)} entries] .... ")
        return len(self.report_data)

    def getKey(self, row):
        return row['agent_user_id'] + "~" + self.getFormattedDate(row['created']) + "~" + row['payment_type']
    
    def getSorted(self):
        formattedList = []
        for item in self.report_data:
            rec = item.split("~")
            rec.append(self.report_data[item])
            formattedList.append(rec)
            
        formattedList.sort(key=lambda x: (x[0], x[1]))
        return formattedList

    def getFormattedDate(self, unformatted_date):
        return datetime.strptime(unformatted_date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

class PaymentType:

    def __init__(self, data, output_folder, report_date):
        self.data = data
        self.report_date = report_date
        self.output_folder = output_folder
        #self.process()

    def process(self):
        report_data = {}
        for row in self.data:
            pass

    def __init__(self, data, output_folder, report_date):
        self.data = data
        self.report_date = report_date
        self.output_folder = output_folder
        self.report_data = {}
        self.process()

    def process(self):
        for row in self.data:
            # Ignore unsuccessful payments
            if row['status'] != 'SUCCESSFUL':
                continue
            key = self.getKey(row)
            if key in self.report_data:
                self.report_data[key] = int(self.report_data[key]) + int(row['payment_amount'])
            else:
                self.report_data[key] = row['payment_amount']

        sorted_list = self.getSorted()
        #Write to file
        Utilities.writeToFile(
            output_folder=self.output_folder, 
            output_file='payment_type_report.csv', 
            data=sorted_list
        )
        print( f" [x] Payment Type Report [{len(self.report_data)} entries] .... ")
        return len(self.report_data)

    def getKey(self, row):
        return row['payment_type'] 
    
    def getSorted(self):
        formattedList = []
        for item in self.report_data:
            formattedList.append([item, self.report_data[item]])
            
        formattedList.sort(key=lambda x: (x[0], x[1]))
        #print(formattedList)
        return formattedList