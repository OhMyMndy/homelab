import os
from pprint import pprint

from tailscale_openapi.models.list_dns_nameservers200_response import (
    ListDnsNameservers200Response,
)
from tailscale_openapi.exceptions import ApiException

from tailscale_openapi.configuration import Configuration
from tailscale_openapi.api_client import ApiClient
from tailscale_openapi.api.dns_api import DNSApi


# import logging
# import os
# from datetime import datetime, timezone
#
# from bitwarden_sdk import (
#     BitwardenClient,
#     DeviceType,
#     client_settings_from_dict,
#     api_key_login_request_from_dict,
# )
# login_request = api_key_login_request_from_dict({
#     "clientId": os.getenv("CLIENT_ID"),
#     "clientSecret": os.getenv("CLIENT_SECRET"),
#     "p"
# })
# # Create the BitwardenClient, which is used to interact with the SDK
# client = BitwardenClient(
#     client_settings_from_dict(
#         {
#             "apiUrl": os.getenv("API_URL", "https://passwords.home.ohmymndy.com"),
#             "deviceType": DeviceType.SDK,
#             # "identityUrl": os.getenv("IDENTITY_URL", "http://localhost:33656"),
#             "userAgent": "Python",
#         }
#     )
# )
# logging.basicConfig(level=logging.DEBUG)
# # organization_id = os.getenv("ORGANIZATION_ID")
#
# # Set the state file location
# # Note: the path must exist, the file will be created & managed by the sdk
# state_path = "/tmp/.bw-state"  # os.getenv("STATE_FILE")
#
# # Attempt to authenticate with the Secrets Manager Access Token
# client.auth().login_access_token(os.getenv("ACCESS_TOKEN"), state_path)
# client.auth()
#
#
def get_tailnet() -> str:
    return ""


def set_dns(dns: list[str]):
    tailnet = os.environ["TAILNET"]
    configuration = Configuration(access_token=os.environ["BEARER_TOKEN"])
    with ApiClient(configuration) as api_client:
        try:
            dns_api = DNSApi(api_client)
            api_response = dns_api.set_dns_nameservers(
                tailnet,
                ListDnsNameservers200Response.from_dict({"dns": dns, "magicDNS": True}),
            )
            pprint(api_response)
            api_response = dns_api.list_dns_nameservers(tailnet=tailnet)
            pprint(api_response)
        except ApiException as e:
            print("Exception %s\n" % e)
