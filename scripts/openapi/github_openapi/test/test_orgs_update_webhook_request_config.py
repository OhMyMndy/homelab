# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.orgs_update_webhook_request_config import OrgsUpdateWebhookRequestConfig

class TestOrgsUpdateWebhookRequestConfig(unittest.TestCase):
    """OrgsUpdateWebhookRequestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgsUpdateWebhookRequestConfig:
        """Test OrgsUpdateWebhookRequestConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgsUpdateWebhookRequestConfig`
        """
        model = OrgsUpdateWebhookRequestConfig()
        if include_optional:
            return OrgsUpdateWebhookRequestConfig(
                url = 'https://example.com/webhook',
                content_type = '"json"',
                secret = '"********"',
                insecure_ssl = None
            )
        else:
            return OrgsUpdateWebhookRequestConfig(
                url = 'https://example.com/webhook',
        )
        """

    def testOrgsUpdateWebhookRequestConfig(self):
        """Test OrgsUpdateWebhookRequestConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
