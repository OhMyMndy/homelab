# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ActionsUpdateOrgVariableRequest(BaseModel):
    """
    ActionsUpdateOrgVariableRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the variable.")
    value: Optional[StrictStr] = Field(default=None, description="The value of the variable.")
    visibility: Optional[StrictStr] = Field(default=None, description="The type of repositories in the organization that can access the variable. `selected` means only the repositories specified by `selected_repository_ids` can access the variable.")
    selected_repository_ids: Optional[List[StrictInt]] = Field(default=None, description="An array of repository ids that can access the organization variable. You can only provide a list of repository ids when the `visibility` is set to `selected`.")
    __properties: ClassVar[List[str]] = ["name", "value", "visibility", "selected_repository_ids"]

    @field_validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['all', 'private', 'selected']):
            raise ValueError("must be one of enum values ('all', 'private', 'selected')")
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
        """Create an instance of ActionsUpdateOrgVariableRequest from a JSON string"""
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
        """Create an instance of ActionsUpdateOrgVariableRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "value": obj.get("value"),
            "visibility": obj.get("visibility"),
            "selected_repository_ids": obj.get("selected_repository_ids")
        })
        return _obj


