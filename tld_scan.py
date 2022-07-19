import subprocess
import queue
import argparse
from threading import Thread
from threading import Lock

parser = argparse.ArgumentParser()
parser.add_argument("domain")
parser.add_argument("wordlist")
parser.add_argument("-t", dest="threads", default=33)

args = parser.parse_args()

target_domain = args.domain
wordlist_file = args.wordlist
threads = int(args.threads)

class EnumThreads():
    to_level_domains = queue.Queue()
    exit_flag = 'exit_b6bf725c-b629-4275-bb8f-1485cc760073'
    lock = Lock()
    
def read_file(file_name):
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
   
    final_data = []
   
    for line in data:
        line = line.replace('\n', '').replace('\r', '').replace(' ', '').replace('\t', '')
        EnumThreads.to_level_domains.put(line)
    
    EnumThreads.to_level_domains.put(EnumThreads.exit_flag)
    
def exec_comand(comand):
    try:
        cmd = subprocess.Popen(comand, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = str(cmd.stdout.read().decode())

        return out
    except Exception as error:
        print("exec_comand " + str(error))

def safe_print(data):
    EnumThreads.lock.acquire()
    print(data)
    EnumThreads.lock.release()
    
def start_enum():
    while True:
        tld = EnumThreads.to_level_domains.get()
        if tld == EnumThreads.exit_flag:        
            EnumThreads.to_level_domains.put(EnumThreads.exit_flag)
            break
        
        new_target = target_domain.replace("*", tld).replace('..', '.')
        command = 'host ' + new_target
        out = exec_comand(command)
        
        if new_target + ' has address ' in out:
            safe_print(new_target)
        
def main():
    read_file(wordlist_file)
    
    for i in range(0, threads):
        t = Thread(target=start_enum)
        t.start()
    
main()
