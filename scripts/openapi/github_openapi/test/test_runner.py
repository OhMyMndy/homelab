# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.runner import Runner

class TestRunner(unittest.TestCase):
    """Runner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Runner:
        """Test Runner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Runner`
        """
        model = Runner()
        if include_optional:
            return Runner(
                id = 5,
                runner_group_id = 1,
                name = 'iMac',
                os = 'macos',
                status = 'online',
                busy = True,
                labels = [
                    github_openapi.models.self_hosted_runner_label.Self hosted runner label(
                        id = 56, 
                        name = '', 
                        type = 'read-only', )
                    ]
            )
        else:
            return Runner(
                id = 5,
                name = 'iMac',
                os = 'macos',
                status = 'online',
                busy = True,
                labels = [
                    github_openapi.models.self_hosted_runner_label.Self hosted runner label(
                        id = 56, 
                        name = '', 
                        type = 'read-only', )
                    ],
        )
        """

    def testRunner(self):
        """Test Runner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()