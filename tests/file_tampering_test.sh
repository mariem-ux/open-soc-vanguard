#!/bin/bash
# Attack C: Sensitive File Tampering Simulation

echo "------ Simulating sensitive file access & tampering..."
sudo cat /etc/sudoers
sudo cat /etc/passwd | tail -5
sudo touch /etc/passwd


# chmod +x tests/file_tampering_test.sh