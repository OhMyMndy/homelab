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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner(BaseModel):
    """
    CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner
    """ # noqa: E501
    reviewer_id: StrictInt = Field(description="The ID of the team or role selected as a bypass reviewer")
    reviewer_type: StrictStr = Field(description="The type of the bypass reviewer")
    __properties: ClassVar[List[str]] = ["reviewer_id", "reviewer_type"]

    @field_validator('reviewer_type')
    def reviewer_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TEAM', 'ROLE']):
            raise ValueError("must be one of enum values ('TEAM', 'ROLE')")
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
        """Create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner from a JSON string"""
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
        """Create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reviewer_id": obj.get("reviewer_id"),
            "reviewer_type": obj.get("reviewer_type")
        })
        return _obj


