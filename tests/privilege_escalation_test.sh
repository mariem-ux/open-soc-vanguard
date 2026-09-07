#!/bin/bash
# Attack A: Privilege Escalation Reconnaissance Simulation

echo "----- Simulating privilege escalation recon..."
whoami
id
uname -a
sudo -l
cat /etc/passwd
sudo cat /etc/shadow
find / -perm -4000 -type f 2>/dev/null

#chmod +x tests/privilege_escalation_test.sh