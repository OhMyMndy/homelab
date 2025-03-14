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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SettingsRequest(BaseModel):
    """
    Settings Serializer
    """ # noqa: E501
    avatars: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Configure how authentik should show avatars for users.")
    default_user_change_name: Optional[StrictBool] = Field(default=None, description="Enable the ability for users to change their name.")
    default_user_change_email: Optional[StrictBool] = Field(default=None, description="Enable the ability for users to change their email address.")
    default_user_change_username: Optional[StrictBool] = Field(default=None, description="Enable the ability for users to change their username.")
    event_retention: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Events will be deleted after this duration.(Format: weeks=3;days=2;hours=3,seconds=2).")
    footer_links: Optional[Any] = Field(default=None, description="The option configures the footer links on the flow executor pages.")
    gdpr_compliance: Optional[StrictBool] = Field(default=None, description="When enabled, all the events caused by a user will be deleted upon the user's deletion.")
    impersonation: Optional[StrictBool] = Field(default=None, description="Globally enable/disable impersonation.")
    default_token_duration: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Default token duration")
    default_token_length: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = Field(default=None, description="Default token length")
    __properties: ClassVar[List[str]] = ["avatars", "default_user_change_name", "default_user_change_email", "default_user_change_username", "event_retention", "footer_links", "gdpr_compliance", "impersonation", "default_token_duration", "default_token_length"]

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
        """Create an instance of SettingsRequest from a JSON string"""
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
        # set to None if footer_links (nullable) is None
        # and model_fields_set contains the field
        if self.footer_links is None and "footer_links" in self.model_fields_set:
            _dict['footer_links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SettingsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatars": obj.get("avatars"),
            "default_user_change_name": obj.get("default_user_change_name"),
            "default_user_change_email": obj.get("default_user_change_email"),
            "default_user_change_username": obj.get("default_user_change_username"),
            "event_retention": obj.get("event_retention"),
            "footer_links": obj.get("footer_links"),
            "gdpr_compliance": obj.get("gdpr_compliance"),
            "impersonation": obj.get("impersonation"),
            "default_token_duration": obj.get("default_token_duration"),
            "default_token_length": obj.get("default_token_length")
        })
        return _obj


