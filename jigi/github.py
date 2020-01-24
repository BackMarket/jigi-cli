from github import Github


def create_client(token):
    return Github(token)


def search_issues(client, repo, *args):
    search_expr = "repo:{} {}".format(repo, " ".join(args))
    return client.search_issues(search_expr, sort="created", order="desc")


def get_pull_requests(client, repo, *args):
    results = search_issues(client, repo, "is:pr", *args)
    return [pr.as_pull_request() for pr in results]


def get_pull_requests_opened(client, repo, *args):
    return get_pull_requests(client, repo, "is:open", *args)
