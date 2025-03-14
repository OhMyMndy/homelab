# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_review import WebhooksReview

class TestWebhooksReview(unittest.TestCase):
    """WebhooksReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksReview:
        """Test WebhooksReview
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksReview`
        """
        model = WebhooksReview()
        if include_optional:
            return WebhooksReview(
                links = github_openapi.models.webhooks_review__links.webhooks_review__links(
                    html = github_openapi.models.link.Link(
                        href = '', ), 
                    pull_request = github_openapi.models.link.Link(
                        href = '', ), ),
                author_association = 'COLLABORATOR',
                body = '',
                commit_id = '',
                html_url = '',
                id = 56,
                node_id = '',
                pull_request_url = '',
                state = '',
                submitted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = github_openapi.models.user.User(
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
                    user_view_type = '', )
            )
        else:
            return WebhooksReview(
                links = github_openapi.models.webhooks_review__links.webhooks_review__links(
                    html = github_openapi.models.link.Link(
                        href = '', ), 
                    pull_request = github_openapi.models.link.Link(
                        href = '', ), ),
                author_association = 'COLLABORATOR',
                body = '',
                commit_id = '',
                html_url = '',
                id = 56,
                node_id = '',
                pull_request_url = '',
                state = '',
                submitted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = github_openapi.models.user.User(
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
        )
        """

    def testWebhooksReview(self):
        """Test WebhooksReview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
