# Server-Monitor
Monitor the logs from multiple servers and aggregate the logs and store them in the master server.


**************************INTRODUCTION**************************

Aim of this application is to monitor the logs from multiple servers and aggregate the logs and store them in the master server.

This application has two parts,

	1.) Log Collector

	2.) Log Aggregator

Log Collector runs various commands against the server on a periodic basis and stores the data in a log file.

Log Aggregator collects the log files from various servers and aggregate them based on the timestamps in the log files.


**************************PRE REQUISITES**************************

1.) Python 3.x to be installed on all the systems.

2.) Crontab functionality to be enabled in the servers.

3.) rsync functionality to be enabled in the nodes and master server.

**************************HOW TO USE THE CODE**************************

1.) Using Log Collector

>save the program (app_monitor_logs_1.0.0_final.py) in the location where your interpretor identifies.
>Edit your Crontab and place the program by enabling it to run in the intervals as per our requirement. 
>Include the command in Crontab to append the output of above python script to the log file.
>Using similar naming conversion for the log file is advised as it is required in Log Aggregator application. 
>Enable rsync between the node servers(where Log Collector is executed) and the master server(where Log Aggregator is executed).

2.) Using Log Aggregator

>Save the program(app_logs_aggregation1.0.0_final.py) in a location where your interpretor identifies.
>Pass the log file names of the node servers so that the script reads them.
>Execute the script once, it is designed to run continuously in an interval of 1 minute.
>The Log Aggregator program runs every one minute and reads the contents from provided logs, segregates them based on the time stamp and then writes into the aggregator log file.


**************************POTENTIAL PERFORMANCE AND LIMITATIONS**************************

>This application has the potential to monitor any number of services and servers as per requirement.
>This application provides the flexibility to the user for changing the monitoring parameters and interval of monitoring.
>Log aggregation in single server simplifies the monitoring process and saves time.
>This application automates the server monitoring.

>The current version of the application does not offer a user friendly interface to access the logs.
>The logs from different servers are written into the aggregated log file as a single line with time stamp.
>Current version of the application requires the prerequisites like Crontab and rsync
>Manual intervention is required when an error occurs.

**************************FEATURES COMING IN NEXT ITERATION**************************

>Eliminate the requirement of Crontab and rsync.
>Provide a user friendly GUI where the logs can be accessed based on time and date selection as well as other parameters.
>Better presentation of logs by adding adequate graphics.
>A website hosted in cloud, and provide a graphical interface in the dashboard to access the logs of underlying servers.

**************************PROS AND CONS OF THE APPROACH**************************

>Simplified log monitoring approach using functions and short program.
>Automation of the monitoring process and saving logs.
>Made use of the existing modules in the python to make the code simple.

>Made use of the Crontab and rsync functionality of Linux to achieve the result of Python code
>Security factor of the code is not taken into consideration in this iteration.
>The only filter criteria applied to the logs are based on their time stamp.

********************************************************************************************************************************************************************
