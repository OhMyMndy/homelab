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
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.copilot_seat_details import CopilotSeatDetails
from typing import Optional, Set
from typing_extensions import Self

class CopilotListCopilotSeats200Response(BaseModel):
    """
    CopilotListCopilotSeats200Response
    """ # noqa: E501
    total_seats: Optional[StrictInt] = Field(default=None, description="Total number of Copilot seats for the organization currently being billed.")
    seats: Optional[List[CopilotSeatDetails]] = None
    __properties: ClassVar[List[str]] = ["total_seats", "seats"]

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
        """Create an instance of CopilotListCopilotSeats200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in seats (list)
        _items = []
        if self.seats:
            for _item_seats in self.seats:
                if _item_seats:
                    _items.append(_item_seats.to_dict())
            _dict['seats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CopilotListCopilotSeats200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_seats": obj.get("total_seats"),
            "seats": [CopilotSeatDetails.from_dict(_item) for _item in obj["seats"]] if obj.get("seats") is not None else None
        })
        return _obj


