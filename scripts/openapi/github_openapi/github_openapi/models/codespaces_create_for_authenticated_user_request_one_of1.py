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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.codespaces_create_for_authenticated_user_request_one_of1_pull_request import CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest
from typing import Optional, Set
from typing_extensions import Self

class CodespacesCreateForAuthenticatedUserRequestOneOf1(BaseModel):
    """
    CodespacesCreateForAuthenticatedUserRequestOneOf1
    """ # noqa: E501
    pull_request: CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest
    location: Optional[StrictStr] = Field(default=None, description="The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.")
    geo: Optional[StrictStr] = Field(default=None, description="The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaces `location`, which is closing down.")
    machine: Optional[StrictStr] = Field(default=None, description="Machine type to use for this codespace")
    devcontainer_path: Optional[StrictStr] = Field(default=None, description="Path to devcontainer.json config to use for this codespace")
    working_directory: Optional[StrictStr] = Field(default=None, description="Working directory for this codespace")
    idle_timeout_minutes: Optional[StrictInt] = Field(default=None, description="Time in minutes before codespace stops from inactivity")
    __properties: ClassVar[List[str]] = ["pull_request", "location", "geo", "machine", "devcontainer_path", "working_directory", "idle_timeout_minutes"]

    @field_validator('geo')
    def geo_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EuropeWest', 'SoutheastAsia', 'UsEast', 'UsWest']):
            raise ValueError("must be one of enum values ('EuropeWest', 'SoutheastAsia', 'UsEast', 'UsWest')")
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
        """Create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pull_request
        if self.pull_request:
            _dict['pull_request'] = self.pull_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pull_request": CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.from_dict(obj["pull_request"]) if obj.get("pull_request") is not None else None,
            "location": obj.get("location"),
            "geo": obj.get("geo"),
            "machine": obj.get("machine"),
            "devcontainer_path": obj.get("devcontainer_path"),
            "working_directory": obj.get("working_directory"),
            "idle_timeout_minutes": obj.get("idle_timeout_minutes")
        })
        return _obj


