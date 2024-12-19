# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_users200_response import CopilotCancelCopilotSeatAssignmentForUsers200Response

class TestCopilotCancelCopilotSeatAssignmentForUsers200Response(unittest.TestCase):
    """CopilotCancelCopilotSeatAssignmentForUsers200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotCancelCopilotSeatAssignmentForUsers200Response:
        """Test CopilotCancelCopilotSeatAssignmentForUsers200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotCancelCopilotSeatAssignmentForUsers200Response`
        """
        model = CopilotCancelCopilotSeatAssignmentForUsers200Response()
        if include_optional:
            return CopilotCancelCopilotSeatAssignmentForUsers200Response(
                seats_cancelled = 56
            )
        else:
            return CopilotCancelCopilotSeatAssignmentForUsers200Response(
                seats_cancelled = 56,
        )
        """

    def testCopilotCancelCopilotSeatAssignmentForUsers200Response(self):
        """Test CopilotCancelCopilotSeatAssignmentForUsers200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()