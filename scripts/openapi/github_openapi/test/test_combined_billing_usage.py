# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.combined_billing_usage import CombinedBillingUsage

class TestCombinedBillingUsage(unittest.TestCase):
    """CombinedBillingUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CombinedBillingUsage:
        """Test CombinedBillingUsage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CombinedBillingUsage`
        """
        model = CombinedBillingUsage()
        if include_optional:
            return CombinedBillingUsage(
                days_left_in_billing_cycle = 56,
                estimated_paid_storage_for_month = 56,
                estimated_storage_for_month = 56
            )
        else:
            return CombinedBillingUsage(
                days_left_in_billing_cycle = 56,
                estimated_paid_storage_for_month = 56,
                estimated_storage_for_month = 56,
        )
        """

    def testCombinedBillingUsage(self):
        """Test CombinedBillingUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()