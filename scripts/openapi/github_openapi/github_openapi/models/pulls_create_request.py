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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PullsCreateRequest(BaseModel):
    """
    PullsCreateRequest
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The title of the new pull request. Required unless `issue` is specified.")
    head: StrictStr = Field(description="The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace `head` with a user like this: `username:branch`.")
    head_repo: Optional[StrictStr] = Field(default=None, description="The name of the repository where the changes in the pull request were made. This field is required for cross-repository pull requests if both repositories are owned by the same organization.")
    base: StrictStr = Field(description="The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.")
    body: Optional[StrictStr] = Field(default=None, description="The contents of the pull request.")
    maintainer_can_modify: Optional[StrictBool] = Field(default=None, description="Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request.")
    draft: Optional[StrictBool] = Field(default=None, description="Indicates whether the pull request is a draft. See \"[Draft Pull Requests](https://docs.github.com/articles/about-pull-requests#draft-pull-requests)\" in the GitHub Help documentation to learn more.")
    issue: Optional[StrictInt] = Field(default=None, description="An issue in the repository to convert to a pull request. The issue title, body, and comments will become the title, body, and comments on the new pull request. Required unless `title` is specified.")
    __properties: ClassVar[List[str]] = ["title", "head", "head_repo", "base", "body", "maintainer_can_modify", "draft", "issue"]

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
        """Create an instance of PullsCreateRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PullsCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "head": obj.get("head"),
            "head_repo": obj.get("head_repo"),
            "base": obj.get("base"),
            "body": obj.get("body"),
            "maintainer_can_modify": obj.get("maintainer_can_modify"),
            "draft": obj.get("draft"),
            "issue": obj.get("issue")
        })
        return _obj

