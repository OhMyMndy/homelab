# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_member_added_changes import WebhookMemberAddedChanges

class TestWebhookMemberAddedChanges(unittest.TestCase):
    """WebhookMemberAddedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMemberAddedChanges:
        """Test WebhookMemberAddedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMemberAddedChanges`
        """
        model = WebhookMemberAddedChanges()
        if include_optional:
            return WebhookMemberAddedChanges(
                permission = github_openapi.models.webhook_member_added_changes_permission.webhook_member_added_changes_permission(
                    to = 'write', ),
                role_name = github_openapi.models.webhook_member_added_changes_role_name.webhook_member_added_changes_role_name(
                    to = '', )
            )
        else:
            return WebhookMemberAddedChanges(
        )
        """

    def testWebhookMemberAddedChanges(self):
        """Test WebhookMemberAddedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()