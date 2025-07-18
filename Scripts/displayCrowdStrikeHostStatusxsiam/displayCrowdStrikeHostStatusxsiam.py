import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
# This is a helper script designed to be used with the "[BETA] CrowdStrike Endpoint Alert Layout". This populates a dynamic section of the layout with the most current host record,
# as extracted from the CrowdStrike Falcon integration, using the cs-falcon-search-device command
#

def main():
    try:
        context_data = demisto.alert()
        agent_id = context_data['CustomFields']['agentid']
        hosts = execute_command('cs-falcon-search-device', {'ids': agent_id})
        for host_record in hosts:
            host_name = host_record['resources'][0]['hostname']
            host_status = host_record['resources'][0]['status']
            if host_status == "normal":
                host_status = "🟢 Online"
            elif host_status == "containment_pending":
                host_status = "🟡 Pending Containment"
            elif host_status == "lift_containment_pending":
                host_status = "🟡 Lifting Containment"
            elif host_status == "contained":
                host_status = "🔴 Contained"
            else:
                host_status = "🟤 Unknown or Offline"
            host_current_local_ip = host_record['resources'][0]['local_ip']
            host_current_external_ip = host_record['resources'][0]['external_ip']

        # Seems to be missing in some CRWD tenants
        try:
            host_os = host_record['resources'][0]['os_product_name']
        except Exception as e:
            host_os = "unknown"

        # Seems to be missing in some CRWD tenants
        try:
            last_user = host_record['resources'][0]['last_login_user']
        except Exception as e:
            last_user = "not-available"

        host_snippet = "Hostname: " + host_name + "\n" + "Status: " + host_status + "\n" + "Current Local IP: " + host_current_local_ip + "\n" + "Current External IP: " + host_current_external_ip + "\n" + "OS: " + host_os + "\n" + "Last Logged In User: " + last_user
        return_results(host_snippet)

    except Exception as e:
        error_statement = "🔴 There has been an issue gathering host status. Please ensure the CrowdStrike Falcon automation integration is enabled.\n"
        error_statement += "\n\n\n\n\n\nException thrown: " + str(e)
        return_results(error_statement)

if __name__ in ("builtins", "__builtin__", "__main__"):
    main()
