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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from github_openapi.models.custom_property_default_value import CustomPropertyDefaultValue
from typing import Optional, Set
from typing_extensions import Self

class CustomProperty(BaseModel):
    """
    Custom property defined on an organization
    """ # noqa: E501
    property_name: StrictStr = Field(description="The name of the property")
    url: Optional[StrictStr] = Field(default=None, description="The URL that can be used to fetch, update, or delete info about this property via the API.")
    source_type: Optional[StrictStr] = Field(default=None, description="The source type of the property")
    value_type: StrictStr = Field(description="The type of the value for the property")
    required: Optional[StrictBool] = Field(default=None, description="Whether the property is required.")
    default_value: Optional[CustomPropertyDefaultValue] = None
    description: Optional[StrictStr] = Field(default=None, description="Short description of the property")
    allowed_values: Optional[Annotated[List[Annotated[str, Field(strict=True, max_length=75)]], Field(max_length=200)]] = Field(default=None, description="An ordered list of the allowed values of the property. The property can have up to 200 allowed values.")
    values_editable_by: Optional[StrictStr] = Field(default=None, description="Who can edit the values of the property")
    __properties: ClassVar[List[str]] = ["property_name", "url", "source_type", "value_type", "required", "default_value", "description", "allowed_values", "values_editable_by"]

    @field_validator('source_type')
    def source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['organization', 'enterprise']):
            raise ValueError("must be one of enum values ('organization', 'enterprise')")
        return value

    @field_validator('value_type')
    def value_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['string', 'single_select', 'multi_select', 'true_false']):
            raise ValueError("must be one of enum values ('string', 'single_select', 'multi_select', 'true_false')")
        return value

    @field_validator('values_editable_by')
    def values_editable_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['org_actors', 'org_and_repo_actors']):
            raise ValueError("must be one of enum values ('org_actors', 'org_and_repo_actors')")
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
        """Create an instance of CustomProperty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_value
        if self.default_value:
            _dict['default_value'] = self.default_value.to_dict()
        # set to None if default_value (nullable) is None
        # and model_fields_set contains the field
        if self.default_value is None and "default_value" in self.model_fields_set:
            _dict['default_value'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if allowed_values (nullable) is None
        # and model_fields_set contains the field
        if self.allowed_values is None and "allowed_values" in self.model_fields_set:
            _dict['allowed_values'] = None

        # set to None if values_editable_by (nullable) is None
        # and model_fields_set contains the field
        if self.values_editable_by is None and "values_editable_by" in self.model_fields_set:
            _dict['values_editable_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "property_name": obj.get("property_name"),
            "url": obj.get("url"),
            "source_type": obj.get("source_type"),
            "value_type": obj.get("value_type"),
            "required": obj.get("required"),
            "default_value": CustomPropertyDefaultValue.from_dict(obj["default_value"]) if obj.get("default_value") is not None else None,
            "description": obj.get("description"),
            "allowed_values": obj.get("allowed_values"),
            "values_editable_by": obj.get("values_editable_by")
        })
        return _obj

