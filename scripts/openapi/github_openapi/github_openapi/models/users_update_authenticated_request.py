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
from typing import Optional, Set
from typing_extensions import Self

class UsersUpdateAuthenticatedRequest(BaseModel):
    """
    UsersUpdateAuthenticatedRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The new name of the user.")
    email: Optional[StrictStr] = Field(default=None, description="The publicly visible email address of the user.")
    blog: Optional[StrictStr] = Field(default=None, description="The new blog URL of the user.")
    twitter_username: Optional[StrictStr] = Field(default=None, description="The new Twitter username of the user.")
    company: Optional[StrictStr] = Field(default=None, description="The new company of the user.")
    location: Optional[StrictStr] = Field(default=None, description="The new location of the user.")
    hireable: Optional[StrictBool] = Field(default=None, description="The new hiring availability of the user.")
    bio: Optional[StrictStr] = Field(default=None, description="The new short biography of the user.")
    __properties: ClassVar[List[str]] = ["name", "email", "blog", "twitter_username", "company", "location", "hireable", "bio"]

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
        """Create an instance of UsersUpdateAuthenticatedRequest from a JSON string"""
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
        # set to None if twitter_username (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_username is None and "twitter_username" in self.model_fields_set:
            _dict['twitter_username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsersUpdateAuthenticatedRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "blog": obj.get("blog"),
            "twitter_username": obj.get("twitter_username"),
            "company": obj.get("company"),
            "location": obj.get("location"),
            "hireable": obj.get("hireable"),
            "bio": obj.get("bio")
        })
        return _obj


