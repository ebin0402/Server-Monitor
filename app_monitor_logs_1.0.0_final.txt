#!/usr/bin/env python
#Collector application which collects the logs data and sends accross to the aggregator application
import os
import psutil
import datetime
import socket
import getpass
import time

server = socket.gethostname()
path = os.getcwd()
user = getpass.getuser()
tm = datetime.datetime.now()

#Function defenitions
def cpu_monitor():
    print("*"*25,"CPU LOGS","*"*25,"\n")
    cpu_time=psutil.cpu_times(percpu=True)
    cpu_percent=psutil.cpu_percent(percpu=True,interval=None)
    cpu_count=psutil.cpu_count()
    cpu_status=psutil.cpu_stats()
    cpu_frequency=psutil.cpu_freq()
    print("-"*25,"CPU TIME IS","-"*25,"\n",cpu_time)
    print("-"*25,"CPU PERCENTAGE IS","-"*25,"\n",cpu_percent)
    print("-"*25,"CPU COUNT IS","-"*25,"\n",cpu_count)
    print("-"*25,"CPU STATUS IS","-"*25,"\n",cpu_status)
    print("-"*25,"CPU FREQUENCY IS","-"*25,"\n",cpu_frequency)
def memory_monitor():
    print("*"*25,"MEMORY LOGS","*"*25,"\n")
    virt_mem=psutil.virtual_memory()
    swap_mem=psutil.swap_memory()
    print("-"*25,"VIRTUAL MEMORY USAGE IS","-"*25,"\n",virt_mem)
    print("-"*25,"SWAP MEMORY USAGE IS","-"*25,"\n",swap_mem)
def disk_monitor():
    print("*"*25,"DISK LOGS","*"*25,"\n")
    disk_part=psutil.disk_partitions(all=True)
    disk_usage=psutil.disk_usage(path)
    disk_io=psutil.disk_io_counters()
    print("-"*25,"DISK PARTITION IS","-"*25,"\n",disk_part)
    print("-"*25,"DISK USAGE IS","-"*25,"\n",disk_usage)
    print("-"*25,"DISK I/O IS","-"*25,"\n",disk_io)       
def process_monitor():
    print("*"*25,"PROCESS LOGS","*"*25,"\n")
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
        except:
            pass
        else:
            print(pinfo)
            
#Function calls begin here
print(datetime.datetime.now(),"\n")
print("*"*25,"LOGS ITERATION BEGINS","*"*25,"\n")
print("YOU ARE : ", user,"\n")
print(user,"YOU ARE IN THE SERVER: ", server,"\n")
print(user,"\tYOU ARE IN THE LOCATION : ",path,"\n")
print("*"*25, "CPU UTILIZATION","*"*25,"\n1")
cpu_monitor()
print("*"*25,"MEMORY USAGE","*"*25,"\n")
memory_monitor()
print("*"*25,"DISKSPACE USAGE","*"*25,"\n")
disk_monitor()
print("*"*25,"RUNNING PROCESSESS","*"*25,"\n")
process_monitor()
print("\n","*"*25,"END OF LOGS ITERATION","*"*25,"\n")
            
    
    
