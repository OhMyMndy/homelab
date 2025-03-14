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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebhookCodeScanningAlertClosedByUserAlertRule(BaseModel):
    """
    WebhookCodeScanningAlertClosedByUserAlertRule
    """ # noqa: E501
    description: StrictStr = Field(description="A short description of the rule used to detect the alert.")
    full_description: Optional[StrictStr] = None
    help: Optional[StrictStr] = None
    help_uri: Optional[StrictStr] = Field(default=None, description="A link to the documentation for the rule used to detect the alert.")
    id: StrictStr = Field(description="A unique identifier for the rule used to detect the alert.")
    name: Optional[StrictStr] = None
    severity: Optional[StrictStr] = Field(description="The severity of the alert.")
    tags: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["description", "full_description", "help", "help_uri", "id", "name", "severity", "tags"]

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'note', 'warning', 'error']):
            raise ValueError("must be one of enum values ('none', 'note', 'warning', 'error')")
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
        """Create an instance of WebhookCodeScanningAlertClosedByUserAlertRule from a JSON string"""
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
        # set to None if help (nullable) is None
        # and model_fields_set contains the field
        if self.help is None and "help" in self.model_fields_set:
            _dict['help'] = None

        # set to None if help_uri (nullable) is None
        # and model_fields_set contains the field
        if self.help_uri is None and "help_uri" in self.model_fields_set:
            _dict['help_uri'] = None

        # set to None if severity (nullable) is None
        # and model_fields_set contains the field
        if self.severity is None and "severity" in self.model_fields_set:
            _dict['severity'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookCodeScanningAlertClosedByUserAlertRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "full_description": obj.get("full_description"),
            "help": obj.get("help"),
            "help_uri": obj.get("help_uri"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "severity": obj.get("severity"),
            "tags": obj.get("tags")
        })
        return _obj


