# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.orgs_update_webhook_request import OrgsUpdateWebhookRequest

class TestOrgsUpdateWebhookRequest(unittest.TestCase):
    """OrgsUpdateWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgsUpdateWebhookRequest:
        """Test OrgsUpdateWebhookRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgsUpdateWebhookRequest`
        """
        model = OrgsUpdateWebhookRequest()
        if include_optional:
            return OrgsUpdateWebhookRequest(
                config = github_openapi.models.orgs_update_webhook_request_config.orgs_update_webhook_request_config(
                    url = 'https://example.com/webhook', 
                    content_type = '"json"', 
                    secret = '"********"', 
                    insecure_ssl = null, ),
                events = [
                    ''
                    ],
                active = True,
                name = '"web"'
            )
        else:
            return OrgsUpdateWebhookRequest(
        )
        """

    def testOrgsUpdateWebhookRequest(self):
        """Test OrgsUpdateWebhookRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
