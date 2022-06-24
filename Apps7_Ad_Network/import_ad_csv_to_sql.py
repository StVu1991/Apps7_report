import sys
import pandas as pd
#data = pd.read_csv('https://storage.googleapis.com/expertise-test/supernetwork/report/daily/2017-09-15.csv')
#data = pd.read_csv('https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-15_9_2017.csv')
#print(data)

def count_arguments():
    number_of_arguments = len(sys.argv)
    if number_of_arguments != 3:
        print('Invalid number of arguments. You should pass two arguments')
        return False
    else:
        return True

def validate_arguments():
    if first_argument.lower() != 'supernetwork' and first_argument.lower() != 'adumbrella':
        print('Invalid first argument -> first argument should be supernetwork or adumbrella')
        return False
    else:
        if (len(second_argument) != 10) or (second_argument[4] != '-' or second_argument[7] != '-'):
            print('Invalid date format. Date format should be YYYY-MM-DD, for example: 2022-06-24')
            return False
        else:
            return True

def convert_second_argument(date):
    converted_date = 'dd_mm_yyyy';
    converted_day = date[8:]
    converted_month = int(date[5:7])
    converted_year = date[0:4]

    if converted_month < 10:
        converted_month = str(converted_month)
        converted_month.replace("0", "")

    converted_date = f'{converted_day}_{converted_month}_{converted_year}'
    return converted_date

def form_api_url():
    print(first_argument)
    #https://storage.googleapis.com/expertise-test/supernetwork/report/daily/2017-09-15.csv
    #https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-15_9_2017.csv
    report_url = '';
    if first_argument == 'supernetwork':
        report_url = f'https://storage.googleapis.com/expertise-test/supernetwork/report/daily/{second_argument}.csv'
    elif first_argument == 'adumbrella':
        formatted_date = convert_second_argument(second_argument)
        report_url = f'https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-{formatted_date}.csv'

    return report_url

if count_arguments():
    first_argument = sys.argv[1]
    second_argument = sys.argv[2]
    if validate_arguments():
        source_file_url = form_api_url()
        print(source_file_url)