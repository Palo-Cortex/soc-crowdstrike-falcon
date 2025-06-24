# 🛡️ Cortex XSIAM – CrowdStrike Falcon Integration Setup

Enhances the native CrowdStrike Falcon integration in Cortex XSIAM with tailored layouts, automation support, dashboards, and correlation rules to improve threat visibility and SOC response efficiency.

---

## 🚀 Configuration Steps

### 1. Layout Rule (Recommended)

- Use condition: `tags contains "DS:CrowdStrike"`
- Designed for correlation alerts; compatible with FDR-based alerts (BIOCs/Analytics)
- **Note:** First alert must be ingested before DS tag can be used in a rule

---

### 2. Playbook Trigger (Recommended)

- Use condition: `tags = "DS:CrowdStrike_xxx"`
- Triggers enrichment and response playbooks
- **Note:** DS tag must exist before the trigger rule can be created

---

### 3. Correlation Rule Strategy

- **Option 1:** 12 MITRE tactic-specific rules (granular visibility, harder to manage at scale)
- **Option 2:** 2 simplified rules (EDR/EPP and IDP events; IDP currently lacks MITRE mapping)

---

### 4. Dashboards

- Compatible with XSIAM 2.x
- Update drilldown link on **CrowdStrike Alert Table** to match your tenant for alert navigation
- **Note:** Some widgets may not function as intended on XSIAM 3.x due to dataset changes

---

## ✅ Integration Complete

CrowdStrike Falcon telemetry is now optimized for correlation, investigation, and response within Cortex XSIAM.
