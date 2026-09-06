# OPNsense & Suricata Integration Notes

## 1. Network Architecture
* **OPNsense Gateway IP:** `192.168.2.1`
* **Wazuh Manager IP:** `192.168.2.10`
* **Protocol & Port:** UDP / `514`

## 2. Syslog Export Configuration
* Configured in OPNsense under System -> Settings -> Logging / Targets.
* Source IP: `192.168.2.1`
* Transport: UDP Port 514 targeting Wazuh Manager (`192.168.2.10`).
* Captured Facilities: `user.info`, `local0.info` (Suricata/Firewall events).

## 3. Verification Commands
To verify Syslog traffic arriving at the Wazuh Manager:
```bash
sudo tcpdump -i any port 514 -n
```
To monitor real-time parsed security alerts:
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```