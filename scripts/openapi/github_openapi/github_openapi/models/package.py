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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_minimal_repository import NullableMinimalRepository
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from typing import Optional, Set
from typing_extensions import Self

class Package(BaseModel):
    """
    A software package
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier of the package.")
    name: StrictStr = Field(description="The name of the package.")
    package_type: StrictStr
    url: StrictStr
    html_url: StrictStr
    version_count: StrictInt = Field(description="The number of versions of the package.")
    visibility: StrictStr
    owner: Optional[NullableSimpleUser] = None
    repository: Optional[NullableMinimalRepository] = None
    created_at: datetime
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["id", "name", "package_type", "url", "html_url", "version_count", "visibility", "owner", "repository", "created_at", "updated_at"]

    @field_validator('package_type')
    def package_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['npm', 'maven', 'rubygems', 'docker', 'nuget', 'container']):
            raise ValueError("must be one of enum values ('npm', 'maven', 'rubygems', 'docker', 'nuget', 'container')")
        return value

    @field_validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['private', 'public']):
            raise ValueError("must be one of enum values ('private', 'public')")
        return value

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
        """Create an instance of Package from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if repository (nullable) is None
        # and model_fields_set contains the field
        if self.repository is None and "repository" in self.model_fields_set:
            _dict['repository'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Package from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "package_type": obj.get("package_type"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "version_count": obj.get("version_count"),
            "visibility": obj.get("visibility"),
            "owner": NullableSimpleUser.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "repository": NullableMinimalRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

