# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_security_advisory_vulnerabilities_inner_package import WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage

class TestWebhooksSecurityAdvisoryVulnerabilitiesInnerPackage(unittest.TestCase):
    """WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage:
        """Test WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage`
        """
        model = WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage()
        if include_optional:
            return WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage(
                ecosystem = '',
                name = ''
            )
        else:
            return WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage(
                ecosystem = '',
                name = '',
        )
        """

    def testWebhooksSecurityAdvisoryVulnerabilitiesInnerPackage(self):
        """Test WebhooksSecurityAdvisoryVulnerabilitiesInnerPackage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
