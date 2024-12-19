# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.notification_subject import NotificationSubject

class TestNotificationSubject(unittest.TestCase):
    """NotificationSubject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationSubject:
        """Test NotificationSubject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationSubject`
        """
        model = NotificationSubject()
        if include_optional:
            return NotificationSubject(
                html_url = '',
                latest_comment_html_url = '',
                latest_comment_url = '',
                state = '',
                title = '',
                type = '',
                url = ''
            )
        else:
            return NotificationSubject(
        )
        """

    def testNotificationSubject(self):
        """Test NotificationSubject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
