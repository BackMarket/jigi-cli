from jira import JIRA

JIRA_DEFAULT_JQL_ISSUES = "assignee = currentUser() AND sprint in openSprints()"
JIRA_SUMMARY_MAX_LENGTH = 80


def create_client(api_root, login, token):
    options = {"rest_api_version": 3}
    return JIRA(server=api_root, basic_auth=(login, token), options=options)


def get_issues(client, jql_query=JIRA_DEFAULT_JQL_ISSUES):
    return client.search_issues(jql_query)


def get_issue_summary_truncated(issue):
    summary = issue.fields.summary
    return summary if len(summary) <= JIRA_SUMMARY_MAX_LENGTH else summary[: JIRA_SUMMARY_MAX_LENGTH - 3] + "..."


def get_issue_link(jira_client, issue):
    return "{}/browse/{}".format(jira_client.server_info()["baseUrl"], issue.key)
