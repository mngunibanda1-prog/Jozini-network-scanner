# Jozini Network Scanner

Built on 2026-09-05 at KwaQondile Library, Jozini KZN using Termux on Android

## What I Built
- **scanner.py** - Port scanner with banner grabbing (20 ports) + auto report saving
- **cve_check.py** - Maps RouterOS version to known CVEs
- **final.py** - HTTP confirmation of target
- **report.txt** - Real scan report

## Real Finding
Target: 192.168.182.1 (KwaQondile Library)
- Open: 21, 22, 80, 8291, 8728
- Banner: MikroTik RouterOS 6.46.8 (2020)
- Vulnerability: CVE-2020-2021 - Winbox Auth Bypass (CRITICAL)
- Risk: HIGH - Needs upgrade to RouterOS 7.x

## Skills Used
Python, Sockets, Network Scanning, CVE Research, Report Writing

## Author
Banda Mnguni - Aspiring Pentester from Jozini, KZN
Built with: Termux + Python3
Contact: mngunibanda1@gmail.com
