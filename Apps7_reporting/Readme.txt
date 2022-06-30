CSV Report to DB - version 1.0 - 29.6.2022

GENERAL INFORMATION
------------------
This Python script is developed and tested using Windows OS and it is recommended to use it on Windows OS.

PREREQUISITES
------------------
1. Python installation

To start this script on your OS should be able to execute Python scripts:
- Enter Command Prompt and type 'python' 
	- if Python version is returned with this command, that means 
  	  you are able to execute Python scripts
	- if 'python' command is not recognized that means you need to install Python in your OS:
	  Python installation is available here: https://www.python.org/downloads/release/python-3105/
	  Download Windows installer file and follow installation steps. 
	  After installation open Command prompt one more time and enter 'python'. If Python version is
          displayed, this step is finished!	 

2. pgAdmin installation

This script will convert reports data from CSV into the PostgreSQL DB. 
To work with PostgreSQL it is recommended to install pgAdmin which is designed to monitor and manage  
PostgreSQL database servers.
pgAdmin installation for Windows is available here: https://www.pgadmin.org/download/pgadmin-4-windows/

3. Create database in pgAdmin -> 
a) Expand PostgreSQL 14 in pgAdmin
b) Right click on Databases
c) Create -> Database (for database name use name of database you specified inside Python script)


HOW TO USE SCRIPT (non-Dockerized)
--------------------
Script contains only one file called - main.py
Steps to execute script:
1. Open Command prompt/Powershell/or any other CLI
2. Navigate to script location and execute following commands (one-by-one) to install necessary Python packages:

pip3 install psycopg2
pip3 install pandas

3. Navigate to script location and execute script with following command:
python main.py <argument1> <argument2>

argument 1 - this argument can have two values: 'supernetwork' or 'adumbrella', depending from which storage
             you want to download report
argument 2 - date in format:  YYYY-MM-DD (2022-06-30)

For example --> to start script main.py located in C:\scripts do following:
	1. Open Command prompt (or any other CLI)
	2. execute command to navigate to folder where scripts is located -> cd C:\scripts
	3. execute command to run the script -> python.main py supernetwork 2022-06-30
	4. That's it, your CSV report is inserted into database!

HOW TO USE SCRIPT (Dockerized version)
---------------------
Scripts contains two files - main.py and Dockerfile
1. Open Command prompt/Powershell/or any other CLI
2. Navigate to script location where script and Dockerfile are located and execute following commands to build Docker image:
docker build -t apps7_report .
3. Run Docker container 
docker run apps7_report supernetwork 2017-09-15




 