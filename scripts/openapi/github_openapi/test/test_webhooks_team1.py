# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_team1 import WebhooksTeam1

class TestWebhooksTeam1(unittest.TestCase):
    """WebhooksTeam1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksTeam1:
        """Test WebhooksTeam1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksTeam1`
        """
        model = WebhooksTeam1()
        if include_optional:
            return WebhooksTeam1(
                deleted = True,
                description = '',
                html_url = '',
                id = 56,
                members_url = '',
                name = '',
                node_id = '',
                parent = github_openapi.models.webhooks_team_parent.webhooks_team_parent(
                    description = '', 
                    html_url = '', 
                    id = 56, 
                    members_url = '', 
                    name = '', 
                    node_id = '', 
                    permission = '', 
                    privacy = 'open', 
                    notification_setting = 'notifications_enabled', 
                    repositories_url = '', 
                    slug = '', 
                    url = '', ),
                permission = '',
                privacy = 'open',
                notification_setting = 'notifications_enabled',
                repositories_url = '',
                slug = '',
                url = ''
            )
        else:
            return WebhooksTeam1(
                id = 56,
                name = '',
        )
        """

    def testWebhooksTeam1(self):
        """Test WebhooksTeam1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
