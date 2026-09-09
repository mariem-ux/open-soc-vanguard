# Open SOC Vanguard 🛡️

A custom, Linux-centric Security Operations Center (SOC) home lab and detection engineering pipeline built for real-time log ingestion, threat detection, and active threat containment.

---
## Documentation & Reports

* **Technical Architecture:** Detailed data flow and component integration can be found in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
* **Full Report (PDF):** View the complete academic document in [`docs/Open_SOC_Vanguard_Report.pdf`](docs/Open_SOC_Vanguard_Report.pdf).

---

## System Architecture & Key Components

* **Log Aggregation & SIEM:** Wazuh Manager (`192.168.2.10`)
* **Network Gateway & Firewall:** OPNsense (`192.168.2.1`) streaming Syslog over UDP port `514`
* **Intrusion Detection (IDS):** Suricata engine integrated with OPNsense
* **Endpoint Telemetry:** Linux Auditd (`audit.rules`) tracking execution and file system events
* **Automated Containment:** Active Response scripts (`host-containment.sh`) invoking Wazuh REST APIs

---

##  Repository Structure

```text
open-soc-vanguard/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
├── README.md
├── config/
│   ├── auditd/
│   │   └── audit.rules
│   ├── opnsense/
│   │   └── syslog-suricata-notes.md
│   └── wazuh/
│       ├── local_rules.xml
│       └── ossec.conf
├── docker/
│   ├── wazuh-dashboard/
│   │   └── Dockerfile
│   ├── wazuh-indexer/
│   │   └── Dockerfile
│   └── wazuh-manager/
│       └── Dockerfile
├── docs/
│   ├── ARCHITECTURE.md
│   ├── Open_SOC_Vanguard_Report.pdf
│   ├── diagrams/
│      ├──network_topology.png
       └──alert_processing_pipeline.png
├── rules/
│   ├── decoders/
│   │   └── custom_decoders.xml
│   └── sigma/
│       └── sensitive_file_tampering.yml
├── scripts/
│   ├── active-response/
│   │   └── host-containment.sh
│   └── api/
│       ├── requirements.txt
│       └── wazuh_report.py
└── tests/
    ├── file_tampering_test.sh
    └── privilege_escalation_test.sh
```
## Deployment & Usage

### 1. Spin Up the SIEM Stack (Docker)
Start the containerized Wazuh Manager, Indexer, and Dashboard stack:

#### Clone the repository
```Bash
git clone [https://github.com/mariem-ux/open-soc-vanguard.git](https://github.com/mariem-ux/open-soc-vanguard.git)
cd open-soc-vanguard
```
#### Build and start the containers in detached mode
```bash
docker compose up -d --build
```
#### Access the Wazuh Dashboard at https://localhost:5601 once the containers are running.

### 2. Deploy Endpoint Telemetry
Copy the custom Linux audit rules to your target Linux host:

```Bash
sudo cp config/auditd/audit.rules /etc/audit/rules.d/audit.rules
sudo augenrules --load
```
### 3. Configure Wazuh Active Response
Deploy the containment script on the Wazuh Manager:

```Bash
sudo cp scripts/active-response/host-containment.sh /var/ossec/active-response/bin/host-containment.sh
sudo chmod +x /var/ossec/active-response/bin/host-containment.sh
```
### 4. Run API Reporting Script
Install the required dependencies and generate reports through the Wazuh REST API:

```Bash
pip install -r scripts/api/requirements.txt
python3 scripts/api/wazuh_report.py
```
### 5. Execute Attack Simulations
Run the validation tests inside your target Linux environment:

```Bash
./tests/privilege_escalation_test.sh
./tests/file_tampering_test.sh
```
## Verification Commands
### Monitor Syslog Traffic
Monitor incoming Syslog packets on UDP port 514:

```Bash
sudo tcpdump -i any port 514 -n
```
### Monitor Wazuh Alerts
#### Watch real-time security alerts on the Wazuh Manager:

```Bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```
## Project Goals
● Centralized security monitoring

● Linux endpoint visibility

● Network traffic monitoring

● Custom detection rules

● File tampering detection

● Privilege escalation detection

● Automated incident response

● Security event correlation

● Attack simulation and validation

## Technologies
● SIEM / XDR: Wazuh, Wazuh REST API

● Firewall & IDS: OPNsense, Suricata

● Endpoint Telemetry: Linux Auditd

● Automation & Containerization: Bash, Python, Docker, Docker Compose

● Protocols & Standards: Syslog, Sigma Rules

## Security Workflow
```text
Linux Endpoint
      │
      │ Auditd Logs
      ▼
 Wazuh Agent
      │
      ▼
 Wazuh Manager
      │
      ├──────────────► Detection Rules
      │
      ├──────────────► Security Alerts
      │
      └──────────────► Active Response
                            │
                            ▼
                     Host Containment


OPNsense
   │
   ├── Syslog ──────────────► Wazuh Manager
   │
   └── Suricata IDS
            │
            ▼
      Security Events
```
## Testing
The project includes attack simulation scripts used to validate the detection pipeline.

### File Tampering Test
```Bash
./tests/file_tampering_test.sh
```
#### Expected Workflow:

```text
File Modification ──► Auditd Event ──► Wazuh Agent ──► Wazuh Manager ──► Custom Detection Rule ──► Security Alert ──► Active Response
```

### Privilege Escalation Test
```Bash
./tests/privilege_escalation_test.sh
```
#### Expected Workflow:

```text
Privilege Escalation Activity ──► Auditd Event ──► Wazuh Agent ──► Wazuh Manager ──► Detection Rule ──► Security Alert
```
## Project Status
Developed as a cybersecurity SOC home lab focused on detection engineering, security monitoring, and automated incident response.

## Author

**Mariem Rmili**
Cybersecurity Intern - No Breach Training Hub
