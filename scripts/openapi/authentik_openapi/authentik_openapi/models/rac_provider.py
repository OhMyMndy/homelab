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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RACProvider(BaseModel):
    """
    RACProvider Serializer
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: StrictStr = Field(description="Flow used when authorizing this provider.")
    property_mappings: Optional[List[StrictStr]] = None
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    assigned_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_application_name: StrictStr = Field(description="Application's display Name.")
    assigned_backchannel_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_backchannel_application_name: StrictStr = Field(description="Application's display Name.")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    settings: Optional[Any] = None
    outpost_set: List[StrictStr]
    connection_expiry: Optional[StrictStr] = Field(default=None, description="Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours=-1;minutes=-2;seconds=-3)")
    delete_token_on_disconnect: Optional[StrictBool] = Field(default=None, description="When set to true, connection tokens will be deleted upon disconnect.")
    __properties: ClassVar[List[str]] = ["pk", "name", "authentication_flow", "authorization_flow", "property_mappings", "component", "assigned_application_slug", "assigned_application_name", "assigned_backchannel_application_slug", "assigned_backchannel_application_name", "verbose_name", "verbose_name_plural", "meta_model_name", "settings", "outpost_set", "connection_expiry", "delete_token_on_disconnect"]

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
        """Create an instance of RACProvider from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "component",
            "assigned_application_slug",
            "assigned_application_name",
            "assigned_backchannel_application_slug",
            "assigned_backchannel_application_name",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
            "outpost_set",
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

        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RACProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "component": obj.get("component"),
            "assigned_application_slug": obj.get("assigned_application_slug"),
            "assigned_application_name": obj.get("assigned_application_name"),
            "assigned_backchannel_application_slug": obj.get("assigned_backchannel_application_slug"),
            "assigned_backchannel_application_name": obj.get("assigned_backchannel_application_name"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "settings": obj.get("settings"),
            "outpost_set": obj.get("outpost_set"),
            "connection_expiry": obj.get("connection_expiry"),
            "delete_token_on_disconnect": obj.get("delete_token_on_disconnect")
        })
        return _obj


