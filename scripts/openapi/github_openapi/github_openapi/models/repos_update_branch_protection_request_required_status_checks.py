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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.repos_update_branch_protection_request_required_status_checks_checks_inner import ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner
from typing import Optional, Set
from typing_extensions import Self

class ReposUpdateBranchProtectionRequestRequiredStatusChecks(BaseModel):
    """
    Require status checks to pass before merging. Set to `null` to disable.
    """ # noqa: E501
    strict: StrictBool = Field(description="Require branches to be up to date before merging.")
    contexts: List[StrictStr] = Field(description="**Closing down notice**: The list of status checks to require in order to merge into this branch. If any of these checks have recently been set by a particular GitHub App, they will be required to come from that app in future for the branch to merge. Use `checks` instead of `contexts` for more fine-grained control.")
    checks: Optional[List[ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner]] = Field(default=None, description="The list of status checks to require in order to merge into this branch.")
    __properties: ClassVar[List[str]] = ["strict", "contexts", "checks"]

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
        """Create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item_checks in self.checks:
                if _item_checks:
                    _items.append(_item_checks.to_dict())
            _dict['checks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReposUpdateBranchProtectionRequestRequiredStatusChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "strict": obj.get("strict"),
            "contexts": obj.get("contexts"),
            "checks": [ReposUpdateBranchProtectionRequestRequiredStatusChecksChecksInner.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None
        })
        return _obj


