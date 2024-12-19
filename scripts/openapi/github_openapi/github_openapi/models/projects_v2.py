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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from github_openapi.models.simple_user import SimpleUser
from typing import Optional, Set
from typing_extensions import Self

class ProjectsV2(BaseModel):
    """
    A projects v2 project
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    node_id: StrictStr
    owner: SimpleUser
    creator: SimpleUser
    title: StrictStr
    description: Optional[StrictStr]
    public: StrictBool
    closed_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    number: StrictInt
    short_description: Optional[StrictStr]
    deleted_at: Optional[datetime]
    deleted_by: Optional[NullableSimpleUser]
    __properties: ClassVar[List[str]] = ["id", "node_id", "owner", "creator", "title", "description", "public", "closed_at", "created_at", "updated_at", "number", "short_description", "deleted_at", "deleted_by"]

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
        """Create an instance of ProjectsV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted_by
        if self.deleted_by:
            _dict['deleted_by'] = self.deleted_by.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if closed_at (nullable) is None
        # and model_fields_set contains the field
        if self.closed_at is None and "closed_at" in self.model_fields_set:
            _dict['closed_at'] = None

        # set to None if short_description (nullable) is None
        # and model_fields_set contains the field
        if self.short_description is None and "short_description" in self.model_fields_set:
            _dict['short_description'] = None

        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if deleted_by (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_by is None and "deleted_by" in self.model_fields_set:
            _dict['deleted_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectsV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "owner": SimpleUser.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "creator": SimpleUser.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "public": obj.get("public"),
            "closed_at": obj.get("closed_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "number": obj.get("number"),
            "short_description": obj.get("short_description"),
            "deleted_at": obj.get("deleted_at"),
            "deleted_by": NullableSimpleUser.from_dict(obj["deleted_by"]) if obj.get("deleted_by") is not None else None
        })
        return _obj


