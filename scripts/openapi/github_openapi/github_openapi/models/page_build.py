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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from github_openapi.models.page_build_error import PageBuildError
from typing import Optional, Set
from typing_extensions import Self

class PageBuild(BaseModel):
    """
    Page Build
    """ # noqa: E501
    url: StrictStr
    status: StrictStr
    error: PageBuildError
    pusher: Optional[NullableSimpleUser]
    commit: StrictStr
    duration: StrictInt
    created_at: datetime
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["url", "status", "error", "pusher", "commit", "duration", "created_at", "updated_at"]

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
        """Create an instance of PageBuild from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pusher
        if self.pusher:
            _dict['pusher'] = self.pusher.to_dict()
        # set to None if pusher (nullable) is None
        # and model_fields_set contains the field
        if self.pusher is None and "pusher" in self.model_fields_set:
            _dict['pusher'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PageBuild from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "status": obj.get("status"),
            "error": PageBuildError.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "pusher": NullableSimpleUser.from_dict(obj["pusher"]) if obj.get("pusher") is not None else None,
            "commit": obj.get("commit"),
            "duration": obj.get("duration"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


