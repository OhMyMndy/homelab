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

from authentik_openapi.models.stage_prompt import StagePrompt

class TestStagePrompt(unittest.TestCase):
    """StagePrompt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StagePrompt:
        """Test StagePrompt
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StagePrompt`
        """
        model = StagePrompt()
        if include_optional:
            return StagePrompt(
                field_key = '',
                label = '',
                type = 'text',
                required = True,
                placeholder = '',
                initial_value = '',
                order = 56,
                sub_text = '',
                choices = [
                    ''
                    ]
            )
        else:
            return StagePrompt(
                field_key = '',
                label = '',
                type = 'text',
                required = True,
                placeholder = '',
                initial_value = '',
                order = 56,
                sub_text = '',
                choices = [
                    ''
                    ],
        )
        """

    def testStagePrompt(self):
        """Test StagePrompt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
