# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.orgs_list_attestations200_response import OrgsListAttestations200Response

class TestOrgsListAttestations200Response(unittest.TestCase):
    """OrgsListAttestations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgsListAttestations200Response:
        """Test OrgsListAttestations200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgsListAttestations200Response`
        """
        model = OrgsListAttestations200Response()
        if include_optional:
            return OrgsListAttestations200Response(
                attestations = [
                    github_openapi.models.orgs_list_attestations_200_response_attestations_inner.orgs_list_attestations_200_response_attestations_inner(
                        bundle = github_openapi.models.orgs_list_attestations_200_response_attestations_inner_bundle.orgs_list_attestations_200_response_attestations_inner_bundle(
                            media_type = '', 
                            verification_material = { }, 
                            dsse_envelope = { }, ), 
                        repository_id = 56, 
                        bundle_url = '', )
                    ]
            )
        else:
            return OrgsListAttestations200Response(
        )
        """

    def testOrgsListAttestations200Response(self):
        """Test OrgsListAttestations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()