import sys
import pandas as pd
import psycopg2

hostname = 'localhost'
database = 'limitless_demo'
username = 'postgres'
#master password od PGadmina
pwd = 'nagobrijed'
port_id = 5432
conn = None
cur = None

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
    #print(first_argument)
    #https://storage.googleapis.com/expertise-test/supernetwork/report/daily/2017-09-15.csv
    #https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-15_9_2017.csv
    report_url = '';
    if first_argument == 'supernetwork':
        report_url = f'https://storage.googleapis.com/expertise-test/supernetwork/report/daily/{second_argument}.csv'
    elif first_argument == 'adumbrella':
        formatted_date = convert_second_argument(second_argument)
        report_url = f'https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-{formatted_date}.csv'

    return report_url

def read_csv(source_url):
    data = pd.read_csv(source_url, skipfooter=1, engine='python')
    return data

def insert_data_to_db(csv_data):
    #print(csv_data)
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS daily_report')
        create_script = ''' CREATE TABLE IF NOT EXISTS daily_report (
                                report_id serial PRIMARY KEY,
                                report_date date NOT NULL,
                                app varchar(45) NOT NULL,
                                platform varchar(45) NOT NULL,
                                requests INT NOT NULL,
                                impressions INT NOT NULL,
                                revenue varchar(10) NOT NULL) '''
        cur.execute(create_script)

        for ind in csv_data.index:
            report_date_val = csv_data['Date'][ind]
            app_val = csv_data['App'][ind]
            platform_val = csv_data['Platform'][ind]
            requests_val = csv_data['Requests'][ind]
            impressions_val = csv_data['Impressions'][ind]

            if first_argument == 'adumbrella':
                revenue_val = csv_data['Revenue (usd)'][ind]
                revenue_val = "${:.2f}".format(revenue_val)
            else:
                revenue_val = csv_data['Revenue'][ind]
            #print(df['Name'][ind], df['Stream'][ind])
            # df. iloc[:, 0]
        #for record in:
            request_int_val = int(requests_val)
            impressions_int_val = int(impressions_val)
            insert_script = 'INSERT INTO daily_report (report_date, app, platform, requests, impressions, revenue) VALUES ( %s, %s, %s, %s, %s, %s)'
            insert_value = (report_date_val, app_val, platform_val, request_int_val, impressions_int_val, revenue_val)
            cur.execute(insert_script, insert_value)
        #for exit

        cur.execute('SELECT * FROM daily_report')
        for record in cur.fetchall():
            print(record)

        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if count_arguments():
    first_argument = sys.argv[1]
    print(first_argument)
    second_argument = sys.argv[2]
    if validate_arguments():
        source_file_url = form_api_url()
        api_csv_dataframe_data = read_csv(source_file_url)
        insert_data_to_db(api_csv_dataframe_data)