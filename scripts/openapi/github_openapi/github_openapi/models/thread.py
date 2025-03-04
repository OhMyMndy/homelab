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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.models.thread_subject import ThreadSubject
from typing import Optional, Set
from typing_extensions import Self

class Thread(BaseModel):
    """
    Thread
    """ # noqa: E501
    id: StrictStr
    repository: MinimalRepository
    subject: ThreadSubject
    reason: StrictStr
    unread: StrictBool
    updated_at: StrictStr
    last_read_at: Optional[StrictStr]
    url: StrictStr
    subscription_url: StrictStr
    __properties: ClassVar[List[str]] = ["id", "repository", "subject", "reason", "unread", "updated_at", "last_read_at", "url", "subscription_url"]

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
        """Create an instance of Thread from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        # set to None if last_read_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_read_at is None and "last_read_at" in self.model_fields_set:
            _dict['last_read_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Thread from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "repository": MinimalRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "subject": ThreadSubject.from_dict(obj["subject"]) if obj.get("subject") is not None else None,
            "reason": obj.get("reason"),
            "unread": obj.get("unread"),
            "updated_at": obj.get("updated_at"),
            "last_read_at": obj.get("last_read_at"),
            "url": obj.get("url"),
            "subscription_url": obj.get("subscription_url")
        })
        return _obj


