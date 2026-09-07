FROM wazuh/wazuh-manager:4.7.2

# Copy custom rules and decoders into the Wazuh Manager engine
COPY config/wazuh/ossec.conf /var/ossec/etc/ossec.conf
COPY config/wazuh/local_rules.xml /var/ossec/etc/rules/local_rules.xml
COPY rules/decoders/custom_decoders.xml /var/ossec/etc/decoders/custom_decoders.xml

EXPOSE 1514/udp 1515/tcp 514/udp 55000/tcp