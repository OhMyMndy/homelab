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
from github_openapi.models.webhook_organization_renamed_changes_login import WebhookOrganizationRenamedChangesLogin
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_include import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude
from typing import Optional, Set
from typing_extensions import Self

class WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges(BaseModel):
    """
    WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges
    """ # noqa: E501
    condition_type: Optional[WebhookOrganizationRenamedChangesLogin] = None
    target: Optional[WebhookOrganizationRenamedChangesLogin] = None
    include: Optional[WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude] = None
    exclude: Optional[WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude] = None
    __properties: ClassVar[List[str]] = ["condition_type", "target", "include", "exclude"]

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
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of condition_type
        if self.condition_type:
            _dict['condition_type'] = self.condition_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of include
        if self.include:
            _dict['include'] = self.include.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exclude
        if self.exclude:
            _dict['exclude'] = self.exclude.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "condition_type": WebhookOrganizationRenamedChangesLogin.from_dict(obj["condition_type"]) if obj.get("condition_type") is not None else None,
            "target": WebhookOrganizationRenamedChangesLogin.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "include": WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude.from_dict(obj["include"]) if obj.get("include") is not None else None,
            "exclude": WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude.from_dict(obj["exclude"]) if obj.get("exclude") is not None else None
        })
        return _obj


