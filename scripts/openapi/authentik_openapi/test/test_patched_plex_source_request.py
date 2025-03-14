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

from authentik_openapi.models.patched_plex_source_request import PatchedPlexSourceRequest

class TestPatchedPlexSourceRequest(unittest.TestCase):
    """PatchedPlexSourceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedPlexSourceRequest:
        """Test PatchedPlexSourceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedPlexSourceRequest`
        """
        model = PatchedPlexSourceRequest()
        if include_optional:
            return PatchedPlexSourceRequest(
                name = '0',
                slug = 'z0',
                enabled = True,
                authentication_flow = '',
                enrollment_flow = '',
                policy_engine_mode = 'all',
                user_matching_mode = 'identifier',
                user_path_template = '0',
                client_id = '0',
                allowed_servers = [
                    '0'
                    ],
                allow_friends = True,
                plex_token = '0'
            )
        else:
            return PatchedPlexSourceRequest(
        )
        """

    def testPatchedPlexSourceRequest(self):
        """Test PatchedPlexSourceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
