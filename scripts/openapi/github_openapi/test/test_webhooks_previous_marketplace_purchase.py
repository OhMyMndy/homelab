# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_previous_marketplace_purchase import WebhooksPreviousMarketplacePurchase

class TestWebhooksPreviousMarketplacePurchase(unittest.TestCase):
    """WebhooksPreviousMarketplacePurchase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksPreviousMarketplacePurchase:
        """Test WebhooksPreviousMarketplacePurchase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksPreviousMarketplacePurchase`
        """
        model = WebhooksPreviousMarketplacePurchase()
        if include_optional:
            return WebhooksPreviousMarketplacePurchase(
                account = github_openapi.models.webhooks_marketplace_purchase_account.webhooks_marketplace_purchase_account(
                    id = 56, 
                    login = '', 
                    node_id = '', 
                    organization_billing_email = '', 
                    type = '', ),
                billing_cycle = '',
                free_trial_ends_on = None,
                next_billing_date = '',
                on_free_trial = True,
                plan = github_openapi.models.webhooks_previous_marketplace_purchase_plan.webhooks_previous_marketplace_purchase_plan(
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
                    yearly_price_in_cents = 56, ),
                unit_count = 56
            )
        else:
            return WebhooksPreviousMarketplacePurchase(
                account = github_openapi.models.webhooks_marketplace_purchase_account.webhooks_marketplace_purchase_account(
                    id = 56, 
                    login = '', 
                    node_id = '', 
                    organization_billing_email = '', 
                    type = '', ),
                billing_cycle = '',
                free_trial_ends_on = None,
                on_free_trial = True,
                plan = github_openapi.models.webhooks_previous_marketplace_purchase_plan.webhooks_previous_marketplace_purchase_plan(
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
                    yearly_price_in_cents = 56, ),
                unit_count = 56,
        )
        """

    def testWebhooksPreviousMarketplacePurchase(self):
        """Test WebhooksPreviousMarketplacePurchase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
