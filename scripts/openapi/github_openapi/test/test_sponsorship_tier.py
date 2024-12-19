# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.sponsorship_tier import SponsorshipTier

class TestSponsorshipTier(unittest.TestCase):
    """SponsorshipTier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SponsorshipTier:
        """Test SponsorshipTier
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SponsorshipTier`
        """
        model = SponsorshipTier()
        if include_optional:
            return SponsorshipTier(
                created_at = '',
                description = '',
                is_custom_ammount = True,
                is_custom_amount = True,
                is_one_time = True,
                monthly_price_in_cents = 56,
                monthly_price_in_dollars = 56,
                name = '',
                node_id = ''
            )
        else:
            return SponsorshipTier(
                created_at = '',
                description = '',
                is_one_time = True,
                monthly_price_in_cents = 56,
                monthly_price_in_dollars = 56,
                name = '',
                node_id = '',
        )
        """

    def testSponsorshipTier(self):
        """Test SponsorshipTier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
