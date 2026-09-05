import socket

target = "192.168.182.1"
print(f"Checking {target} for known MikroTik vulns...\n")

# Your finding from report.txt
version = "6.46.8"
print(f"Detected: RouterOS {version}\n")

vulns = {
    "6.46.8": [
        "CVE-2020-2021 - Winbox Authentication Bypass (Critical)",
        "CVE-2020-11881 - DNS Cache Poisoning",
        "CVE-2019-3943 - Directory Traversal - Hackers can read files!"
    ]
}

if version in vulns:
    print("[!] VULNERABLE! Found:")
    for v in vulns[version]:
        print(f" - {v}")
    print("\n[+] Risk: HIGH - This router needs update to 7.x NOW")
else:
    print("[+] Seems OK")

print("\n--- Next: Try to open http://192.168.182.1 in your Chrome - you will see MikroTik login page! ---")
