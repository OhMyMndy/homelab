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
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from github_openapi.models.projects_v2_item_content_type import ProjectsV2ItemContentType
from github_openapi.models.simple_user import SimpleUser
from typing import Optional, Set
from typing_extensions import Self

class ProjectsV2Item(BaseModel):
    """
    An item belonging to a project
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    node_id: Optional[StrictStr] = None
    project_node_id: Optional[StrictStr] = None
    content_node_id: StrictStr
    content_type: ProjectsV2ItemContentType
    creator: Optional[SimpleUser] = None
    created_at: datetime
    updated_at: datetime
    archived_at: Optional[datetime]
    __properties: ClassVar[List[str]] = ["id", "node_id", "project_node_id", "content_node_id", "content_type", "creator", "created_at", "updated_at", "archived_at"]

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
        """Create an instance of ProjectsV2Item from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # set to None if archived_at (nullable) is None
        # and model_fields_set contains the field
        if self.archived_at is None and "archived_at" in self.model_fields_set:
            _dict['archived_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectsV2Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "project_node_id": obj.get("project_node_id"),
            "content_node_id": obj.get("content_node_id"),
            "content_type": obj.get("content_type"),
            "creator": SimpleUser.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "archived_at": obj.get("archived_at")
        })
        return _obj

