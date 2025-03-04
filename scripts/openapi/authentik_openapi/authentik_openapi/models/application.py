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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
from authentik_openapi.models.provider import Provider
from typing import Optional, Set
from typing_extensions import Self

class Application(BaseModel):
    """
    Application Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr = Field(description="Application's display Name.")
    slug: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Internal application name, used in URLs.")
    provider: Optional[StrictInt] = None
    provider_obj: Provider
    backchannel_providers: Optional[List[StrictInt]] = None
    backchannel_providers_obj: List[Provider]
    launch_url: Optional[StrictStr] = Field(description="Allow formatting of launch URL")
    open_in_new_tab: Optional[StrictBool] = Field(default=None, description="Open launch URL in a new browser tab or window.")
    meta_launch_url: Optional[StrictStr] = None
    meta_icon: Optional[StrictStr] = Field(description="Get the URL to the App Icon image. If the name is /static or starts with http it is returned as-is")
    meta_description: Optional[StrictStr] = None
    meta_publisher: Optional[StrictStr] = None
    policy_engine_mode: Optional[PolicyEngineMode] = None
    group: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["pk", "name", "slug", "provider", "provider_obj", "backchannel_providers", "backchannel_providers_obj", "launch_url", "open_in_new_tab", "meta_launch_url", "meta_icon", "meta_description", "meta_publisher", "policy_engine_mode", "group"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
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
        """Create an instance of Application from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pk",
            "provider_obj",
            "backchannel_providers_obj",
            "launch_url",
            "meta_icon",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of provider_obj
        if self.provider_obj:
            _dict['provider_obj'] = self.provider_obj.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in backchannel_providers_obj (list)
        _items = []
        if self.backchannel_providers_obj:
            for _item_backchannel_providers_obj in self.backchannel_providers_obj:
                if _item_backchannel_providers_obj:
                    _items.append(_item_backchannel_providers_obj.to_dict())
            _dict['backchannel_providers_obj'] = _items
        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if launch_url (nullable) is None
        # and model_fields_set contains the field
        if self.launch_url is None and "launch_url" in self.model_fields_set:
            _dict['launch_url'] = None

        # set to None if meta_icon (nullable) is None
        # and model_fields_set contains the field
        if self.meta_icon is None and "meta_icon" in self.model_fields_set:
            _dict['meta_icon'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Application from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "provider": obj.get("provider"),
            "provider_obj": Provider.from_dict(obj["provider_obj"]) if obj.get("provider_obj") is not None else None,
            "backchannel_providers": obj.get("backchannel_providers"),
            "backchannel_providers_obj": [Provider.from_dict(_item) for _item in obj["backchannel_providers_obj"]] if obj.get("backchannel_providers_obj") is not None else None,
            "launch_url": obj.get("launch_url"),
            "open_in_new_tab": obj.get("open_in_new_tab"),
            "meta_launch_url": obj.get("meta_launch_url"),
            "meta_icon": obj.get("meta_icon"),
            "meta_description": obj.get("meta_description"),
            "meta_publisher": obj.get("meta_publisher"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "group": obj.get("group")
        })
        return _obj


