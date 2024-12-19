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
from github_openapi.models.repository_ruleset_conditions import RepositoryRulesetConditions
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges
from typing import Optional, Set
from typing_extensions import Self

class WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner(BaseModel):
    """
    WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner
    """ # noqa: E501
    condition: Optional[RepositoryRulesetConditions] = None
    changes: Optional[WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges] = None
    __properties: ClassVar[List[str]] = ["condition", "changes"]

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
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of condition
        if self.condition:
            _dict['condition'] = self.condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of changes
        if self.changes:
            _dict['changes'] = self.changes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "condition": RepositoryRulesetConditions.from_dict(obj["condition"]) if obj.get("condition") is not None else None,
            "changes": WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges.from_dict(obj["changes"]) if obj.get("changes") is not None else None
        })
        return _obj


