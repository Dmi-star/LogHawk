# LogHawk
LogHawk is a tool designed to help security teams automatically monitor and analyze log files for suspicious activity like failed login ttempts or unauthorized access

INSTALLATION
Before running the script make sure that Python is installed, you can install Python by running the command.
sudo apt-get install python3

Next step is to give permission to yourself to allow you to excute the script by running this command
chmod 544 LogHawk.py


Using the script. 
to run the script use the command 
python3 LogHawk.py /path/to/Logfile.log  

The script has the ability to use custom regex defined by the user 
the default regex is set to scan for IP address to change the regex for search the command is 
python3 LogHawk.py /path/to/Logfile.log --regex "(regexcode)" 

Result may vary but should show up as 
# total events found in source file 

Breakdown by user

log analysis is complete timeline saved as timeline.txt

AUTOMATION 
using cron you can automat the script and depending on your need can set it to run every 5 minutes or every hour using this command.
*/5 * * * * crontab /path/to/LogHawk.py path/to/Logfile.log
and if you want to use a custom regex and automate it just use this command. 
*/5 * * * * crontab /path/to/LogHawk.py path/to/Logfile.log --regex "(customregex)" 
