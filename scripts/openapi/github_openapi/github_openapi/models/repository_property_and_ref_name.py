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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.repository_ruleset_conditions_ref_name import RepositoryRulesetConditionsRefName
from github_openapi.models.repository_ruleset_conditions_repository_property_target_repository_property import RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty
from typing import Optional, Set
from typing_extensions import Self

class RepositoryPropertyAndRefName(BaseModel):
    """
    Conditions to target repositories by property and refs by name
    """ # noqa: E501
    ref_name: Optional[RepositoryRulesetConditionsRefName] = None
    repository_property: RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty
    __properties: ClassVar[List[str]] = ["ref_name", "repository_property"]

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
        """Create an instance of RepositoryPropertyAndRefName from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ref_name
        if self.ref_name:
            _dict['ref_name'] = self.ref_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository_property
        if self.repository_property:
            _dict['repository_property'] = self.repository_property.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RepositoryPropertyAndRefName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ref_name": RepositoryRulesetConditionsRefName.from_dict(obj["ref_name"]) if obj.get("ref_name") is not None else None,
            "repository_property": RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.from_dict(obj["repository_property"]) if obj.get("repository_property") is not None else None
        })
        return _obj


