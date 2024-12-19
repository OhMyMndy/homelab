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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CombinedBillingUsage(BaseModel):
    """
    CombinedBillingUsage
    """ # noqa: E501
    days_left_in_billing_cycle: StrictInt = Field(description="Numbers of days left in billing cycle.")
    estimated_paid_storage_for_month: StrictInt = Field(description="Estimated storage space (GB) used in billing cycle.")
    estimated_storage_for_month: StrictInt = Field(description="Estimated sum of free and paid storage space (GB) used in billing cycle.")
    __properties: ClassVar[List[str]] = ["days_left_in_billing_cycle", "estimated_paid_storage_for_month", "estimated_storage_for_month"]

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
        """Create an instance of CombinedBillingUsage from a JSON string"""
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
        """Create an instance of CombinedBillingUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "days_left_in_billing_cycle": obj.get("days_left_in_billing_cycle"),
            "estimated_paid_storage_for_month": obj.get("estimated_paid_storage_for_month"),
            "estimated_storage_for_month": obj.get("estimated_storage_for_month")
        })
        return _obj


