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
from authentik_openapi.models.flow_set import FlowSet
from authentik_openapi.models.user_creation_mode_enum import UserCreationModeEnum
from authentik_openapi.models.user_type_enum import UserTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class UserWriteStage(BaseModel):
    """
    UserWriteStage Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    component: StrictStr = Field(description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    flow_set: Optional[List[FlowSet]] = None
    user_creation_mode: Optional[UserCreationModeEnum] = None
    create_users_as_inactive: Optional[StrictBool] = Field(default=None, description="When set, newly created users are inactive and cannot login.")
    create_users_group: Optional[StrictStr] = Field(default=None, description="Optionally add newly created users to this group.")
    user_type: Optional[UserTypeEnum] = None
    user_path_template: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "user_creation_mode", "create_users_as_inactive", "create_users_group", "user_type", "user_path_template"]

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
        """Create an instance of UserWriteStage from a JSON string"""
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
            "component",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item_flow_set in self.flow_set:
                if _item_flow_set:
                    _items.append(_item_flow_set.to_dict())
            _dict['flow_set'] = _items
        # set to None if create_users_group (nullable) is None
        # and model_fields_set contains the field
        if self.create_users_group is None and "create_users_group" in self.model_fields_set:
            _dict['create_users_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserWriteStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj["flow_set"]] if obj.get("flow_set") is not None else None,
            "user_creation_mode": obj.get("user_creation_mode"),
            "create_users_as_inactive": obj.get("create_users_as_inactive"),
            "create_users_group": obj.get("create_users_group"),
            "user_type": obj.get("user_type"),
            "user_path_template": obj.get("user_path_template")
        })
        return _obj

