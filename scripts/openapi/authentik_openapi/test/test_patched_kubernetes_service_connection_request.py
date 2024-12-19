# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.patched_kubernetes_service_connection_request import PatchedKubernetesServiceConnectionRequest

class TestPatchedKubernetesServiceConnectionRequest(unittest.TestCase):
    """PatchedKubernetesServiceConnectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedKubernetesServiceConnectionRequest:
        """Test PatchedKubernetesServiceConnectionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedKubernetesServiceConnectionRequest`
        """
        model = PatchedKubernetesServiceConnectionRequest()
        if include_optional:
            return PatchedKubernetesServiceConnectionRequest(
                name = '0',
                local = True,
                kubeconfig = None,
                verify_ssl = True
            )
        else:
            return PatchedKubernetesServiceConnectionRequest(
        )
        """

    def testPatchedKubernetesServiceConnectionRequest(self):
        """Test PatchedKubernetesServiceConnectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
