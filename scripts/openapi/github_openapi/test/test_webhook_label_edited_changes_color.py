# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_label_edited_changes_color import WebhookLabelEditedChangesColor

class TestWebhookLabelEditedChangesColor(unittest.TestCase):
    """WebhookLabelEditedChangesColor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookLabelEditedChangesColor:
        """Test WebhookLabelEditedChangesColor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookLabelEditedChangesColor`
        """
        model = WebhookLabelEditedChangesColor()
        if include_optional:
            return WebhookLabelEditedChangesColor(
                var_from = ''
            )
        else:
            return WebhookLabelEditedChangesColor(
                var_from = '',
        )
        """

    def testWebhookLabelEditedChangesColor(self):
        """Test WebhookLabelEditedChangesColor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()