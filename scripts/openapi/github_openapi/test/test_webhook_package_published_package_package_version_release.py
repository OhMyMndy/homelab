# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_package_published_package_package_version_release import WebhookPackagePublishedPackagePackageVersionRelease

class TestWebhookPackagePublishedPackagePackageVersionRelease(unittest.TestCase):
    """WebhookPackagePublishedPackagePackageVersionRelease unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookPackagePublishedPackagePackageVersionRelease:
        """Test WebhookPackagePublishedPackagePackageVersionRelease
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookPackagePublishedPackagePackageVersionRelease`
        """
        model = WebhookPackagePublishedPackagePackageVersionRelease()
        if include_optional:
            return WebhookPackagePublishedPackagePackageVersionRelease(
                author = github_openapi.models.user.User(
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
                created_at = '',
                draft = True,
                html_url = '',
                id = 56,
                name = '',
                prerelease = True,
                published_at = '',
                tag_name = '',
                target_commitish = '',
                url = ''
            )
        else:
            return WebhookPackagePublishedPackagePackageVersionRelease(
                author = github_openapi.models.user.User(
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
                created_at = '',
                draft = True,
                html_url = '',
                id = 56,
                name = '',
                prerelease = True,
                published_at = '',
                tag_name = '',
                target_commitish = '',
                url = '',
        )
        """

    def testWebhookPackagePublishedPackagePackageVersionRelease(self):
        """Test WebhookPackagePublishedPackagePackageVersionRelease"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
