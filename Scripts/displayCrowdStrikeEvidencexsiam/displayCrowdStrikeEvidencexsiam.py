import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
# This is a helper script designed to be used with the "[BETA] CrowdStrike Endpoint Alert Layout". This populates a dynamic section of the layout with the raw alert data from CRWD


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

    # Fetch data from context
    try:
        context_data = demisto.alert()
                # Extract the specific field that contains the CrowdStrike "alert_data" raw event JSON
        context_data = context_data['rawJSON']
        if context_data:
            table = json_to_html_table(context_data)

            return_results({
                'ContentsFormat': EntryFormat.HTML,
                'Type': EntryType.NOTE,
                'Contents': table,
            })

    except Exception as e:
        error_statement = "There seems to be an issue rendering this field.\n\nContents of this are controlled by the Script 'displayCrowdStrikeEvidence_xsiam' which can be located under Investigation & Response -> Automation -> Scripts.\nThis script pulls data from the *rawevent key in the alert/issue context - if that key is improperly populated, or missing, nothing will be displayed here. Please review the correlation rule, alert mapping and CrowdStrike data set."
        error_statement += "\n\nException thrown by script: " + str(e)
        return_results(error_statement)

if __name__ in ("builtins", "__builtin__", "__main__"):
    main()

