# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.simple_classroom_assignment import SimpleClassroomAssignment

class TestSimpleClassroomAssignment(unittest.TestCase):
    """SimpleClassroomAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleClassroomAssignment:
        """Test SimpleClassroomAssignment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleClassroomAssignment`
        """
        model = SimpleClassroomAssignment()
        if include_optional:
            return SimpleClassroomAssignment(
                id = 42,
                public_repo = True,
                title = 'Intro to Binaries',
                type = 'individual',
                invite_link = 'https://classroom.github.com/a/Lx7jiUgx',
                invitations_enabled = True,
                slug = 'intro-to-binaries',
                students_are_repo_admins = True,
                feedback_pull_requests_enabled = True,
                max_teams = 0,
                max_members = 0,
                editor = 'codespaces',
                accepted = 25,
                submitted = 10,
                passing = 10,
                language = 'elixir',
                deadline = '2011-01-26T19:06:43Z',
                classroom = github_openapi.models.simple_classroom.Simple Classroom(
                    id = 42, 
                    name = 'Programming Elixir', 
                    archived = False, 
                    url = 'https://classroom.github.com/classrooms/1-programming-elixir', )
            )
        else:
            return SimpleClassroomAssignment(
                id = 42,
                public_repo = True,
                title = 'Intro to Binaries',
                type = 'individual',
                invite_link = 'https://classroom.github.com/a/Lx7jiUgx',
                invitations_enabled = True,
                slug = 'intro-to-binaries',
                students_are_repo_admins = True,
                feedback_pull_requests_enabled = True,
                editor = 'codespaces',
                accepted = 25,
                submitted = 10,
                passing = 10,
                language = 'elixir',
                deadline = '2011-01-26T19:06:43Z',
                classroom = github_openapi.models.simple_classroom.Simple Classroom(
                    id = 42, 
                    name = 'Programming Elixir', 
                    archived = False, 
                    url = 'https://classroom.github.com/classrooms/1-programming-elixir', ),
        )
        """

    def testSimpleClassroomAssignment(self):
        """Test SimpleClassroomAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
