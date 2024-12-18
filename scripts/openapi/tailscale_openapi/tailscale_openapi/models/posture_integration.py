# coding: utf-8

"""
    Tailscale API

    ### Overview  **The API endpoints documented here are stable. However, the OpenAPI spec used to generate this documentation is unstable. It may change or break without notice.**  The Tailscale API is a (mostly) RESTful API. Typically, both POST bodies and responses are JSON-encoded.  ### Base URL  The base URL for the Tailscale API is https://api.tailscale.com/api/v2/.  Examples in this document may abbreviate this to `/api/v2/`.  ### Authentication  Requests to the Tailscale API are authenticated with an API access token (sometimes called an API key). Access tokens can be supplied as the username portion of HTTP Basic authentication (leave the password blank) or as an OAuth Bearer token:  ``` // passing token with basic auth curl -u \"tskey-api-xxxxx:\" https://api.tailscale.com/api/v2/...  // passing token as bearer token curl -H \"Authorization: Bearer tskey-api-xxxxx\" https://api.tailscale.com/api/v2/... ```  Access tokens for individual users can be created and managed from the [Keys](https://login.tailscale.com/admin/settings/keys) page of the admin console. These tokens will have the same permissions as the owning user, and can be set to expire in 1 to 90 days. Access tokens are identifiable by the prefix tskey-api-.  Alternatively, an OAuth client can be used to create short-lived access tokens with scoped permission. OAuth clients don't expire, and can therefore be used to provide ongoing access to the API, creating access tokens as needed. OAuth clients and the access tokens they create are not tied to an individual Tailscale user. OAuth client secrets are identifiable by the prefix tskey-client-. Learn more about [OAuth clients].  [ OAuth clients ]: https://tailscale.com/kb/1215/  ### Errors  The Tailscale API returns status codes consistent with standard HTTP conventions. In addition to the status code, errors may include additional information in the response body:  ``` {   \"message\": \"additional error information\" } ```  ### Pagination  The Tailscale API does not currently support pagination. All results are returned at once.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tailscale_openapi.models.posture_integration_status import PostureIntegrationStatus
from typing import Optional, Set
from typing_extensions import Self

class PostureIntegration(BaseModel):
    """
    A configured PostureIntegration.
    """ # noqa: E501
    provider: Optional[StrictStr] = Field(default=None, description="The device posture provider.  Required on POST requests, ignored on PATCH requests. ")
    cloud_id: Optional[StrictStr] = Field(default=None, description="Identifies which of the provider's clouds to integrate with.  - For CrowdStrike Falcon, it will be one of `us-1`, `us-2`, `eu-1` or `us-gov`. - For Microsoft Intune, it will be one of `global` or `us-gov`.  - For Jamf Pro, Kandji and Sentinel One, it is the FQDN of your subdomain, for example `mydomain.sentinelone.net`. - For Kolide, this is left blank. ", alias="cloudId")
    client_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for your client.  - For Microsoft Intune, it will be your application's UUID. - For CrowdStrike Falcon and Jamf Pro, it will be your client id. - For Kandji, Kolide and Sentinel One, this is left blank. ", alias="clientId")
    tenant_id: Optional[StrictStr] = Field(default=None, description="The Microsoft Intune directory (tenant) ID. For other providers, this is left blank.", alias="tenantId")
    client_secret: Optional[StrictStr] = Field(default=None, description="The secret (auth key, token, etc.) used to authenticate with the provider.  Required when creating a new integration, may be omitted when updating an existing integration, in which case we retain the existing password. ", alias="clientSecret")
    id: Optional[StrictStr] = Field(default=None, description="A unique identifier for the integration (generated by the system).")
    config_updated: Optional[StrictStr] = Field(default=None, description="Timestamp of the last time this configuration was updated, in RFC 3339 format.", alias="configUpdated")
    status: Optional[PostureIntegrationStatus] = None
    __properties: ClassVar[List[str]] = ["provider", "cloudId", "clientId", "tenantId", "clientSecret", "id", "configUpdated", "status"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['falcon', 'intune', 'jamfpro', 'kandji', 'kolide', 'sentinelone']):
            raise ValueError("must be one of enum values ('falcon', 'intune', 'jamfpro', 'kandji', 'kolide', 'sentinelone')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PostureIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "config_updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostureIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider"),
            "cloudId": obj.get("cloudId"),
            "clientId": obj.get("clientId"),
            "tenantId": obj.get("tenantId"),
            "clientSecret": obj.get("clientSecret"),
            "id": obj.get("id"),
            "configUpdated": obj.get("configUpdated"),
            "status": PostureIntegrationStatus.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        return _obj


