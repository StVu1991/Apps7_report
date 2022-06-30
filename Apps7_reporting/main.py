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

def insert_data_to_db():
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
                                requests numeric(5,1) NOT NULL,
                                impressions numeric(5,1) NOT NULL,
                                revenue varchar(10) NOT NULL) '''
        cur.execute(create_script)
        #for record in:
        insert_script = 'INSERT INTO daily_report (report_id, report_date, app, platform, requests, impressions, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        insert_value = (1, '16/9/2017', 'Talking Ginger', 'iOS', 9295, 137, '1.096')
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
    second_argument = sys.argv[2]
    if validate_arguments():
        print(first_argument)
        print(second_argument)
