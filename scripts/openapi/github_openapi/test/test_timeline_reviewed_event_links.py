# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.timeline_reviewed_event_links import TimelineReviewedEventLinks

class TestTimelineReviewedEventLinks(unittest.TestCase):
    """TimelineReviewedEventLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineReviewedEventLinks:
        """Test TimelineReviewedEventLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineReviewedEventLinks`
        """
        model = TimelineReviewedEventLinks()
        if include_optional:
            return TimelineReviewedEventLinks(
                html = github_openapi.models.timeline_reviewed_event__links_html.timeline_reviewed_event__links_html(
                    href = '', ),
                pull_request = github_openapi.models.timeline_reviewed_event__links_html.timeline_reviewed_event__links_html(
                    href = '', )
            )
        else:
            return TimelineReviewedEventLinks(
                html = github_openapi.models.timeline_reviewed_event__links_html.timeline_reviewed_event__links_html(
                    href = '', ),
                pull_request = github_openapi.models.timeline_reviewed_event__links_html.timeline_reviewed_event__links_html(
                    href = '', ),
        )
        """

    def testTimelineReviewedEventLinks(self):
        """Test TimelineReviewedEventLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
