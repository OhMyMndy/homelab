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
from github_openapi.models.repository_rule_commit_message_pattern_parameters import RepositoryRuleCommitMessagePatternParameters
from typing import Optional, Set
from typing_extensions import Self

class RepositoryRuleDetailedOneOf13(BaseModel):
    """
    RepositoryRuleDetailedOneOf13
    """ # noqa: E501
    type: StrictStr
    parameters: Optional[RepositoryRuleCommitMessagePatternParameters] = None
    ruleset_source_type: Optional[StrictStr] = Field(default=None, description="The type of source for the ruleset that includes this rule.")
    ruleset_source: Optional[StrictStr] = Field(default=None, description="The name of the source of the ruleset that includes this rule.")
    ruleset_id: Optional[StrictInt] = Field(default=None, description="The ID of the ruleset that includes this rule.")
    __properties: ClassVar[List[str]] = ["type", "parameters", "ruleset_source_type", "ruleset_source", "ruleset_id"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['branch_name_pattern']):
            raise ValueError("must be one of enum values ('branch_name_pattern')")
        return value

    @field_validator('ruleset_source_type')
    def ruleset_source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Repository', 'Organization']):
            raise ValueError("must be one of enum values ('Repository', 'Organization')")
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
        """Create an instance of RepositoryRuleDetailedOneOf13 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RepositoryRuleDetailedOneOf13 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "parameters": RepositoryRuleCommitMessagePatternParameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "ruleset_source_type": obj.get("ruleset_source_type"),
            "ruleset_source": obj.get("ruleset_source"),
            "ruleset_id": obj.get("ruleset_id")
        })
        return _obj


