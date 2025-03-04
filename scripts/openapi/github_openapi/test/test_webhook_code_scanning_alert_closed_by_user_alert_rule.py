# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_code_scanning_alert_closed_by_user_alert_rule import WebhookCodeScanningAlertClosedByUserAlertRule

class TestWebhookCodeScanningAlertClosedByUserAlertRule(unittest.TestCase):
    """WebhookCodeScanningAlertClosedByUserAlertRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookCodeScanningAlertClosedByUserAlertRule:
        """Test WebhookCodeScanningAlertClosedByUserAlertRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookCodeScanningAlertClosedByUserAlertRule`
        """
        model = WebhookCodeScanningAlertClosedByUserAlertRule()
        if include_optional:
            return WebhookCodeScanningAlertClosedByUserAlertRule(
                description = '',
                full_description = '',
                help = '',
                help_uri = '',
                id = '',
                name = '',
                severity = 'none',
                tags = [
                    ''
                    ]
            )
        else:
            return WebhookCodeScanningAlertClosedByUserAlertRule(
                description = '',
                id = '',
                severity = 'none',
        )
        """

    def testWebhookCodeScanningAlertClosedByUserAlertRule(self):
        """Test WebhookCodeScanningAlertClosedByUserAlertRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
