# 🛡️ Cortex XSIAM – CrowdStrike Falcon Integration Setup

Enhances the native CrowdStrike Falcon integration in Cortex XSIAM with tailored layouts, automation support, dashboards, and correlation rules to improve threat visibility and SOC response efficiency.

---

## 🚀 Configuration Steps

### 1. Configure the CrowdStrike Falcon Integration Instance
1. Navigate to **Settings → Configurations → Data Collection → Automation & Feed Integration**
2. Expand the CrowdStrike Falcon instance dropdown 
3. Click on the gear next to the _CrowdstrikeFalcon_Detections_Incidents_
4. Update the integration instance’s configuration for the following form fields: 
   1. Server URL
   2. Client ID
   3. Secret
   
5. Test and save the integration instance configuration
6. **Enable** the instance

---

### 2. Layout Rule (Recommended)

- Use condition: `tags contains "DS:CrowdStrike"`
- Designed for correlation alerts; compatible with FDR-based alerts (BIOCs/Analytics)
- **Note:** First alert must be ingested before DS tag can be used in a rule


---

### 3. Playbook Trigger (Recommended)

- Use condition: `tags = "DS:CrowdStrike_xxx"`
- Triggers enrichment and response playbooks
- **Note:** DS tag must exist before the trigger rule can be created

---

### 4. Correlation Rule Strategy

- **Option 1:** 12 MITRE tactic-specific rules (granular visibility, harder to manage at scale)
- **Option 2:** 2 simplified rules (EDR/EPP and IDP events; IDP currently lacks MITRE mapping)

---

### 5. Dashboards

- Compatible with XSIAM 2.x
- Update drilldown link on **CrowdStrike Alert Table** to match your tenant for alert navigation
- **Note:** Some widgets may not function as intended on XSIAM 3.x due to dataset changes

---

## ✅ Integration Complete

CrowdStrike Falcon telemetry is now optimized for correlation, investigation, and response within Cortex XSIAM.
