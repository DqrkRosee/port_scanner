import socket
import threading
from queue import Queue
import argparse
import time

parser = argparse.ArgumentParser(description="Multi-threaded Port Scanner")
parser.add_argument("-t", "--target", required=True)
parser.add_argument("-p", "--ports", default="1-100")
parser.add_argument("-w", "--threads", type=int, default=50)

args = parser.parse_args()
target_ip = args.target
threads_count = args.threads

port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

q = Queue()

for p in range(start_port, end_port + 1):
    q.put(p)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except:
        pass

def worker():
    while True:
        port = q.get()
        scan_port(port)
        q.task_done()

start_time = time.time()

for _ in range(threads_count):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()

end_time = time.time()
print(f"Scanning finished in {round(end_time - start_time, 2)}s")