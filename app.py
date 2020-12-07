
from report.main import Report
import sys
from report.validators import Args

if __name__ == '__main__':
    try:
        args = Args(sys)
        (input, output) = args.getArgs()
        report = Report(input, output)
        report.run()
    except Exception as e:
        print(" [x] ERROR {}".format(e))