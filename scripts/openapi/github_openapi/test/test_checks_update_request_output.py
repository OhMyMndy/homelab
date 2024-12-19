# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.checks_update_request_output import ChecksUpdateRequestOutput

class TestChecksUpdateRequestOutput(unittest.TestCase):
    """ChecksUpdateRequestOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecksUpdateRequestOutput:
        """Test ChecksUpdateRequestOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecksUpdateRequestOutput`
        """
        model = ChecksUpdateRequestOutput()
        if include_optional:
            return ChecksUpdateRequestOutput(
                title = '',
                summary = '',
                text = '',
                annotations = [
                    github_openapi.models.checks_create_request_output_annotations_inner.checks_create_request_output_annotations_inner(
                        path = '', 
                        start_line = 56, 
                        end_line = 56, 
                        start_column = 56, 
                        end_column = 56, 
                        annotation_level = 'notice', 
                        message = '', 
                        title = '', 
                        raw_details = '', )
                    ],
                images = [
                    github_openapi.models.checks_create_request_output_images_inner.checks_create_request_output_images_inner(
                        alt = '', 
                        image_url = '', 
                        caption = '', )
                    ]
            )
        else:
            return ChecksUpdateRequestOutput(
                summary = '',
        )
        """

    def testChecksUpdateRequestOutput(self):
        """Test ChecksUpdateRequestOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()