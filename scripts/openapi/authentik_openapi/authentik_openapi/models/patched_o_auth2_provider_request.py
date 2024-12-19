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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.client_type_enum import ClientTypeEnum
from authentik_openapi.models.issuer_mode_enum import IssuerModeEnum
from authentik_openapi.models.sub_mode_enum import SubModeEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedOAuth2ProviderRequest(BaseModel):
    """
    OAuth2Provider Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: Optional[StrictStr] = Field(default=None, description="Flow used when authorizing this provider.")
    property_mappings: Optional[List[StrictStr]] = None
    client_type: Optional[ClientTypeEnum] = Field(default=None, description="Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable")
    client_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    client_secret: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    access_code_validity: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Access codes not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    access_token_validity: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    refresh_token_validity: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    include_claims_in_id_token: Optional[StrictBool] = Field(default=None, description="Include User claims from scopes in the id_token, for applications that don't access the userinfo endpoint.")
    signing_key: Optional[StrictStr] = Field(default=None, description="Key used to sign the tokens. Only required when JWT Algorithm is set to RS256.")
    redirect_uris: Optional[StrictStr] = Field(default=None, description="Enter each URI on a new line.")
    sub_mode: Optional[SubModeEnum] = Field(default=None, description="Configure what data should be used as unique User Identifier. For most cases, the default should be fine.")
    issuer_mode: Optional[IssuerModeEnum] = Field(default=None, description="Configure how the issuer field of the ID Token should be filled.")
    jwks_sources: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["name", "authentication_flow", "authorization_flow", "property_mappings", "client_type", "client_id", "client_secret", "access_code_validity", "access_token_validity", "refresh_token_validity", "include_claims_in_id_token", "signing_key", "redirect_uris", "sub_mode", "issuer_mode", "jwks_sources"]

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
        """Create an instance of PatchedOAuth2ProviderRequest from a JSON string"""
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
        # set to None if authentication_flow (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_flow is None and "authentication_flow" in self.model_fields_set:
            _dict['authentication_flow'] = None

        # set to None if signing_key (nullable) is None
        # and model_fields_set contains the field
        if self.signing_key is None and "signing_key" in self.model_fields_set:
            _dict['signing_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedOAuth2ProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "client_type": obj.get("client_type"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "access_code_validity": obj.get("access_code_validity"),
            "access_token_validity": obj.get("access_token_validity"),
            "refresh_token_validity": obj.get("refresh_token_validity"),
            "include_claims_in_id_token": obj.get("include_claims_in_id_token"),
            "signing_key": obj.get("signing_key"),
            "redirect_uris": obj.get("redirect_uris"),
            "sub_mode": obj.get("sub_mode"),
            "issuer_mode": obj.get("issuer_mode"),
            "jwks_sources": obj.get("jwks_sources")
        })
        return _obj


