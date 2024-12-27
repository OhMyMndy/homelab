# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from authentik_openapi.models.open_id_connect_configuration import OpenIDConnectConfiguration
from authentik_openapi.models.proxy_mode import ProxyMode
from typing import Optional, Set
from typing_extensions import Self

class ProxyOutpostConfig(BaseModel):
    """
    Proxy provider serializer for outposts
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    internal_host: Optional[StrictStr] = None
    external_host: StrictStr
    internal_host_ssl_validation: Optional[StrictBool] = Field(default=None, description="Validate SSL Certificates of upstream servers")
    client_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    client_secret: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    oidc_configuration: OpenIDConnectConfiguration
    cookie_secret: Optional[StrictStr] = None
    certificate: Optional[StrictStr] = None
    skip_path_regex: Optional[StrictStr] = Field(default=None, description="Regular expressions for which authentication is not required. Each new line is interpreted as a new Regular Expression.")
    basic_auth_enabled: Optional[StrictBool] = Field(default=None, description="Set a custom HTTP-Basic Authentication header based on values from authentik.")
    basic_auth_password_attribute: Optional[StrictStr] = Field(default=None, description="User/Group Attribute used for the password part of the HTTP-Basic Header.")
    basic_auth_user_attribute: Optional[StrictStr] = Field(default=None, description="User/Group Attribute used for the user part of the HTTP-Basic Header. If not set, the user's Email address is used.")
    mode: Optional[ProxyMode] = Field(default=None, description="Enable support for forwardAuth in traefik and nginx auth_request. Exclusive with internal_host.")
    cookie_domain: Optional[StrictStr] = None
    access_token_validity: Optional[Union[StrictFloat, StrictInt]] = Field(description="Get token validity as second count")
    intercept_header_auth: Optional[StrictBool] = Field(default=None, description="When enabled, this provider will intercept the authorization header and authenticate requests based on its value.")
    scopes_to_request: List[StrictStr] = Field(description="Get all the scope names the outpost should request, including custom-defined ones")
    assigned_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_application_name: StrictStr = Field(description="Application's display Name.")
    __properties: ClassVar[List[str]] = ["pk", "name", "internal_host", "external_host", "internal_host_ssl_validation", "client_id", "client_secret", "oidc_configuration", "cookie_secret", "certificate", "skip_path_regex", "basic_auth_enabled", "basic_auth_password_attribute", "basic_auth_user_attribute", "mode", "cookie_domain", "access_token_validity", "intercept_header_auth", "scopes_to_request", "assigned_application_slug", "assigned_application_name"]

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
        """Create an instance of ProxyOutpostConfig from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "oidc_configuration",
            "access_token_validity",
            "scopes_to_request",
            "assigned_application_slug",
            "assigned_application_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of oidc_configuration
        if self.oidc_configuration:
            _dict['oidc_configuration'] = self.oidc_configuration.to_dict()
        # set to None if certificate (nullable) is None
        # and model_fields_set contains the field
        if self.certificate is None and "certificate" in self.model_fields_set:
            _dict['certificate'] = None

        # set to None if access_token_validity (nullable) is None
        # and model_fields_set contains the field
        if self.access_token_validity is None and "access_token_validity" in self.model_fields_set:
            _dict['access_token_validity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProxyOutpostConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "internal_host": obj.get("internal_host"),
            "external_host": obj.get("external_host"),
            "internal_host_ssl_validation": obj.get("internal_host_ssl_validation"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "oidc_configuration": OpenIDConnectConfiguration.from_dict(obj["oidc_configuration"]) if obj.get("oidc_configuration") is not None else None,
            "cookie_secret": obj.get("cookie_secret"),
            "certificate": obj.get("certificate"),
            "skip_path_regex": obj.get("skip_path_regex"),
            "basic_auth_enabled": obj.get("basic_auth_enabled"),
            "basic_auth_password_attribute": obj.get("basic_auth_password_attribute"),
            "basic_auth_user_attribute": obj.get("basic_auth_user_attribute"),
            "mode": obj.get("mode"),
            "cookie_domain": obj.get("cookie_domain"),
            "access_token_validity": obj.get("access_token_validity"),
            "intercept_header_auth": obj.get("intercept_header_auth"),
            "scopes_to_request": obj.get("scopes_to_request"),
            "assigned_application_slug": obj.get("assigned_application_slug"),
            "assigned_application_name": obj.get("assigned_application_name")
        })
        return _obj

