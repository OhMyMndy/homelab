# coding: utf-8

"""
    Tailscale API

    ### Overview  **The API endpoints documented here are stable. However, the OpenAPI spec used to generate this documentation is unstable. It may change or break without notice.**  The Tailscale API is a (mostly) RESTful API. Typically, both POST bodies and responses are JSON-encoded.  ### Base URL  The base URL for the Tailscale API is https://api.tailscale.com/api/v2/.  Examples in this document may abbreviate this to `/api/v2/`.  ### Authentication  Requests to the Tailscale API are authenticated with an API access token (sometimes called an API key). Access tokens can be supplied as the username portion of HTTP Basic authentication (leave the password blank) or as an OAuth Bearer token:  ``` // passing token with basic auth curl -u \"tskey-api-xxxxx:\" https://api.tailscale.com/api/v2/...  // passing token as bearer token curl -H \"Authorization: Bearer tskey-api-xxxxx\" https://api.tailscale.com/api/v2/... ```  Access tokens for individual users can be created and managed from the [Keys](https://login.tailscale.com/admin/settings/keys) page of the admin console. These tokens will have the same permissions as the owning user, and can be set to expire in 1 to 90 days. Access tokens are identifiable by the prefix tskey-api-.  Alternatively, an OAuth client can be used to create short-lived access tokens with scoped permission. OAuth clients don't expire, and can therefore be used to provide ongoing access to the API, creating access tokens as needed. OAuth clients and the access tokens they create are not tied to an individual Tailscale user. OAuth client secrets are identifiable by the prefix tskey-client-. Learn more about [OAuth clients].  [ OAuth clients ]: https://tailscale.com/kb/1215/  ### Errors  The Tailscale API returns status codes consistent with standard HTTP conventions. In addition to the status code, errors may include additional information in the response body:  ``` {   \"message\": \"additional error information\" } ```  ### Pagination  The Tailscale API does not currently support pagination. All results are returned at once.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tailscale_openapi.models.list_configuration_audit_logs200_response import ListConfigurationAuditLogs200Response

class TestListConfigurationAuditLogs200Response(unittest.TestCase):
    """ListConfigurationAuditLogs200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListConfigurationAuditLogs200Response:
        """Test ListConfigurationAuditLogs200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfigurationAuditLogs200Response`
        """
        model = ListConfigurationAuditLogs200Response()
        if include_optional:
            return ListConfigurationAuditLogs200Response(
                version = '1.1',
                tailnet = 'example.com',
                logs = [
                    {action=CREATE, actor={displayName=Lion Dahlia Armadillo, id=uZKk3KSfrH11KTM59, loginName=lion.dahlia.armadillo@example.com, type=USER}, deferredAt=0001-01-01T00:00:00Z, eventGroupID=0378d8f57300d172ef7ae3826e097ef0, eventTime=2024-06-06T15:25:26.583893Z, origin=ADMIN_CONSOLE, target={id=nBLYviWLGB21KTM59, isEphemeral=true, name=silver-robin-horse-albatross-armadillo.taile18a.ts.net, type=NODE}, type=CONFIG}
                    ]
            )
        else:
            return ListConfigurationAuditLogs200Response(
        )
        """

    def testListConfigurationAuditLogs200Response(self):
        """Test ListConfigurationAuditLogs200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()