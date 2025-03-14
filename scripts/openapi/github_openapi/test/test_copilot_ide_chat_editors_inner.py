# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_ide_chat_editors_inner import CopilotIdeChatEditorsInner

class TestCopilotIdeChatEditorsInner(unittest.TestCase):
    """CopilotIdeChatEditorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotIdeChatEditorsInner:
        """Test CopilotIdeChatEditorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotIdeChatEditorsInner`
        """
        model = CopilotIdeChatEditorsInner()
        if include_optional:
            return CopilotIdeChatEditorsInner(
                name = '',
                total_engaged_users = 56,
                models = [
                    github_openapi.models.copilot_ide_chat_editors_inner_models_inner.copilot_ide_chat_editors_inner_models_inner(
                        name = '', 
                        is_custom_model = True, 
                        custom_model_training_date = '', 
                        total_engaged_users = 56, 
                        total_chats = 56, 
                        total_chat_insertion_events = 56, 
                        total_chat_copy_events = 56, )
                    ]
            )
        else:
            return CopilotIdeChatEditorsInner(
        )
        """

    def testCopilotIdeChatEditorsInner(self):
        """Test CopilotIdeChatEditorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
