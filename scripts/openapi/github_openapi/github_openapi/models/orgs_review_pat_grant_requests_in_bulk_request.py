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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrgsReviewPatGrantRequestsInBulkRequest(BaseModel):
    """
    OrgsReviewPatGrantRequestsInBulkRequest
    """ # noqa: E501
    pat_request_ids: Optional[Annotated[List[StrictInt], Field(min_length=1, max_length=100)]] = Field(default=None, description="Unique identifiers of the requests for access via fine-grained personal access token. Must be formed of between 1 and 100 `pat_request_id` values.")
    action: StrictStr = Field(description="Action to apply to the requests.")
    reason: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Reason for approving or denying the requests. Max 1024 characters.")
    __properties: ClassVar[List[str]] = ["pat_request_ids", "action", "reason"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['approve', 'deny']):
            raise ValueError("must be one of enum values ('approve', 'deny')")
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
        """Create an instance of OrgsReviewPatGrantRequestsInBulkRequest from a JSON string"""
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
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrgsReviewPatGrantRequestsInBulkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pat_request_ids": obj.get("pat_request_ids"),
            "action": obj.get("action"),
            "reason": obj.get("reason")
        })
        return _obj


