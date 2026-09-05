import socket
s = socket.socket()
s.settimeout(3)
s.connect(("192.168.182.1", 80))
s.send(b"GET / HTTP/1.0\r\n\r\n")
data = s.recv(1024).decode(errors='ignore')
print(data[:500])
if "MikroTik" in data or "RouterOS" in data:
    print("\n[+] CONFIRMED: Web login page is MikroTik - scan is 100% legit!")
