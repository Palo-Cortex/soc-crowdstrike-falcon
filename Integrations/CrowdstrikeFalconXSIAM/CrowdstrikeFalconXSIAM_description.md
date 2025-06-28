To get an API client ID and secret, contact [CrowdStrike support](mailto:support@crowdstrike.com).


#### Important:

This integration is enabled by default for the new CrowdStrike Raptor version. 

### Required API client scopes

In order to use the CrowdStrike Falcon integration, the API client and secret must have the following scopes and permissions:

- Real Time Response - Read and Write
- Alerts - Read and Write
- IOC Manager - Read and Write
- IOA Exclusions - Read and Write
- Machine Learning Exclusions - Read and Write
- Detections - Read and Write
- Hosts - Read and Write
- Host Groups - Read and Write
- Incidents - Read and Write
- Spotlight Vulnerabilities - Read
- User Management - Read
- On-Demand Scans (ODS) - Read and Write
- Identity Protection Entities - Read and Write
- Identity Protection Detections - Read and Write
- Identity Protection Timeline - Read
- Identity Protection Assessment - Read

### Troubleshooting

- When encountering connectivity or authorization errors, it is necessary to include the IP addresses corresponding to the relevant region in the CrowdStrike Falcon allow list. These IP addresses can be found in the [documentation on enabling access to Cortex]( https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Resources-Required-to-Enable-Access  ) by searching for **Egress**.

- When encountering HTTP 429 response error code from CrowdStrike Falcon, use an engine as explained in this [link]( https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Engines  ).




---
[View Integration Documentation](https://xsoar.pan.dev/docs/reference/integrations/crowdstrike-falcon)