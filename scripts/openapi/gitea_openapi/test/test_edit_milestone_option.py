# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.edit_milestone_option import EditMilestoneOption

class TestEditMilestoneOption(unittest.TestCase):
    """EditMilestoneOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditMilestoneOption:
        """Test EditMilestoneOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditMilestoneOption`
        """
        model = EditMilestoneOption()
        if include_optional:
            return EditMilestoneOption(
                description = '',
                due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = '',
                title = ''
            )
        else:
            return EditMilestoneOption(
        )
        """

    def testEditMilestoneOption(self):
        """Test EditMilestoneOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
