import fileinput
import time

def aggregate():
    file_list=('server1_log.txt','server2_log.txt','server3_log.txt','server4_log.txt')#Log files from each servers
    logs = list(fileinput.input(file_list))
    for i in sorted(logs):
        with open('aggregator_logs.txt','a+') as f1:
            f1.write(i)
        f1.close()

while True:
    aggregate()
    time.sleep(60)




        
    
        
            



        
