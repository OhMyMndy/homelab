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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.artifact_workflow_run import ArtifactWorkflowRun
from typing import Optional, Set
from typing_extensions import Self

class Artifact(BaseModel):
    """
    An artifact
    """ # noqa: E501
    id: StrictInt
    node_id: StrictStr
    name: StrictStr = Field(description="The name of the artifact.")
    size_in_bytes: StrictInt = Field(description="The size in bytes of the artifact.")
    url: StrictStr
    archive_download_url: StrictStr
    expired: StrictBool = Field(description="Whether or not the artifact has expired.")
    created_at: Optional[datetime]
    expires_at: Optional[datetime]
    updated_at: Optional[datetime]
    workflow_run: Optional[ArtifactWorkflowRun] = None
    __properties: ClassVar[List[str]] = ["id", "node_id", "name", "size_in_bytes", "url", "archive_download_url", "expired", "created_at", "expires_at", "updated_at", "workflow_run"]

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
        """Create an instance of Artifact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workflow_run
        if self.workflow_run:
            _dict['workflow_run'] = self.workflow_run.to_dict()
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if workflow_run (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_run is None and "workflow_run" in self.model_fields_set:
            _dict['workflow_run'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Artifact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "size_in_bytes": obj.get("size_in_bytes"),
            "url": obj.get("url"),
            "archive_download_url": obj.get("archive_download_url"),
            "expired": obj.get("expired"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at"),
            "updated_at": obj.get("updated_at"),
            "workflow_run": ArtifactWorkflowRun.from_dict(obj["workflow_run"]) if obj.get("workflow_run") is not None else None
        })
        return _obj

