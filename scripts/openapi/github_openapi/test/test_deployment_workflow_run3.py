# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.deployment_workflow_run3 import DeploymentWorkflowRun3

class TestDeploymentWorkflowRun3(unittest.TestCase):
    """DeploymentWorkflowRun3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentWorkflowRun3:
        """Test DeploymentWorkflowRun3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentWorkflowRun3`
        """
        model = DeploymentWorkflowRun3()
        if include_optional:
            return DeploymentWorkflowRun3(
                actor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                artifacts_url = '',
                cancel_url = '',
                check_suite_id = 56,
                check_suite_node_id = '',
                check_suite_url = '',
                conclusion = 'success',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                event = '',
                head_branch = '',
                head_commit = github_openapi.models.head_commit.head_commit(),
                head_repository = github_openapi.models.deployment_workflow_run_1_head_repository.Deployment_Workflow_Run_1_head_repository(
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
                    description = '', 
                    downloads_url = '', 
                    events_url = '', 
                    fork = True, 
                    forks_url = '', 
                    full_name = '', 
                    git_commits_url = '', 
                    git_refs_url = '', 
                    git_tags_url = '', 
                    hooks_url = '', 
                    html_url = '', 
                    id = 56, 
                    issue_comment_url = '', 
                    issue_events_url = '', 
                    issues_url = '', 
                    keys_url = '', 
                    labels_url = '', 
                    languages_url = '', 
                    merges_url = '', 
                    milestones_url = '', 
                    name = '', 
                    node_id = '', 
                    notifications_url = '', 
                    owner = github_openapi.models.webhooks_sponsorship_maintainer.webhooks_sponsorship_maintainer(
                        avatar_url = '', 
                        events_url = '', 
                        followers_url = '', 
                        following_url = '', 
                        gists_url = '', 
                        gravatar_id = '', 
                        html_url = '', 
                        id = 56, 
                        login = '', 
                        node_id = '', 
                        organizations_url = '', 
                        received_events_url = '', 
                        repos_url = '', 
                        site_admin = True, 
                        starred_url = '', 
                        subscriptions_url = '', 
                        type = '', 
                        url = '', 
                        user_view_type = '', ), 
                    private = True, 
                    pulls_url = '', 
                    releases_url = '', 
                    stargazers_url = '', 
                    statuses_url = '', 
                    subscribers_url = '', 
                    subscription_url = '', 
                    tags_url = '', 
                    teams_url = '', 
                    trees_url = '', 
                    url = '', ),
                head_sha = '',
                html_url = '',
                id = 56,
                jobs_url = '',
                logs_url = '',
                name = '',
                node_id = '',
                path = '',
                previous_attempt_url = '',
                pull_requests = [
                    github_openapi.models.check_run_pull_request.Check Run Pull Request(
                        base = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                            ref = '', 
                            repo = github_openapi.models.repo_ref.Repo Ref(
                                id = 56, 
                                name = '', 
                                url = '', ), 
                            sha = '', ), 
                        head = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                            ref = '', 
                            repo = github_openapi.models.repo_ref.Repo Ref(
                                id = 56, 
                                name = '', 
                                url = '', ), 
                            sha = '', ), 
                        id = 56, 
                        number = 56, 
                        url = '', )
                    ],
                referenced_workflows = [
                    github_openapi.models.deployment_workflow_run_referenced_workflows_inner.Deployment_Workflow_Run_referenced_workflows_inner(
                        path = '', 
                        ref = '', 
                        sha = '', )
                    ],
                repository = github_openapi.models.deployment_workflow_run_1_head_repository.Deployment_Workflow_Run_1_head_repository(
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
                    description = '', 
                    downloads_url = '', 
                    events_url = '', 
                    fork = True, 
                    forks_url = '', 
                    full_name = '', 
                    git_commits_url = '', 
                    git_refs_url = '', 
                    git_tags_url = '', 
                    hooks_url = '', 
                    html_url = '', 
                    id = 56, 
                    issue_comment_url = '', 
                    issue_events_url = '', 
                    issues_url = '', 
                    keys_url = '', 
                    labels_url = '', 
                    languages_url = '', 
                    merges_url = '', 
                    milestones_url = '', 
                    name = '', 
                    node_id = '', 
                    notifications_url = '', 
                    owner = github_openapi.models.webhooks_sponsorship_maintainer.webhooks_sponsorship_maintainer(
                        avatar_url = '', 
                        events_url = '', 
                        followers_url = '', 
                        following_url = '', 
                        gists_url = '', 
                        gravatar_id = '', 
                        html_url = '', 
                        id = 56, 
                        login = '', 
                        node_id = '', 
                        organizations_url = '', 
                        received_events_url = '', 
                        repos_url = '', 
                        site_admin = True, 
                        starred_url = '', 
                        subscriptions_url = '', 
                        type = '', 
                        url = '', 
                        user_view_type = '', ), 
                    private = True, 
                    pulls_url = '', 
                    releases_url = '', 
                    stargazers_url = '', 
                    statuses_url = '', 
                    subscribers_url = '', 
                    subscription_url = '', 
                    tags_url = '', 
                    teams_url = '', 
                    trees_url = '', 
                    url = '', ),
                rerun_url = '',
                run_attempt = 56,
                run_number = 56,
                run_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'requested',
                triggering_actor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                workflow_id = 56,
                workflow_url = '',
                display_title = ''
            )
        else:
            return DeploymentWorkflowRun3(
                actor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                check_suite_id = 56,
                check_suite_node_id = '',
                conclusion = 'success',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                event = '',
                head_branch = '',
                head_sha = '',
                html_url = '',
                id = 56,
                name = '',
                node_id = '',
                path = '',
                pull_requests = [
                    github_openapi.models.check_run_pull_request.Check Run Pull Request(
                        base = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                            ref = '', 
                            repo = github_openapi.models.repo_ref.Repo Ref(
                                id = 56, 
                                name = '', 
                                url = '', ), 
                            sha = '', ), 
                        head = github_openapi.models.check_run_pull_request_base.Check_Run_Pull_Request_base(
                            ref = '', 
                            repo = github_openapi.models.repo_ref.Repo Ref(
                                id = 56, 
                                name = '', 
                                url = '', ), 
                            sha = '', ), 
                        id = 56, 
                        number = 56, 
                        url = '', )
                    ],
                run_attempt = 56,
                run_number = 56,
                run_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'requested',
                triggering_actor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                workflow_id = 56,
                display_title = '',
        )
        """

    def testDeploymentWorkflowRun3(self):
        """Test DeploymentWorkflowRun3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
