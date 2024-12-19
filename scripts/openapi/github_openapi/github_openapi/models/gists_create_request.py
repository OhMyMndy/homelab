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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.gists_create_request_files_value import GistsCreateRequestFilesValue
from github_openapi.models.gists_create_request_public import GistsCreateRequestPublic
from typing import Optional, Set
from typing_extensions import Self

class GistsCreateRequest(BaseModel):
    """
    GistsCreateRequest
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the gist")
    files: Dict[str, GistsCreateRequestFilesValue] = Field(description="Names and content for the files that make up the gist")
    public: Optional[GistsCreateRequestPublic] = None
    __properties: ClassVar[List[str]] = ["description", "files", "public"]

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
        """Create an instance of GistsCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in files (dict)
        _field_dict = {}
        if self.files:
            for _key_files in self.files:
                if self.files[_key_files]:
                    _field_dict[_key_files] = self.files[_key_files].to_dict()
            _dict['files'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of public
        if self.public:
            _dict['public'] = self.public.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GistsCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "files": dict(
                (_k, GistsCreateRequestFilesValue.from_dict(_v))
                for _k, _v in obj["files"].items()
            )
            if obj.get("files") is not None
            else None,
            "public": GistsCreateRequestPublic.from_dict(obj["public"]) if obj.get("public") is not None else None
        })
        return _obj


