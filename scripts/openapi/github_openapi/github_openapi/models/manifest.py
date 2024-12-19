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
from github_openapi.models.dependency import Dependency
from github_openapi.models.manifest_file import ManifestFile
from github_openapi.models.metadata_value import MetadataValue
from typing import Optional, Set
from typing_extensions import Self

class Manifest(BaseModel):
    """
    Manifest
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the manifest.")
    file: Optional[ManifestFile] = None
    metadata: Optional[Dict[str, Optional[MetadataValue]]] = Field(default=None, description="User-defined metadata to store domain-specific information limited to 8 keys with scalar values.")
    resolved: Optional[Dict[str, Dependency]] = Field(default=None, description="A collection of resolved package dependencies.")
    __properties: ClassVar[List[str]] = ["name", "file", "metadata", "resolved"]

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
        """Create an instance of Manifest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in metadata (dict)
        _field_dict = {}
        if self.metadata:
            for _key_metadata in self.metadata:
                if self.metadata[_key_metadata]:
                    _field_dict[_key_metadata] = self.metadata[_key_metadata].to_dict()
            _dict['metadata'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in resolved (dict)
        _field_dict = {}
        if self.resolved:
            for _key_resolved in self.resolved:
                if self.resolved[_key_resolved]:
                    _field_dict[_key_resolved] = self.resolved[_key_resolved].to_dict()
            _dict['resolved'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Manifest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "file": ManifestFile.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "metadata": dict(
                (_k, MetadataValue.from_dict(_v))
                for _k, _v in obj["metadata"].items()
            )
            if obj.get("metadata") is not None
            else None,
            "resolved": dict(
                (_k, Dependency.from_dict(_v))
                for _k, _v in obj["resolved"].items()
            )
            if obj.get("resolved") is not None
            else None
        })
        return _obj

