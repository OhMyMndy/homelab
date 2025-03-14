# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.copilot_seat_details import CopilotSeatDetails

class TestCopilotSeatDetails(unittest.TestCase):
    """CopilotSeatDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopilotSeatDetails:
        """Test CopilotSeatDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopilotSeatDetails`
        """
        model = CopilotSeatDetails()
        if include_optional:
            return CopilotSeatDetails(
                assignee = github_openapi.models.simple_user.Simple User(
                    name = '', 
                    email = '', 
                    login = 'octocat', 
                    id = 1, 
                    node_id = 'MDQ6VXNlcjE=', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                    url = 'https://api.github.com/users/octocat', 
                    html_url = 'https://github.com/octocat', 
                    followers_url = 'https://api.github.com/users/octocat/followers', 
                    following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                    gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                    starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                    subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                    organizations_url = 'https://api.github.com/users/octocat/orgs', 
                    repos_url = 'https://api.github.com/users/octocat/repos', 
                    events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                    received_events_url = 'https://api.github.com/users/octocat/received_events', 
                    type = 'User', 
                    site_admin = True, 
                    starred_at = '"2020-07-09T00:17:55Z"', 
                    user_view_type = 'public', ),
                organization = github_openapi.models.organization_simple.Organization Simple(
                    login = 'github', 
                    id = 1, 
                    node_id = 'MDEyOk9yZ2FuaXphdGlvbjE=', 
                    url = 'https://api.github.com/orgs/github', 
                    repos_url = 'https://api.github.com/orgs/github/repos', 
                    events_url = 'https://api.github.com/orgs/github/events', 
                    hooks_url = 'https://api.github.com/orgs/github/hooks', 
                    issues_url = 'https://api.github.com/orgs/github/issues', 
                    members_url = 'https://api.github.com/orgs/github/members{/member}', 
                    public_members_url = 'https://api.github.com/orgs/github/public_members{/member}', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    description = 'A great organization', ),
                assigning_team = None,
                pending_cancellation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                last_activity_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_activity_editor = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                plan_type = 'business'
            )
        else:
            return CopilotSeatDetails(
                assignee = github_openapi.models.simple_user.Simple User(
                    name = '', 
                    email = '', 
                    login = 'octocat', 
                    id = 1, 
                    node_id = 'MDQ6VXNlcjE=', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    gravatar_id = '41d064eb2195891e12d0413f63227ea7', 
                    url = 'https://api.github.com/users/octocat', 
                    html_url = 'https://github.com/octocat', 
                    followers_url = 'https://api.github.com/users/octocat/followers', 
                    following_url = 'https://api.github.com/users/octocat/following{/other_user}', 
                    gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}', 
                    starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}', 
                    subscriptions_url = 'https://api.github.com/users/octocat/subscriptions', 
                    organizations_url = 'https://api.github.com/users/octocat/orgs', 
                    repos_url = 'https://api.github.com/users/octocat/repos', 
                    events_url = 'https://api.github.com/users/octocat/events{/privacy}', 
                    received_events_url = 'https://api.github.com/users/octocat/received_events', 
                    type = 'User', 
                    site_admin = True, 
                    starred_at = '"2020-07-09T00:17:55Z"', 
                    user_view_type = 'public', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCopilotSeatDetails(self):
        """Test CopilotSeatDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
