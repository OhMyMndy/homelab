# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_installation_repositories_added_repositories_removed_inner import WebhookInstallationRepositoriesAddedRepositoriesRemovedInner

class TestWebhookInstallationRepositoriesAddedRepositoriesRemovedInner(unittest.TestCase):
    """WebhookInstallationRepositoriesAddedRepositoriesRemovedInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookInstallationRepositoriesAddedRepositoriesRemovedInner:
        """Test WebhookInstallationRepositoriesAddedRepositoriesRemovedInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookInstallationRepositoriesAddedRepositoriesRemovedInner`
        """
        model = WebhookInstallationRepositoriesAddedRepositoriesRemovedInner()
        if include_optional:
            return WebhookInstallationRepositoriesAddedRepositoriesRemovedInner(
                full_name = '',
                id = 56,
                name = '',
                node_id = '',
                private = True
            )
        else:
            return WebhookInstallationRepositoriesAddedRepositoriesRemovedInner(
        )
        """

    def testWebhookInstallationRepositoriesAddedRepositoriesRemovedInner(self):
        """Test WebhookInstallationRepositoriesAddedRepositoriesRemovedInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()