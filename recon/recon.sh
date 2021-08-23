#!/bin/bash

echo "Scanning via nmap to detect os and ports"
sudo nmap -O $1 > /tmp/scan.$1.log
cat /tmp/scan.$1.log
cat /tmp/scan.$1.log|grep open
echo "Scan completed"
echo "Testing ports"
python3 check_ports_vulnerabilities.py $1