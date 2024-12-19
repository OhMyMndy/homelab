# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.milestone import Milestone

class TestMilestone(unittest.TestCase):
    """Milestone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Milestone:
        """Test Milestone
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Milestone`
        """
        model = Milestone()
        if include_optional:
            return Milestone(
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed_issues = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                description = '',
                due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                html_url = '',
                id = 56,
                labels_url = '',
                node_id = '',
                number = 56,
                open_issues = 56,
                state = 'open',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = ''
            )
        else:
            return Milestone(
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed_issues = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator = github_openapi.models.user.User(
                    avatar_url = '', 
                    deleted = True, 
                    email = '', 
                    events_url = '', 
                    followers_url = '', 
                    following_url = '', 
                    gists_url = '', 
                    gravatar_id = '', 
                    html_url = '', 
                    id = 56, 
                    login = '', 
                    name = '', 
                    node_id = '', 
                    organizations_url = '', 
                    received_events_url = '', 
                    repos_url = '', 
                    site_admin = True, 
                    starred_url = '', 
                    subscriptions_url = '', 
                    type = 'Bot', 
                    url = '', 
                    user_view_type = '', ),
                description = '',
                due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                html_url = '',
                id = 56,
                labels_url = '',
                node_id = '',
                number = 56,
                open_issues = 56,
                state = 'open',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
        )
        """

    def testMilestone(self):
        """Test Milestone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
