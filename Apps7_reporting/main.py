import psycopg2

hostname = 'localhost'
database = 'limitless_demo'
username = 'postgres'
#master password od PGadmina
pwd = 'nagobrijed'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor()
    create_script = ''' CREATE TABLE IF NOT EXISTS daily_report (
                            report_id serial PRIMARY KEY,
                            report_date date NOT NULL,
                            app varchar(45) NOT NULL,
                            platform varchar(45) NOT NULL,
                            requests numeric(5,1) NOT NULL,
                            impressions numeric(5,1) NOT NULL,
                            revenue varchar(10) NOT NULL) '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO daily_report (report_id, report_date, app, platform, requests, impressions, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    insert_value = (1, '16/9/2017', 'Talking Ginger', 'iOS', 9295, 137, '1.096')
    cur.execute(insert_script, insert_value)
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()