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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, SecretStr, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Webhook(BaseModel):
    """
    Webhook
    """ # noqa: E501
    endpoint_id: Optional[StrictStr] = Field(default=None, description="ID of the webhook endpoint. ", alias="endpointId")
    endpoint_url: Optional[StrictStr] = Field(default=None, description="The endpoint that events are sent to from Tailscale via POST requests. ", alias="endpointUrl")
    provider_type: Optional[StrictStr] = Field(default=None, description="The provider type for the webhook destination, or an empty string if none are applicable. Outgoing webhook events are sent in the format expected by the provider type if non-empty. ", alias="providerType")
    creator_login_name: Optional[StrictStr] = Field(default=None, description="The login name for the creator of the webhook endpoint. In some cases, such as webhooks created with an OAuth client, this can be blank. ", alias="creatorLoginName")
    created: Optional[datetime] = Field(default=None, description="The time the webhook endpoint was created. ")
    last_modified: Optional[datetime] = Field(default=None, description="The time the webhook endpoint was last modified. ", alias="lastModified")
    subscriptions: Optional[List[StrictStr]] = Field(default=None, description="The list of subscribed events that trigger POST requests to the configured endpoint URL. Learn more about [webhook events](/kb/1213/webhooks#events). ")
    secret: Optional[SecretStr] = Field(default=None, description="The webhook secret associated with the endpoint. Only populated on creation or when the secret is rotated.  This secret is used for generating the `Tailscale-Webhook-Signature` header in requests sent to the endpoint URL. Learn more about [verifying webhook event signatures](/kb/1213/webhooks#verifying-an-event-signature). ")
    __properties: ClassVar[List[str]] = ["endpointId", "endpointUrl", "providerType", "creatorLoginName", "created", "lastModified", "subscriptions", "secret"]

    @field_validator('provider_type')
    def provider_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['slack', 'mattermost', 'googlechat', 'discord']):
            raise ValueError("must be one of enum values ('slack', 'mattermost', 'googlechat', 'discord')")
        return value

    @field_validator('subscriptions')
    def subscriptions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['nodeCreated', 'nodeNeedsApproval', 'nodeApproved', 'nodeKeyExpiringInOneDay', 'nodeKeyExpired', 'nodeDeleted', 'policyUpdate', 'userCreated', 'userNeedsApproval', 'userSuspended', 'userRestored', 'userDeleted', 'userApproved', 'userRoleUpdated', 'subnetIPForwardingNotEnabled', 'exitNodeIPForwardingNotEnabled']):
                raise ValueError("each list item must be one of ('nodeCreated', 'nodeNeedsApproval', 'nodeApproved', 'nodeKeyExpiringInOneDay', 'nodeKeyExpired', 'nodeDeleted', 'policyUpdate', 'userCreated', 'userNeedsApproval', 'userSuspended', 'userRestored', 'userDeleted', 'userApproved', 'userRoleUpdated', 'subnetIPForwardingNotEnabled', 'exitNodeIPForwardingNotEnabled')")
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
        """Create an instance of Webhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Webhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endpointId": obj.get("endpointId"),
            "endpointUrl": obj.get("endpointUrl"),
            "providerType": obj.get("providerType"),
            "creatorLoginName": obj.get("creatorLoginName"),
            "created": obj.get("created"),
            "lastModified": obj.get("lastModified"),
            "subscriptions": obj.get("subscriptions"),
            "secret": obj.get("secret")
        })
        return _obj


