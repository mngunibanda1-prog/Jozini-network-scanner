import socket
from datetime import datetime

target = input("Target IP (e.g. 192.168.182.1): ")
ports = [21,22,23,25,53,80,110,135,139,443,445,993,995,1723,3306,3389,5900,8080,8291,8728]

print(f"\n--- Scan Started {datetime.now()} ---\n")

with open("report.txt","w") as f:
    f.write(f"Scan Report for {target} - {datetime.now()}\n\n")
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((target, port))
            try:
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = s.recv(1024).decode(errors='ignore').strip().split('\n')[0]
            except:
                banner = "No banner"
            print(f"[+] {port}/open -> {banner}")
            f.write(f"[+] {port}/open -> {banner}\n")
        except:
            print(f"[-] {port}/closed")
        s.close()
    print(f"\nSaved to report.txt")

