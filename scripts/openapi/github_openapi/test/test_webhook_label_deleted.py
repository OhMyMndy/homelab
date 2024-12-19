# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_label_deleted import WebhookLabelDeleted

class TestWebhookLabelDeleted(unittest.TestCase):
    """WebhookLabelDeleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookLabelDeleted:
        """Test WebhookLabelDeleted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookLabelDeleted`
        """
        model = WebhookLabelDeleted()
        if include_optional:
            return WebhookLabelDeleted(
                action = 'deleted',
                enterprise = github_openapi.models.enterprise.Enterprise(
                    description = '', 
                    html_url = 'https://github.com/enterprises/octo-business', 
                    website_url = '', 
                    id = 42, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Octo Business', 
                    slug = 'octo-business', 
                    created_at = '2019-01-26T19:01:12Z', 
                    updated_at = '2019-01-26T19:14:43Z', 
                    avatar_url = '', ),
                installation = github_openapi.models.simple_installation.Simple Installation(
                    id = 1, 
                    node_id = 'MDQ6VXNlcjU4MzIzMQ==', ),
                label = github_openapi.models.label.Label(
                    color = '', 
                    default = True, 
                    description = '', 
                    id = 56, 
                    name = '', 
                    node_id = '', 
                    url = '', ),
                organization = github_openapi.models.organization_simple.Organization Simple(
                    login = 'github', 
                    id = 1, 
                    node_id = 'MDEyOk9yZ2FuaXphdGlvbjE=', 
                    url = 'https://api.github.com/orgs/github', 
                    repos_url = 'https://api.github.com/orgs/github/repos', 
                    events_url = 'https://api.github.com/orgs/github/events', 
                    hooks_url = 'https://api.github.com/orgs/github/hooks', 
                    issues_url = 'https://api.github.com/orgs/github/issues', 
                    members_url = 'https://api.github.com/orgs/github/members{/member}', 
                    public_members_url = 'https://api.github.com/orgs/github/public_members{/member}', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    description = 'A great organization', ),
                repository = github_openapi.models.repository.Repository(
                    id = 42, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Team Environment', 
                    full_name = 'octocat/Hello-World', 
                    license = github_openapi.models.license_simple.License Simple(
                        key = 'mit', 
                        name = 'MIT License', 
                        url = 'https://api.github.com/licenses/mit', 
                        spdx_id = 'MIT', 
                        node_id = 'MDc6TGljZW5zZW1pdA==', 
                        html_url = '', ), 
                    organization = github_openapi.models.simple_user.Simple User(
                        name = '', 
                        email = '', 
                        login = 'octocat', 
                        id = 1, 
                        node_id = 'MDQ6VXNlcjE=', 
                        avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                        gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                        url = 'https://api.github.com/users/octocat', 
                        html_url = 'https://github.com/octocat', 
                        followers_url = 'https://api.github.com/users/octocat/followers', 
                        following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                        gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                        starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                        subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                        organizations_url = 'https://api.github.com/users/octocat/orgs', 
                        repos_url = 'https://api.github.com/users/octocat/repos', 
                        events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                        received_events_url = 'https://api.github.com/users/octocat/received_events', 
                        type = 'User', 
                        site_admin = True, 
                        starred_at = '"2020-07-09T00:17:55Z"', 
                        user_view_type = 'public', ), 
                    forks = 56, 
                    permissions = github_openapi.models.repository_permissions.repository_permissions(
                        admin = True, 
                        pull = True, 
                        triage = True, 
                        push = True, 
                        maintain = True, ), 
                    owner = github_openapi.models.simple_user.Simple User(
                        name = '', 
                        email = '', 
                        login = 'octocat', 
                        id = 1, 
                        node_id = 'MDQ6VXNlcjE=', 
                        avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                        gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                        url = 'https://api.github.com/users/octocat', 
                        html_url = 'https://github.com/octocat', 
                        followers_url = 'https://api.github.com/users/octocat/followers', 
                        following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                        gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                        starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                        subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                        organizations_url = 'https://api.github.com/users/octocat/orgs', 
                        repos_url = 'https://api.github.com/users/octocat/repos', 
                        events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                        received_events_url = 'https://api.github.com/users/octocat/received_events', 
                        type = 'User', 
                        site_admin = True, 
                        starred_at = '"2020-07-09T00:17:55Z"', 
                        user_view_type = 'public', ), 
                    private = True, 
                    html_url = 'https://github.com/octocat/Hello-World', 
                    description = 'This your first repo!', 
                    fork = True, 
                    url = 'https://api.github.com/repos/octocat/Hello-World', 
                    archive_url = 'http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}', 
                    assignees_url = 'http://api.github.com/repos/octocat/Hello-World/assignees{/user}', 
                    blobs_url = 'http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}', 
                    branches_url = 'http://api.github.com/repos/octocat/Hello-World/branches{/branch}', 
                    collaborators_url = 'http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}', 
                    comments_url = 'http://api.github.com/repos/octocat/Hello-World/comments{/number}', 
                    commits_url = 'http://api.github.com/repos/octocat/Hello-World/commits{/sha}', 
                    compare_url = 'http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}', 
                    contents_url = 'http://api.github.com/repos/octocat/Hello-World/contents/{+path}', 
                    contributors_url = 'http://api.github.com/repos/octocat/Hello-World/contributors', 
                    deployments_url = 'http://api.github.com/repos/octocat/Hello-World/deployments', 
                    downloads_url = 'http://api.github.com/repos/octocat/Hello-World/downloads', 
                    events_url = 'http://api.github.com/repos/octocat/Hello-World/events', 
                    forks_url = 'http://api.github.com/repos/octocat/Hello-World/forks', 
                    git_commits_url = 'http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}', 
                    git_refs_url = 'http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}', 
                    git_tags_url = 'http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}', 
                    git_url = 'git:github.com/octocat/Hello-World.git', 
                    issue_comment_url = 'http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}', 
                    issue_events_url = 'http://api.github.com/repos/octocat/Hello-World/issues/events{/number}', 
                    issues_url = 'http://api.github.com/repos/octocat/Hello-World/issues{/number}', 
                    keys_url = 'http://api.github.com/repos/octocat/Hello-World/keys{/key_id}', 
                    labels_url = 'http://api.github.com/repos/octocat/Hello-World/labels{/name}', 
                    languages_url = 'http://api.github.com/repos/octocat/Hello-World/languages', 
                    merges_url = 'http://api.github.com/repos/octocat/Hello-World/merges', 
                    milestones_url = 'http://api.github.com/repos/octocat/Hello-World/milestones{/number}', 
                    notifications_url = 'http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}', 
                    pulls_url = 'http://api.github.com/repos/octocat/Hello-World/pulls{/number}', 
                    releases_url = 'http://api.github.com/repos/octocat/Hello-World/releases{/id}', 
                    ssh_url = 'git@github.com:octocat/Hello-World.git', 
                    stargazers_url = 'http://api.github.com/repos/octocat/Hello-World/stargazers', 
                    statuses_url = 'http://api.github.com/repos/octocat/Hello-World/statuses/{sha}', 
                    subscribers_url = 'http://api.github.com/repos/octocat/Hello-World/subscribers', 
                    subscription_url = 'http://api.github.com/repos/octocat/Hello-World/subscription', 
                    tags_url = 'http://api.github.com/repos/octocat/Hello-World/tags', 
                    teams_url = 'http://api.github.com/repos/octocat/Hello-World/teams', 
                    trees_url = 'http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}', 
                    clone_url = 'https://github.com/octocat/Hello-World.git', 
                    mirror_url = 'git:git.example.com/octocat/Hello-World', 
                    hooks_url = 'http://api.github.com/repos/octocat/Hello-World/hooks', 
                    svn_url = 'https://svn.github.com/octocat/Hello-World', 
                    homepage = 'https://github.com', 
                    language = '', 
                    forks_count = 9, 
                    stargazers_count = 80, 
                    watchers_count = 80, 
                    size = 108, 
                    default_branch = 'master', 
                    open_issues_count = 0, 
                    is_template = True, 
                    topics = [
                        ''
                        ], 
                    custom_properties = { }, 
                    has_issues = True, 
                    has_projects = True, 
                    has_wiki = True, 
                    has_pages = True, 
                    has_downloads = True, 
                    has_discussions = True, 
                    archived = True, 
                    disabled = True, 
                    visibility = 'public', 
                    pushed_at = '2011-01-26T19:06:43Z', 
                    created_at = '2011-01-26T19:01:12Z', 
                    updated_at = '2011-01-26T19:14:43Z', 
                    allow_rebase_merge = True, 
                    template_repository = github_openapi.models.repository_webhooks_template_repository.repository_webhooks_template_repository(
                        id = 56, 
                        node_id = '', 
                        name = '', 
                        full_name = '', 
                        private = True, 
                        html_url = '', 
                        description = '', 
                        fork = True, 
                        url = '', 
                        archive_url = '', 
                        assignees_url = '', 
                        blobs_url = '', 
                        branches_url = '', 
                        collaborators_url = '', 
                        comments_url = '', 
                        commits_url = '', 
                        compare_url = '', 
                        contents_url = '', 
                        contributors_url = '', 
                        deployments_url = '', 
                        downloads_url = '', 
                        events_url = '', 
                        forks_url = '', 
                        git_commits_url = '', 
                        git_refs_url = '', 
                        git_tags_url = '', 
                        git_url = '', 
                        issue_comment_url = '', 
                        issue_events_url = '', 
                        issues_url = '', 
                        keys_url = '', 
                        labels_url = '', 
                        languages_url = '', 
                        merges_url = '', 
                        milestones_url = '', 
                        notifications_url = '', 
                        pulls_url = '', 
                        releases_url = '', 
                        ssh_url = '', 
                        stargazers_url = '', 
                        statuses_url = '', 
                        subscribers_url = '', 
                        subscription_url = '', 
                        tags_url = '', 
                        teams_url = '', 
                        trees_url = '', 
                        clone_url = '', 
                        mirror_url = '', 
                        hooks_url = '', 
                        svn_url = '', 
                        homepage = '', 
                        language = '', 
                        forks_count = 56, 
                        stargazers_count = 56, 
                        watchers_count = 56, 
                        size = 56, 
                        default_branch = '', 
                        open_issues_count = 56, 
                        is_template = True, 
                        has_issues = True, 
                        has_projects = True, 
                        has_wiki = True, 
                        has_pages = True, 
                        has_downloads = True, 
                        archived = True, 
                        disabled = True, 
                        visibility = '', 
                        pushed_at = '', 
                        created_at = '', 
                        updated_at = '', 
                        allow_rebase_merge = True, 
                        temp_clone_token = '', 
                        allow_squash_merge = True, 
                        allow_auto_merge = True, 
                        delete_branch_on_merge = True, 
                        allow_update_branch = True, 
                        use_squash_pr_title_as_default = True, 
                        squash_merge_commit_title = 'PR_TITLE', 
                        squash_merge_commit_message = 'PR_BODY', 
                        merge_commit_title = 'PR_TITLE', 
                        merge_commit_message = 'PR_BODY', 
                        allow_merge_commit = True, 
                        subscribers_count = 56, 
                        network_count = 56, ), 
                    temp_clone_token = '', 
                    allow_squash_merge = True, 
                    allow_auto_merge = False, 
                    delete_branch_on_merge = False, 
                    allow_update_branch = False, 
                    use_squash_pr_title_as_default = True, 
                    squash_merge_commit_title = 'PR_TITLE', 
                    squash_merge_commit_message = 'PR_BODY', 
                    merge_commit_title = 'PR_TITLE', 
                    merge_commit_message = 'PR_BODY', 
                    allow_merge_commit = True, 
                    allow_forking = True, 
                    web_commit_signoff_required = True, 
                    subscribers_count = 56, 
                    network_count = 56, 
                    open_issues = 56, 
                    watchers = 56, 
                    master_branch = '', 
                    starred_at = '"2020-07-09T00:17:42Z"', 
                    anonymous_access_enabled = True, ),
                sender = github_openapi.models.simple_user.Simple User(
                    name = '', 
                    email = '', 
                    login = 'octocat', 
                    id = 1, 
                    node_id = 'MDQ6VXNlcjE=', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                    url = 'https://api.github.com/users/octocat', 
                    html_url = 'https://github.com/octocat', 
                    followers_url = 'https://api.github.com/users/octocat/followers', 
                    following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                    gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                    starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                    subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                    organizations_url = 'https://api.github.com/users/octocat/orgs', 
                    repos_url = 'https://api.github.com/users/octocat/repos', 
                    events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                    received_events_url = 'https://api.github.com/users/octocat/received_events', 
                    type = 'User', 
                    site_admin = True, 
                    starred_at = '"2020-07-09T00:17:55Z"', 
                    user_view_type = 'public', )
            )
        else:
            return WebhookLabelDeleted(
                action = 'deleted',
                label = github_openapi.models.label.Label(
                    color = '', 
                    default = True, 
                    description = '', 
                    id = 56, 
                    name = '', 
                    node_id = '', 
                    url = '', ),
                repository = github_openapi.models.repository.Repository(
                    id = 42, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Team Environment', 
                    full_name = 'octocat/Hello-World', 
                    license = github_openapi.models.license_simple.License Simple(
                        key = 'mit', 
                        name = 'MIT License', 
                        url = 'https://api.github.com/licenses/mit', 
                        spdx_id = 'MIT', 
                        node_id = 'MDc6TGljZW5zZW1pdA==', 
                        html_url = '', ), 
                    organization = github_openapi.models.simple_user.Simple User(
                        name = '', 
                        email = '', 
                        login = 'octocat', 
                        id = 1, 
                        node_id = 'MDQ6VXNlcjE=', 
                        avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                        gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                        url = 'https://api.github.com/users/octocat', 
                        html_url = 'https://github.com/octocat', 
                        followers_url = 'https://api.github.com/users/octocat/followers', 
                        following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                        gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                        starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                        subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                        organizations_url = 'https://api.github.com/users/octocat/orgs', 
                        repos_url = 'https://api.github.com/users/octocat/repos', 
                        events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                        received_events_url = 'https://api.github.com/users/octocat/received_events', 
                        type = 'User', 
                        site_admin = True, 
                        starred_at = '"2020-07-09T00:17:55Z"', 
                        user_view_type = 'public', ), 
                    forks = 56, 
                    permissions = github_openapi.models.repository_permissions.repository_permissions(
                        admin = True, 
                        pull = True, 
                        triage = True, 
                        push = True, 
                        maintain = True, ), 
                    owner = github_openapi.models.simple_user.Simple User(
                        name = '', 
                        email = '', 
                        login = 'octocat', 
                        id = 1, 
                        node_id = 'MDQ6VXNlcjE=', 
                        avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                        gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                        url = 'https://api.github.com/users/octocat', 
                        html_url = 'https://github.com/octocat', 
                        followers_url = 'https://api.github.com/users/octocat/followers', 
                        following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                        gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                        starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                        subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                        organizations_url = 'https://api.github.com/users/octocat/orgs', 
                        repos_url = 'https://api.github.com/users/octocat/repos', 
                        events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                        received_events_url = 'https://api.github.com/users/octocat/received_events', 
                        type = 'User', 
                        site_admin = True, 
                        starred_at = '"2020-07-09T00:17:55Z"', 
                        user_view_type = 'public', ), 
                    private = True, 
                    html_url = 'https://github.com/octocat/Hello-World', 
                    description = 'This your first repo!', 
                    fork = True, 
                    url = 'https://api.github.com/repos/octocat/Hello-World', 
                    archive_url = 'http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}', 
                    assignees_url = 'http://api.github.com/repos/octocat/Hello-World/assignees{/user}', 
                    blobs_url = 'http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}', 
                    branches_url = 'http://api.github.com/repos/octocat/Hello-World/branches{/branch}', 
                    collaborators_url = 'http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}', 
                    comments_url = 'http://api.github.com/repos/octocat/Hello-World/comments{/number}', 
                    commits_url = 'http://api.github.com/repos/octocat/Hello-World/commits{/sha}', 
                    compare_url = 'http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}', 
                    contents_url = 'http://api.github.com/repos/octocat/Hello-World/contents/{+path}', 
                    contributors_url = 'http://api.github.com/repos/octocat/Hello-World/contributors', 
                    deployments_url = 'http://api.github.com/repos/octocat/Hello-World/deployments', 
                    downloads_url = 'http://api.github.com/repos/octocat/Hello-World/downloads', 
                    events_url = 'http://api.github.com/repos/octocat/Hello-World/events', 
                    forks_url = 'http://api.github.com/repos/octocat/Hello-World/forks', 
                    git_commits_url = 'http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}', 
                    git_refs_url = 'http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}', 
                    git_tags_url = 'http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}', 
                    git_url = 'git:github.com/octocat/Hello-World.git', 
                    issue_comment_url = 'http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}', 
                    issue_events_url = 'http://api.github.com/repos/octocat/Hello-World/issues/events{/number}', 
                    issues_url = 'http://api.github.com/repos/octocat/Hello-World/issues{/number}', 
                    keys_url = 'http://api.github.com/repos/octocat/Hello-World/keys{/key_id}', 
                    labels_url = 'http://api.github.com/repos/octocat/Hello-World/labels{/name}', 
                    languages_url = 'http://api.github.com/repos/octocat/Hello-World/languages', 
                    merges_url = 'http://api.github.com/repos/octocat/Hello-World/merges', 
                    milestones_url = 'http://api.github.com/repos/octocat/Hello-World/milestones{/number}', 
                    notifications_url = 'http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}', 
                    pulls_url = 'http://api.github.com/repos/octocat/Hello-World/pulls{/number}', 
                    releases_url = 'http://api.github.com/repos/octocat/Hello-World/releases{/id}', 
                    ssh_url = 'git@github.com:octocat/Hello-World.git', 
                    stargazers_url = 'http://api.github.com/repos/octocat/Hello-World/stargazers', 
                    statuses_url = 'http://api.github.com/repos/octocat/Hello-World/statuses/{sha}', 
                    subscribers_url = 'http://api.github.com/repos/octocat/Hello-World/subscribers', 
                    subscription_url = 'http://api.github.com/repos/octocat/Hello-World/subscription', 
                    tags_url = 'http://api.github.com/repos/octocat/Hello-World/tags', 
                    teams_url = 'http://api.github.com/repos/octocat/Hello-World/teams', 
                    trees_url = 'http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}', 
                    clone_url = 'https://github.com/octocat/Hello-World.git', 
                    mirror_url = 'git:git.example.com/octocat/Hello-World', 
                    hooks_url = 'http://api.github.com/repos/octocat/Hello-World/hooks', 
                    svn_url = 'https://svn.github.com/octocat/Hello-World', 
                    homepage = 'https://github.com', 
                    language = '', 
                    forks_count = 9, 
                    stargazers_count = 80, 
                    watchers_count = 80, 
                    size = 108, 
                    default_branch = 'master', 
                    open_issues_count = 0, 
                    is_template = True, 
                    topics = [
                        ''
                        ], 
                    custom_properties = { }, 
                    has_issues = True, 
                    has_projects = True, 
                    has_wiki = True, 
                    has_pages = True, 
                    has_downloads = True, 
                    has_discussions = True, 
                    archived = True, 
                    disabled = True, 
                    visibility = 'public', 
                    pushed_at = '2011-01-26T19:06:43Z', 
                    created_at = '2011-01-26T19:01:12Z', 
                    updated_at = '2011-01-26T19:14:43Z', 
                    allow_rebase_merge = True, 
                    template_repository = github_openapi.models.repository_webhooks_template_repository.repository_webhooks_template_repository(
                        id = 56, 
                        node_id = '', 
                        name = '', 
                        full_name = '', 
                        private = True, 
                        html_url = '', 
                        description = '', 
                        fork = True, 
                        url = '', 
                        archive_url = '', 
                        assignees_url = '', 
                        blobs_url = '', 
                        branches_url = '', 
                        collaborators_url = '', 
                        comments_url = '', 
                        commits_url = '', 
                        compare_url = '', 
                        contents_url = '', 
                        contributors_url = '', 
                        deployments_url = '', 
                        downloads_url = '', 
                        events_url = '', 
                        forks_url = '', 
                        git_commits_url = '', 
                        git_refs_url = '', 
                        git_tags_url = '', 
                        git_url = '', 
                        issue_comment_url = '', 
                        issue_events_url = '', 
                        issues_url = '', 
                        keys_url = '', 
                        labels_url = '', 
                        languages_url = '', 
                        merges_url = '', 
                        milestones_url = '', 
                        notifications_url = '', 
                        pulls_url = '', 
                        releases_url = '', 
                        ssh_url = '', 
                        stargazers_url = '', 
                        statuses_url = '', 
                        subscribers_url = '', 
                        subscription_url = '', 
                        tags_url = '', 
                        teams_url = '', 
                        trees_url = '', 
                        clone_url = '', 
                        mirror_url = '', 
                        hooks_url = '', 
                        svn_url = '', 
                        homepage = '', 
                        language = '', 
                        forks_count = 56, 
                        stargazers_count = 56, 
                        watchers_count = 56, 
                        size = 56, 
                        default_branch = '', 
                        open_issues_count = 56, 
                        is_template = True, 
                        has_issues = True, 
                        has_projects = True, 
                        has_wiki = True, 
                        has_pages = True, 
                        has_downloads = True, 
                        archived = True, 
                        disabled = True, 
                        visibility = '', 
                        pushed_at = '', 
                        created_at = '', 
                        updated_at = '', 
                        allow_rebase_merge = True, 
                        temp_clone_token = '', 
                        allow_squash_merge = True, 
                        allow_auto_merge = True, 
                        delete_branch_on_merge = True, 
                        allow_update_branch = True, 
                        use_squash_pr_title_as_default = True, 
                        squash_merge_commit_title = 'PR_TITLE', 
                        squash_merge_commit_message = 'PR_BODY', 
                        merge_commit_title = 'PR_TITLE', 
                        merge_commit_message = 'PR_BODY', 
                        allow_merge_commit = True, 
                        subscribers_count = 56, 
                        network_count = 56, ), 
                    temp_clone_token = '', 
                    allow_squash_merge = True, 
                    allow_auto_merge = False, 
                    delete_branch_on_merge = False, 
                    allow_update_branch = False, 
                    use_squash_pr_title_as_default = True, 
                    squash_merge_commit_title = 'PR_TITLE', 
                    squash_merge_commit_message = 'PR_BODY', 
                    merge_commit_title = 'PR_TITLE', 
                    merge_commit_message = 'PR_BODY', 
                    allow_merge_commit = True, 
                    allow_forking = True, 
                    web_commit_signoff_required = True, 
                    subscribers_count = 56, 
                    network_count = 56, 
                    open_issues = 56, 
                    watchers = 56, 
                    master_branch = '', 
                    starred_at = '"2020-07-09T00:17:42Z"', 
                    anonymous_access_enabled = True, ),
                sender = github_openapi.models.simple_user.Simple User(
                    name = '', 
                    email = '', 
                    login = 'octocat', 
                    id = 1, 
                    node_id = 'MDQ6VXNlcjE=', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                    url = 'https://api.github.com/users/octocat', 
                    html_url = 'https://github.com/octocat', 
                    followers_url = 'https://api.github.com/users/octocat/followers', 
                    following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                    gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                    starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                    subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                    organizations_url = 'https://api.github.com/users/octocat/orgs', 
                    repos_url = 'https://api.github.com/users/octocat/repos', 
                    events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                    received_events_url = 'https://api.github.com/users/octocat/received_events', 
                    type = 'User', 
                    site_admin = True, 
                    starred_at = '"2020-07-09T00:17:55Z"', 
                    user_view_type = 'public', ),
        )
        """

    def testWebhookLabelDeleted(self):
        """Test WebhookLabelDeleted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
