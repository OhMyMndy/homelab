# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_package_published_package_package_version_container_metadata import WebhookPackagePublishedPackagePackageVersionContainerMetadata

class TestWebhookPackagePublishedPackagePackageVersionContainerMetadata(unittest.TestCase):
    """WebhookPackagePublishedPackagePackageVersionContainerMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookPackagePublishedPackagePackageVersionContainerMetadata:
        """Test WebhookPackagePublishedPackagePackageVersionContainerMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookPackagePublishedPackagePackageVersionContainerMetadata`
        """
        model = WebhookPackagePublishedPackagePackageVersionContainerMetadata()
        if include_optional:
            return WebhookPackagePublishedPackagePackageVersionContainerMetadata(
                labels = github_openapi.models.labels.labels(),
                manifest = github_openapi.models.manifest.manifest(),
                tag = github_openapi.models.webhook_package_published_package_package_version_container_metadata_tag.webhook_package_published_package_package_version_container_metadata_tag(
                    digest = '', 
                    name = '', )
            )
        else:
            return WebhookPackagePublishedPackagePackageVersionContainerMetadata(
        )
        """

    def testWebhookPackagePublishedPackagePackageVersionContainerMetadata(self):
        """Test WebhookPackagePublishedPackagePackageVersionContainerMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
