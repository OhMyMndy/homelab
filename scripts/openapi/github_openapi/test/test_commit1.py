# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.commit1 import Commit1

class TestCommit1(unittest.TestCase):
    """Commit1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Commit1:
        """Test Commit1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Commit1`
        """
        model = Commit1()
        if include_optional:
            return Commit1(
                added = [
                    ''
                    ],
                author = github_openapi.models.committer.Committer(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    name = '', 
                    username = '', ),
                committer = github_openapi.models.committer.Committer(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    name = '', 
                    username = '', ),
                distinct = True,
                id = '',
                message = '',
                modified = [
                    ''
                    ],
                removed = [
                    ''
                    ],
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tree_id = '',
                url = ''
            )
        else:
            return Commit1(
                author = github_openapi.models.committer.Committer(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    name = '', 
                    username = '', ),
                committer = github_openapi.models.committer.Committer(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    name = '', 
                    username = '', ),
                distinct = True,
                id = '',
                message = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tree_id = '',
                url = '',
        )
        """

    def testCommit1(self):
        """Test Commit1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
