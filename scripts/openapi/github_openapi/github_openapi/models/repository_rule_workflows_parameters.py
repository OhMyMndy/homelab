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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.repository_rule_params_workflow_file_reference import RepositoryRuleParamsWorkflowFileReference
from typing import Optional, Set
from typing_extensions import Self

class RepositoryRuleWorkflowsParameters(BaseModel):
    """
    RepositoryRuleWorkflowsParameters
    """ # noqa: E501
    do_not_enforce_on_create: Optional[StrictBool] = Field(default=None, description="Allow repositories and branches to be created if a check would otherwise prohibit it.")
    workflows: List[RepositoryRuleParamsWorkflowFileReference] = Field(description="Workflows that must pass for this rule to pass.")
    __properties: ClassVar[List[str]] = ["do_not_enforce_on_create", "workflows"]

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
        """Create an instance of RepositoryRuleWorkflowsParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in workflows (list)
        _items = []
        if self.workflows:
            for _item_workflows in self.workflows:
                if _item_workflows:
                    _items.append(_item_workflows.to_dict())
            _dict['workflows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RepositoryRuleWorkflowsParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "do_not_enforce_on_create": obj.get("do_not_enforce_on_create"),
            "workflows": [RepositoryRuleParamsWorkflowFileReference.from_dict(_item) for _item in obj["workflows"]] if obj.get("workflows") is not None else None
        })
        return _obj


