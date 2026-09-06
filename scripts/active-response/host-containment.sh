#!/bin/bash
read -r INPUT_JSON
SRCIP=$(echo "$INPUT_JSON" | grep -oP '"srcip"\s*:\s*"\K[^"]+')

if [ -n "$SRCIP" ]; then
    iptables -I INPUT -s "$SRCIP" -j DROP
    echo "$(date) isolate-host.sh: blocked $SRCIP" >> /var/ossec/logs/active-responses.log
else
    echo "$(date) isolate-host.sh: no srcip found in alert" >> /var/ossec/logs/active-responses.log
fi
exit 0