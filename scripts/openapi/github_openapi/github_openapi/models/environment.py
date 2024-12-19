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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment_branch_policy_settings import DeploymentBranchPolicySettings
from github_openapi.models.environment_protection_rules_inner import EnvironmentProtectionRulesInner
from typing import Optional, Set
from typing_extensions import Self

class Environment(BaseModel):
    """
    Details of a deployment environment
    """ # noqa: E501
    id: StrictInt = Field(description="The id of the environment.")
    node_id: StrictStr
    name: StrictStr = Field(description="The name of the environment.")
    url: StrictStr
    html_url: StrictStr
    created_at: datetime = Field(description="The time that the environment was created, in ISO 8601 format.")
    updated_at: datetime = Field(description="The time that the environment was last updated, in ISO 8601 format.")
    protection_rules: Optional[List[EnvironmentProtectionRulesInner]] = Field(default=None, description="Built-in deployment protection rules for the environment.")
    deployment_branch_policy: Optional[DeploymentBranchPolicySettings] = None
    __properties: ClassVar[List[str]] = ["id", "node_id", "name", "url", "html_url", "created_at", "updated_at", "protection_rules", "deployment_branch_policy"]

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
        """Create an instance of Environment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in protection_rules (list)
        _items = []
        if self.protection_rules:
            for _item_protection_rules in self.protection_rules:
                if _item_protection_rules:
                    _items.append(_item_protection_rules.to_dict())
            _dict['protection_rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of deployment_branch_policy
        if self.deployment_branch_policy:
            _dict['deployment_branch_policy'] = self.deployment_branch_policy.to_dict()
        # set to None if deployment_branch_policy (nullable) is None
        # and model_fields_set contains the field
        if self.deployment_branch_policy is None and "deployment_branch_policy" in self.model_fields_set:
            _dict['deployment_branch_policy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Environment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "protection_rules": [EnvironmentProtectionRulesInner.from_dict(_item) for _item in obj["protection_rules"]] if obj.get("protection_rules") is not None else None,
            "deployment_branch_policy": DeploymentBranchPolicySettings.from_dict(obj["deployment_branch_policy"]) if obj.get("deployment_branch_policy") is not None else None
        })
        return _obj

