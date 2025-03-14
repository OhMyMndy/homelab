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
from github_openapi.models.nullable_integration import NullableIntegration
from typing import Optional, Set
from typing_extensions import Self

class DeploymentSimple(BaseModel):
    """
    A deployment created as the result of an Actions check run from a workflow that references an environment
    """ # noqa: E501
    url: StrictStr
    id: StrictInt = Field(description="Unique identifier of the deployment")
    node_id: StrictStr
    task: StrictStr = Field(description="Parameter to specify a task to execute")
    original_environment: Optional[StrictStr] = None
    environment: StrictStr = Field(description="Name for the target deployment environment.")
    description: Optional[StrictStr]
    created_at: datetime
    updated_at: datetime
    statuses_url: StrictStr
    repository_url: StrictStr
    transient_environment: Optional[StrictBool] = Field(default=None, description="Specifies if the given environment is will no longer exist at some point in the future. Default: false.")
    production_environment: Optional[StrictBool] = Field(default=None, description="Specifies if the given environment is one that end-users directly interact with. Default: false.")
    performed_via_github_app: Optional[NullableIntegration] = None
    __properties: ClassVar[List[str]] = ["url", "id", "node_id", "task", "original_environment", "environment", "description", "created_at", "updated_at", "statuses_url", "repository_url", "transient_environment", "production_environment", "performed_via_github_app"]

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
        """Create an instance of DeploymentSimple from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of performed_via_github_app
        if self.performed_via_github_app:
            _dict['performed_via_github_app'] = self.performed_via_github_app.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if performed_via_github_app (nullable) is None
        # and model_fields_set contains the field
        if self.performed_via_github_app is None and "performed_via_github_app" in self.model_fields_set:
            _dict['performed_via_github_app'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentSimple from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "task": obj.get("task"),
            "original_environment": obj.get("original_environment"),
            "environment": obj.get("environment"),
            "description": obj.get("description"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "statuses_url": obj.get("statuses_url"),
            "repository_url": obj.get("repository_url"),
            "transient_environment": obj.get("transient_environment"),
            "production_environment": obj.get("production_environment"),
            "performed_via_github_app": NullableIntegration.from_dict(obj["performed_via_github_app"]) if obj.get("performed_via_github_app") is not None else None
        })
        return _obj


