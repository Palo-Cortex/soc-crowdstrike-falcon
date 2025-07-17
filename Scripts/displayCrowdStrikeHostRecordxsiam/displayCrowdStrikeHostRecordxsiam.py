import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
# This is a helper script designed to be used with the "[BETA] CrowdStrike Endpoint Alert Layout". This populates a dynamic section of the layout with the most current host record,
# as extracted from the CrowdStrike Falcon integration, using the cs-falcon-search-device command
#

def json_to_html_table(json_string):
    import json

    def format_value(value):
        if isinstance(value, str):
            try:
                value_dict = json.loads(value)
                if isinstance(value_dict, dict):
                    return "<br>".join(["<b>{}</b>: {}".format(k, v) for k, v in value_dict.items()])
            except ValueError:
                pass
        elif isinstance(value, dict):
            return "<br>".join(["<b>{}</b>: {}".format(k, v) for k, v in value.items()])
        return value

    # Convert the JSON string to a dictionary
    data = json.loads(json_string)

    # Initialize the HTML table with header row
    html_table = "<table style='border-collapse: collapse; width: 100%;'><tr style='background-color: #01cc66;'><td style='text-align: center; vertical-align: top; width: 20%;'>Field</td><td style='text-align: center; width: 80%;'>Value</td></tr>"

    # Populate table rows with data from the dictionary
    for key, value in data.items():
        key_html = "<span style='text-align: right; display: inline-block; font-weight: bold; vertical-align: top;'>{key}</span>".format(key=key + ":  ") if key != "Field" else "<span style='text-align: center; display: inline-block;'>{key}</span>".format(key=key)
        value_html = "<span style='display: inline-block;'>{}</span>".format(format_value(value))
        html_table += "<tr><td style='text-align: right; vertical-align: top;'>{}</td><td>{}</td></tr>".format(key_html, value_html)

    # Close the table tag
    html_table += "</table>"

    # Return the HTML table
    return html_table

def main():
    try:
        context_data = demisto.alert()
        agent_id = context_data['CustomFields']['agentid']
        hosts = execute_command('cs-falcon-search-device', {'ids': agent_id})
        for host_record in hosts:
            # host_record = hosts['resources'][0]
            host_record_string = json.dumps(host_record)
            html_record = json_to_html_table(host_record_string)
            return_results({
                'ContentsFormat': EntryFormat.HTML,
                'Type': EntryType.NOTE,
                'Contents': html_record,
            })

    except Exception as e:
        error_statement = "🔴 There has been an issue gathering host information. Please ensure the CrowdStrike Falcon automation integration is enabled.\n"
        error_statement += "\n\n\n Exception thrown: " + str(e)
        return_results(error_statement)

if __name__ in ("builtins", "__builtin__", "__main__"):
    main()
