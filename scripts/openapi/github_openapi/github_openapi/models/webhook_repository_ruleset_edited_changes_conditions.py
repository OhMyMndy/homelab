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
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner
from typing import Optional, Set
from typing_extensions import Self

class WebhookRepositoryRulesetEditedChangesConditions(BaseModel):
    """
    WebhookRepositoryRulesetEditedChangesConditions
    """ # noqa: E501
    added: Optional[List[RepositoryRulesetConditions]] = None
    deleted: Optional[List[RepositoryRulesetConditions]] = None
    updated: Optional[List[WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner]] = None
    __properties: ClassVar[List[str]] = ["added", "deleted", "updated"]

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
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in added (list)
        _items = []
        if self.added:
            for _item_added in self.added:
                if _item_added:
                    _items.append(_item_added.to_dict())
            _dict['added'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in deleted (list)
        _items = []
        if self.deleted:
            for _item_deleted in self.deleted:
                if _item_deleted:
                    _items.append(_item_deleted.to_dict())
            _dict['deleted'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in updated (list)
        _items = []
        if self.updated:
            for _item_updated in self.updated:
                if _item_updated:
                    _items.append(_item_updated.to_dict())
            _dict['updated'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookRepositoryRulesetEditedChangesConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "added": [RepositoryRulesetConditions.from_dict(_item) for _item in obj["added"]] if obj.get("added") is not None else None,
            "deleted": [RepositoryRulesetConditions.from_dict(_item) for _item in obj["deleted"]] if obj.get("deleted") is not None else None,
            "updated": [WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner.from_dict(_item) for _item in obj["updated"]] if obj.get("updated") is not None else None
        })
        return _obj

