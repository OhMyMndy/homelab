# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.marketplace_purchase_marketplace_pending_change import MarketplacePurchaseMarketplacePendingChange

class TestMarketplacePurchaseMarketplacePendingChange(unittest.TestCase):
    """MarketplacePurchaseMarketplacePendingChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarketplacePurchaseMarketplacePendingChange:
        """Test MarketplacePurchaseMarketplacePendingChange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarketplacePurchaseMarketplacePendingChange`
        """
        model = MarketplacePurchaseMarketplacePendingChange()
        if include_optional:
            return MarketplacePurchaseMarketplacePendingChange(
                is_installed = True,
                effective_date = '',
                unit_count = 56,
                id = 56,
                plan = github_openapi.models.marketplace_listing_plan.Marketplace Listing Plan(
                    url = 'https://api.github.com/marketplace_listing/plans/1313', 
                    accounts_url = 'https://api.github.com/marketplace_listing/plans/1313/accounts', 
                    id = 1313, 
                    number = 3, 
                    name = 'Pro', 
                    description = 'A professional-grade CI solution', 
                    monthly_price_in_cents = 1099, 
                    yearly_price_in_cents = 11870, 
                    price_model = 'FLAT_RATE', 
                    has_free_trial = True, 
                    unit_name = '', 
                    state = 'published', 
                    bullets = ["Up to 25 private repositories","11 concurrent builds"], )
            )
        else:
            return MarketplacePurchaseMarketplacePendingChange(
        )
        """

    def testMarketplacePurchaseMarketplacePendingChange(self):
        """Test MarketplacePurchaseMarketplacePendingChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
