# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_issues_closed_issue import WebhookIssuesClosedIssue

class TestWebhookIssuesClosedIssue(unittest.TestCase):
    """WebhookIssuesClosedIssue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookIssuesClosedIssue:
        """Test WebhookIssuesClosedIssue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookIssuesClosedIssue`
        """
        model = WebhookIssuesClosedIssue()
        if include_optional:
            return WebhookIssuesClosedIssue(
                active_lock_reason = '',
                assignee = None,
                assignees = [
                    None
                    ],
                author_association = '',
                body = '',
                closed_at = '',
                comments = 56,
                comments_url = '',
                created_at = '',
                draft = True,
                events_url = '',
                html_url = '',
                id = 56,
                labels = [
                    None
                    ],
                labels_url = '',
                locked = True,
                milestone = None,
                node_id = '',
                number = 56,
                performed_via_github_app = None,
                pull_request = github_openapi.models.webhooks_issue_pull_request.webhooks_issue_pull_request(
                    diff_url = '', 
                    html_url = '', 
                    merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    patch_url = '', 
                    url = '', ),
                reactions = github_openapi.models.webhook_issue_comment_created_issue_all_of_reactions.webhook_issue_comment_created_issue_allOf_reactions(
                    +1 = 56, 
                    _1 = 56, 
                    confused = 56, 
                    eyes = 56, 
                    heart = 56, 
                    hooray = 56, 
                    laugh = 56, 
                    rocket = 56, 
                    total_count = 56, 
                    url = '', ),
                repository_url = '',
                sub_issues_summary = github_openapi.models.sub_issues_summary.Sub-issues Summary(
                    total = 56, 
                    completed = 56, 
                    percent_completed = 56, ),
                state = 'closed',
                state_reason = '',
                timeline_url = '',
                title = '',
                updated_at = '',
                url = '',
                user = github_openapi.models.webhook_issue_comment_deleted_issue_all_of_user.webhook_issue_comment_deleted_issue_allOf_user(
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
                    user_view_type = '', )
            )
        else:
            return WebhookIssuesClosedIssue(
                active_lock_reason = '',
                assignees = [
                    None
                    ],
                author_association = '',
                body = '',
                closed_at = '',
                comments = 56,
                comments_url = '',
                created_at = '',
                events_url = '',
                html_url = '',
                id = 56,
                labels_url = '',
                milestone = None,
                node_id = '',
                number = 56,
                reactions = github_openapi.models.webhook_issue_comment_created_issue_all_of_reactions.webhook_issue_comment_created_issue_allOf_reactions(
                    +1 = 56, 
                    _1 = 56, 
                    confused = 56, 
                    eyes = 56, 
                    heart = 56, 
                    hooray = 56, 
                    laugh = 56, 
                    rocket = 56, 
                    total_count = 56, 
                    url = '', ),
                repository_url = '',
                state = 'closed',
                title = '',
                updated_at = '',
                url = '',
                user = github_openapi.models.webhook_issue_comment_deleted_issue_all_of_user.webhook_issue_comment_deleted_issue_allOf_user(
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
        )
        """

    def testWebhookIssuesClosedIssue(self):
        """Test WebhookIssuesClosedIssue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()