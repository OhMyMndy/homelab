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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.webhook_member_edited_changes_permission import WebhookMemberEditedChangesPermission
from github_openapi.models.webhook_projects_v2_project_edited_changes_public import WebhookProjectsV2ProjectEditedChangesPublic
from github_openapi.models.webhook_projects_v2_project_edited_changes_title import WebhookProjectsV2ProjectEditedChangesTitle
from typing import Optional, Set
from typing_extensions import Self

class WebhookProjectsV2ProjectEditedChanges(BaseModel):
    """
    WebhookProjectsV2ProjectEditedChanges
    """ # noqa: E501
    description: Optional[WebhookMemberEditedChangesPermission] = None
    public: Optional[WebhookProjectsV2ProjectEditedChangesPublic] = None
    short_description: Optional[WebhookMemberEditedChangesPermission] = None
    title: Optional[WebhookProjectsV2ProjectEditedChangesTitle] = None
    __properties: ClassVar[List[str]] = ["description", "public", "short_description", "title"]

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
        """Create an instance of WebhookProjectsV2ProjectEditedChanges from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public
        if self.public:
            _dict['public'] = self.public.to_dict()
        # override the default output from pydantic by calling `to_dict()` of short_description
        if self.short_description:
            _dict['short_description'] = self.short_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of title
        if self.title:
            _dict['title'] = self.title.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookProjectsV2ProjectEditedChanges from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": WebhookMemberEditedChangesPermission.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "public": WebhookProjectsV2ProjectEditedChangesPublic.from_dict(obj["public"]) if obj.get("public") is not None else None,
            "short_description": WebhookMemberEditedChangesPermission.from_dict(obj["short_description"]) if obj.get("short_description") is not None else None,
            "title": WebhookProjectsV2ProjectEditedChangesTitle.from_dict(obj["title"]) if obj.get("title") is not None else None
        })
        return _obj


