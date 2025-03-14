# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.simple_commit import SimpleCommit

class TestSimpleCommit(unittest.TestCase):
    """SimpleCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleCommit:
        """Test SimpleCommit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleCommit`
        """
        model = SimpleCommit()
        if include_optional:
            return SimpleCommit(
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
                id = '',
                message = '',
                timestamp = '',
                tree_id = ''
            )
        else:
            return SimpleCommit(
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
                id = '',
                message = '',
                timestamp = '',
                tree_id = '',
        )
        """

    def testSimpleCommit(self):
        """Test SimpleCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
