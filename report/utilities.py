import csv
import os

class Utilities:

    @staticmethod
    def writeToFile(output_folder, output_file, data):
        #return 
        os.makedirs(output_folder, exist_ok=True) 
        with open(os.path.join(output_folder, output_file), mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in data:
                writer.writerow(row)
        
    