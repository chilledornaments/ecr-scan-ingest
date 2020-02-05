import json
import requests

from os import environ


def slack_alert(repo_name, findings):

    if len(findings) > 0:

        h = {"Content-Type": "application/json"}
        m = {
            "channel": environ['SLACK_CHANNEL'],
            "icon_emoji": environ['SLACK_EMOJI'],
            "username": environ['SLACK_USERNAME'],
            "attachments": [{
                "title": "ECR Scan Findings",
                "color": "Danger",
                "fallback": f"ECR scan found issues in {repo_name}",
                "text": f"ECR scan found {findings['CRITICAL']} CRITICAL and {findings['WARNING']} WARNING issues in {repo_name}"
            }]
        }

        requests.post(environ['SLACK_WEBHOOK'], data=json.dumps(m), headers=h)


    return "Ok"



def lambda_handler(event, context):

    findings_json = {}

    #event_json = json.loads(event)

    repo = event['detail']['repository-name']

    if event['detail']['scan-status'] != "COMPLETE":
        print(f"Scan status {event['detail']['scan-status']}")
        return "Ok"

    findings = event['detail'].get('finding-severity-counts')

    if findings is None:
        print("No findings")
        pass

    else:
        if findings.get("CRITICAL") is not None:
            findings_json['CRITICAL'] = findings.get("CRITICAL")
        if findings.get("MEDIUM") is not None:
            findings_json['CRITICAL'] = findings.get("CRITICAL")

    slack_alert(repo, findings_json)
