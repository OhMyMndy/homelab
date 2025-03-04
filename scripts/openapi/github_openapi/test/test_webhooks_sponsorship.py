# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhooks_sponsorship import WebhooksSponsorship

class TestWebhooksSponsorship(unittest.TestCase):
    """WebhooksSponsorship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhooksSponsorship:
        """Test WebhooksSponsorship
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhooksSponsorship`
        """
        model = WebhooksSponsorship()
        if include_optional:
            return WebhooksSponsorship(
                created_at = '',
                maintainer = github_openapi.models.webhooks_sponsorship_maintainer.webhooks_sponsorship_maintainer(
                    avatar_url = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = '', 
                    url = '', 
                    user_view_type = '', ),
                node_id = '',
                privacy_level = '',
                sponsor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                sponsorable = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                tier = github_openapi.models.sponsorship_tier.Sponsorship Tier(
                    created_at = '', 
                    description = '', 
                    is_custom_ammount = True, 
                    is_custom_amount = True, 
                    is_one_time = True, 
                    monthly_price_in_cents = 56, 
                    monthly_price_in_dollars = 56, 
                    name = '', 
                    node_id = '', )
            )
        else:
            return WebhooksSponsorship(
                created_at = '',
                node_id = '',
                privacy_level = '',
                sponsor = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                sponsorable = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                tier = github_openapi.models.sponsorship_tier.Sponsorship Tier(
                    created_at = '', 
                    description = '', 
                    is_custom_ammount = True, 
                    is_custom_amount = True, 
                    is_one_time = True, 
                    monthly_price_in_cents = 56, 
                    monthly_price_in_dollars = 56, 
                    name = '', 
                    node_id = '', ),
        )
        """

    def testWebhooksSponsorship(self):
        """Test WebhooksSponsorship"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
