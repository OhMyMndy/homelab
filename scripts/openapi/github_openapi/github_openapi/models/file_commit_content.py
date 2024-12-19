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
from github_openapi.models.file_commit_content_links import FileCommitContentLinks
from typing import Optional, Set
from typing_extensions import Self

class FileCommitContent(BaseModel):
    """
    FileCommitContent
    """ # noqa: E501
    name: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    git_url: Optional[StrictStr] = None
    download_url: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    links: Optional[FileCommitContentLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["name", "path", "sha", "size", "url", "html_url", "git_url", "download_url", "type", "_links"]

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
        """Create an instance of FileCommitContent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileCommitContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "path": obj.get("path"),
            "sha": obj.get("sha"),
            "size": obj.get("size"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "git_url": obj.get("git_url"),
            "download_url": obj.get("download_url"),
            "type": obj.get("type"),
            "_links": FileCommitContentLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj

