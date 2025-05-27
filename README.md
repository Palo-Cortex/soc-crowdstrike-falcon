## 🛠 Installation & Configuration

### 📦 Installing the Pack into Cortex XSIAM

To install this content pack using the [Demisto SDK](https://github.com/demisto/demisto-sdk), run the following command:

demisto-sdk upload -x -z -i /Users/sbrumley/IdeaProjects/xsiam-pov-automation/Packs/soc-crowdstrike-falcon

> **Note:**  
> - `-x` ensures the pack is zipped before upload.  
> - `-z` uploads the zipped pack.  
> - Adjust the path (`-i`) as needed to match your local directory structure.

Make sure your environment is properly configured with the XSIAM host and API key by using either:

- A `.demisto-sdk-conf` file, **or**
- Setting the following environment variables:
  - `DEMISTO_BASE_URL`
  - `DEMISTO_API_KEY`

---

### 🧩 Post-Installation Configuration

After uploading the pack, complete the following steps to ensure alerts are displayed properly:

1. Navigate to **Settings > Alert Layout Rules** in XSIAM.
2. Click **Add Layout Rule**.
3. Configure the rule with the following values:
   - **Rule Name**: `CrowdStrike`
   - **Layout to Display**: `CrowdStrike Endpoint Alert Layout`
   - **Alert Type**: `CrowdStrikeFalcon_XSIAM`

> ⚠️ **Important:** The `Alert Type` must exactly match the dataset name created by the integration:  
> `CrowdStrikeFalcon_XSIAM`

Once configured, alerts ingested from CrowdStrike Falcon will automatically use the custom layout defined in this pack.
