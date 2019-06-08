# Security-Logs-Schedules
Security-Logs-Schedules is a python script designed for the purpose of viewing security audit events 4624 and 4625 and saving the latest 10 log on audit events into txt files, it includes a file viewer to see the data written to the log files and a scheduler which can create a new scheduled task in Task Scheduler to run at a specified time triggering the script “CREATEFILEWITHLOGDATA” which will generate a txt file with the 10 latest log on audit events(ID: 4624 and 4625).
# Purpose
Security-Logs-Schedules is a python script designed for the purpose of viewing security audit events 4624 and 4625 and saving the latest 10 log on audit events into txt files, it includes a file viewer to see the data written to the log files and a scheduler which can create a new scheduled task in Task Scheduler to run at a specified time triggering the script “CREATEFILEWITHLOGDATA” which will generate a txt file with the 10 latest log on audit events(ID: 4624 and 4625).
# Requirements
1. Designed and Tested for Windows 10
2. Must run Python script through CMD prompt with Administrative Privileges
3. Python must be installed to path
4. PowerShell is installed and accessible
5. Security Event Auditing enabled.
# Guide
This script will only run properly from path "C:/Security-Logs-Schedules"  <--- This cannot be renamed.
CMD PROMPT TO SCRIPT  <cd C:/Security-Logs-Schedules>
 <"C:/Security-Logs-Schedules\RUN THIS.py"> ---------  dont type <>
Everything should work perfectly fine if user is administrator and has run cmd prompt as admininstrator and brought executed file through python. 
Was designed with Pycharm so should run perfectly fine to run on there if started Pycharm application is started as admin.
User video guide available at - 
