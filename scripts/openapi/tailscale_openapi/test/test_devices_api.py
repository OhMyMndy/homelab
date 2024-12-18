# coding: utf-8

"""
    Tailscale API

    ### Overview  **The API endpoints documented here are stable. However, the OpenAPI spec used to generate this documentation is unstable. It may change or break without notice.**  The Tailscale API is a (mostly) RESTful API. Typically, both POST bodies and responses are JSON-encoded.  ### Base URL  The base URL for the Tailscale API is https://api.tailscale.com/api/v2/.  Examples in this document may abbreviate this to `/api/v2/`.  ### Authentication  Requests to the Tailscale API are authenticated with an API access token (sometimes called an API key). Access tokens can be supplied as the username portion of HTTP Basic authentication (leave the password blank) or as an OAuth Bearer token:  ``` // passing token with basic auth curl -u \"tskey-api-xxxxx:\" https://api.tailscale.com/api/v2/...  // passing token as bearer token curl -H \"Authorization: Bearer tskey-api-xxxxx\" https://api.tailscale.com/api/v2/... ```  Access tokens for individual users can be created and managed from the [Keys](https://login.tailscale.com/admin/settings/keys) page of the admin console. These tokens will have the same permissions as the owning user, and can be set to expire in 1 to 90 days. Access tokens are identifiable by the prefix tskey-api-.  Alternatively, an OAuth client can be used to create short-lived access tokens with scoped permission. OAuth clients don't expire, and can therefore be used to provide ongoing access to the API, creating access tokens as needed. OAuth clients and the access tokens they create are not tied to an individual Tailscale user. OAuth client secrets are identifiable by the prefix tskey-client-. Learn more about [OAuth clients].  [ OAuth clients ]: https://tailscale.com/kb/1215/  ### Errors  The Tailscale API returns status codes consistent with standard HTTP conventions. In addition to the status code, errors may include additional information in the response body:  ``` {   \"message\": \"additional error information\" } ```  ### Pagination  The Tailscale API does not currently support pagination. All results are returned at once.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tailscale_openapi.api.devices_api import DevicesApi


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DevicesApi()

    def tearDown(self) -> None:
        pass

    def test_authorize_device(self) -> None:
        """Test case for authorize_device

        Authorize device
        """
        pass

    def test_delete_custom_device_posture_attributes(self) -> None:
        """Test case for delete_custom_device_posture_attributes

        Delete custom device posture attributes
        """
        pass

    def test_delete_device(self) -> None:
        """Test case for delete_device

        Delete a device
        """
        pass

    def test_expire_device_key(self) -> None:
        """Test case for expire_device_key

        Expire a device's key
        """
        pass

    def test_get_device(self) -> None:
        """Test case for get_device

        Get a device
        """
        pass

    def test_get_device_posture_attributes(self) -> None:
        """Test case for get_device_posture_attributes

        Get device posture attributes
        """
        pass

    def test_list_device_routes(self) -> None:
        """Test case for list_device_routes

        List device routes
        """
        pass

    def test_list_tailnet_devices(self) -> None:
        """Test case for list_tailnet_devices

        List tailnet devices
        """
        pass

    def test_set_custom_device_posture_attributes(self) -> None:
        """Test case for set_custom_device_posture_attributes

        Set custom device posture attributes
        """
        pass

    def test_set_device_ip(self) -> None:
        """Test case for set_device_ip

        Set device IPv4 address
        """
        pass

    def test_set_device_name(self) -> None:
        """Test case for set_device_name

        Set device name
        """
        pass

    def test_set_device_routes(self) -> None:
        """Test case for set_device_routes

        Set device routes
        """
        pass

    def test_set_device_tags(self) -> None:
        """Test case for set_device_tags

        Set device tags
        """
        pass

    def test_update_device_key(self) -> None:
        """Test case for update_device_key

        Update device key
        """
        pass


if __name__ == '__main__':
    unittest.main()