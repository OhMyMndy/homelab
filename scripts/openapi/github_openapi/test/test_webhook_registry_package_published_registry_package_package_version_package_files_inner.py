# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_registry_package_published_registry_package_package_version_package_files_inner import WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner

class TestWebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner(unittest.TestCase):
    """WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner:
        """Test WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner`
        """
        model = WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner()
        if include_optional:
            return WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner(
                content_type = '',
                created_at = '',
                download_url = '',
                id = 56,
                md5 = '',
                name = '',
                sha1 = '',
                sha256 = '',
                size = 56,
                state = '',
                updated_at = ''
            )
        else:
            return WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner(
                content_type = '',
                created_at = '',
                download_url = '',
                id = 56,
                md5 = '',
                name = '',
                sha1 = '',
                sha256 = '',
                size = 56,
                state = '',
                updated_at = '',
        )
        """

    def testWebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner(self):
        """Test WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
