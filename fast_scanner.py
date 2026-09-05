import socket, threading

target = "192.168.182.1"
open_ports = []

def scan(port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        open_ports.append(port)
        print(f"[+] {port} OPEN")
        s.close()
    except:
        pass

print(f"Fast scanning {target}...")
threads = []
for p in [21,22,23,53,80,443,8291,8728,8729]:
    t = threading.Thread(target=scan, args=(p,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nDone! Open: {open_ports}")
