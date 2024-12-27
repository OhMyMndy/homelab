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

from authentik_openapi.models.scim_source import SCIMSource

class TestSCIMSource(unittest.TestCase):
    """SCIMSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SCIMSource:
        """Test SCIMSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SCIMSource`
        """
        model = SCIMSource()
        if include_optional:
            return SCIMSource(
                pk = '',
                name = '',
                slug = 'z',
                enabled = True,
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                user_matching_mode = 'identifier',
                managed = '',
                user_path_template = '',
                root_url = '',
                token_obj = authentik_openapi.models.token.Token(
                    pk = '', 
                    managed = '', 
                    identifier = 'z', 
                    intent = 'verification', 
                    user = 56, 
                    user_obj = null, 
                    description = '', 
                    expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expiring = True, )
            )
        else:
            return SCIMSource(
                pk = '',
                name = '',
                slug = 'z',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                managed = '',
                root_url = '',
                token_obj = authentik_openapi.models.token.Token(
                    pk = '', 
                    managed = '', 
                    identifier = 'z', 
                    intent = 'verification', 
                    user = 56, 
                    user_obj = null, 
                    description = '', 
                    expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expiring = True, ),
        )
        """

    def testSCIMSource(self):
        """Test SCIMSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()