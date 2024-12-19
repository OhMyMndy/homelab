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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiInsightsRouteStatsInner(BaseModel):
    """
    ApiInsightsRouteStatsInner
    """ # noqa: E501
    http_method: Optional[StrictStr] = Field(default=None, description="The HTTP method")
    api_route: Optional[StrictStr] = Field(default=None, description="The API path's route template")
    total_request_count: Optional[StrictInt] = Field(default=None, description="The total number of requests within the queried time period")
    rate_limited_request_count: Optional[StrictInt] = Field(default=None, description="The total number of requests that were rate limited within the queried time period")
    last_rate_limited_timestamp: Optional[StrictStr] = None
    last_request_timestamp: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["http_method", "api_route", "total_request_count", "rate_limited_request_count", "last_rate_limited_timestamp", "last_request_timestamp"]

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
        """Create an instance of ApiInsightsRouteStatsInner from a JSON string"""
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
        # set to None if last_rate_limited_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.last_rate_limited_timestamp is None and "last_rate_limited_timestamp" in self.model_fields_set:
            _dict['last_rate_limited_timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiInsightsRouteStatsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "http_method": obj.get("http_method"),
            "api_route": obj.get("api_route"),
            "total_request_count": obj.get("total_request_count"),
            "rate_limited_request_count": obj.get("rate_limited_request_count"),
            "last_rate_limited_timestamp": obj.get("last_rate_limited_timestamp"),
            "last_request_timestamp": obj.get("last_request_timestamp")
        })
        return _obj


