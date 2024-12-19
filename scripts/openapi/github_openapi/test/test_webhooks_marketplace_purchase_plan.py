# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_marketplace_purchase_plan import WebhooksMarketplacePurchasePlan

class TestWebhooksMarketplacePurchasePlan(unittest.TestCase):
    """WebhooksMarketplacePurchasePlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksMarketplacePurchasePlan:
        """Test WebhooksMarketplacePurchasePlan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksMarketplacePurchasePlan`
        """
        model = WebhooksMarketplacePurchasePlan()
        if include_optional:
            return WebhooksMarketplacePurchasePlan(
                bullets = [
                    ''
                    ],
                description = '',
                has_free_trial = True,
                id = 56,
                monthly_price_in_cents = 56,
                name = '',
                price_model = 'FREE',
                unit_name = '',
                yearly_price_in_cents = 56
            )
        else:
            return WebhooksMarketplacePurchasePlan(
                bullets = [
                    ''
                    ],
                description = '',
                has_free_trial = True,
                id = 56,
                monthly_price_in_cents = 56,
                name = '',
                price_model = 'FREE',
                unit_name = '',
                yearly_price_in_cents = 56,
        )
        """

    def testWebhooksMarketplacePurchasePlan(self):
        """Test WebhooksMarketplacePurchasePlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
