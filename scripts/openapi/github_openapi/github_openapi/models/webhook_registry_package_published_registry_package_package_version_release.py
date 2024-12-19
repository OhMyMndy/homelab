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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.webhooks_sponsorship_maintainer import WebhooksSponsorshipMaintainer
from typing import Optional, Set
from typing_extensions import Self

class WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease(BaseModel):
    """
    WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease
    """ # noqa: E501
    author: Optional[WebhooksSponsorshipMaintainer] = None
    created_at: Optional[StrictStr] = None
    draft: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    prerelease: Optional[StrictBool] = None
    published_at: Optional[StrictStr] = None
    tag_name: Optional[StrictStr] = None
    target_commitish: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["author", "created_at", "draft", "html_url", "id", "name", "prerelease", "published_at", "tag_name", "target_commitish", "url"]

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
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author": WebhooksSponsorshipMaintainer.from_dict(obj["author"]) if obj.get("author") is not None else None,
            "created_at": obj.get("created_at"),
            "draft": obj.get("draft"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "prerelease": obj.get("prerelease"),
            "published_at": obj.get("published_at"),
            "tag_name": obj.get("tag_name"),
            "target_commitish": obj.get("target_commitish"),
            "url": obj.get("url")
        })
        return _obj


