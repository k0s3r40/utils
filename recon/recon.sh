#!/bin/bash

sudo nmap -O $1 > /tmp/scan.$1.log
cat /tmp/scan.$1.log
cat /tmp/scan.$1.log|grep open