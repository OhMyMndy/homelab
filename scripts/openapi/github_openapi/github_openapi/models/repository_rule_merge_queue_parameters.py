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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RepositoryRuleMergeQueueParameters(BaseModel):
    """
    RepositoryRuleMergeQueueParameters
    """ # noqa: E501
    check_response_timeout_minutes: Annotated[int, Field(le=360, strict=True, ge=1)] = Field(description="Maximum time for a required status check to report a conclusion. After this much time has elapsed, checks that have not reported a conclusion will be assumed to have failed")
    grouping_strategy: StrictStr = Field(description="When set to ALLGREEN, the merge commit created by merge queue for each PR in the group must pass all required checks to merge. When set to HEADGREEN, only the commit at the head of the merge group, i.e. the commit containing changes from all of the PRs in the group, must pass its required checks to merge.")
    max_entries_to_build: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="Limit the number of queued pull requests requesting checks and workflow runs at the same time.")
    max_entries_to_merge: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="The maximum number of PRs that will be merged together in a group.")
    merge_method: StrictStr = Field(description="Method to use when merging changes from queued pull requests.")
    min_entries_to_merge: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="The minimum number of PRs that will be merged together in a group.")
    min_entries_to_merge_wait_minutes: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="The time merge queue should wait after the first PR is added to the queue for the minimum group size to be met. After this time has elapsed, the minimum group size will be ignored and a smaller group will be merged.")
    __properties: ClassVar[List[str]] = ["check_response_timeout_minutes", "grouping_strategy", "max_entries_to_build", "max_entries_to_merge", "merge_method", "min_entries_to_merge", "min_entries_to_merge_wait_minutes"]

    @field_validator('grouping_strategy')
    def grouping_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ALLGREEN', 'HEADGREEN']):
            raise ValueError("must be one of enum values ('ALLGREEN', 'HEADGREEN')")
        return value

    @field_validator('merge_method')
    def merge_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MERGE', 'SQUASH', 'REBASE']):
            raise ValueError("must be one of enum values ('MERGE', 'SQUASH', 'REBASE')")
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
        """Create an instance of RepositoryRuleMergeQueueParameters from a JSON string"""
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
        """Create an instance of RepositoryRuleMergeQueueParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "check_response_timeout_minutes": obj.get("check_response_timeout_minutes"),
            "grouping_strategy": obj.get("grouping_strategy"),
            "max_entries_to_build": obj.get("max_entries_to_build"),
            "max_entries_to_merge": obj.get("max_entries_to_merge"),
            "merge_method": obj.get("merge_method"),
            "min_entries_to_merge": obj.get("min_entries_to_merge"),
            "min_entries_to_merge_wait_minutes": obj.get("min_entries_to_merge_wait_minutes")
        })
        return _obj

