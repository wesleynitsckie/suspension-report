from .validators import InputFile, OutputFolder, CSVFields
from .reports import Suspension, AgentCollection, PaymentType

class Report:

    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder
        self.report_date = None
        self.data = None

    def validate(self):
        print(" [x] Validate .... ")
        input = InputFile(self.input_file)
        self.report_date = input.getFileDate()
        
        OutputFolder(self.output_folder)

        fields = CSVFields(self.input_file)
        self.data = fields.getData()

    def reports(self):
        print(" [x] Run  Suspension Report.... ")
        suspection_report = Suspension( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        suspection_report.process()

        print(" [x] Run  Agent Collection Report.... ")
        agent_collection_report = AgentCollection( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        agent_collection_report.process()

        print(" [x] Run  Payment Type Report.... ")
        payment_type_report = PaymentType( data=self.data, 
                    output_folder=self.output_folder,
                    report_date=self.report_date )
        payment_type_report.process()

    def run(self):
        try:
            print("\n" +"START".center(70, ":"))
            # Validate
            self.validate()

            # Reports
            self.reports()

            print("COMPLETED".center(70, ":"))
        except Exception as e:
            print(" [xxx] ERROR  {}".format(e))