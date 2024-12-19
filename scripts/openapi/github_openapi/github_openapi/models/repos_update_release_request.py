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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReposUpdateReleaseRequest(BaseModel):
    """
    ReposUpdateReleaseRequest
    """ # noqa: E501
    tag_name: Optional[StrictStr] = Field(default=None, description="The name of the tag.")
    target_commitish: Optional[StrictStr] = Field(default=None, description="Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository's default branch.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the release.")
    body: Optional[StrictStr] = Field(default=None, description="Text describing the contents of the tag.")
    draft: Optional[StrictBool] = Field(default=None, description="`true` makes the release a draft, and `false` publishes the release.")
    prerelease: Optional[StrictBool] = Field(default=None, description="`true` to identify the release as a prerelease, `false` to identify the release as a full release.")
    make_latest: Optional[StrictStr] = Field(default='true', description="Specifies whether this release should be set as the latest release for the repository. Drafts and prereleases cannot be set as latest. Defaults to `true` for newly published releases. `legacy` specifies that the latest release should be determined based on the release creation date and higher semantic version.")
    discussion_category_name: Optional[StrictStr] = Field(default=None, description="If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository. If there is already a discussion linked to the release, this parameter is ignored. For more information, see \"[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository).\"")
    __properties: ClassVar[List[str]] = ["tag_name", "target_commitish", "name", "body", "draft", "prerelease", "make_latest", "discussion_category_name"]

    @field_validator('make_latest')
    def make_latest_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['true', 'false', 'legacy']):
            raise ValueError("must be one of enum values ('true', 'false', 'legacy')")
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
        """Create an instance of ReposUpdateReleaseRequest from a JSON string"""
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
        """Create an instance of ReposUpdateReleaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tag_name": obj.get("tag_name"),
            "target_commitish": obj.get("target_commitish"),
            "name": obj.get("name"),
            "body": obj.get("body"),
            "draft": obj.get("draft"),
            "prerelease": obj.get("prerelease"),
            "make_latest": obj.get("make_latest") if obj.get("make_latest") is not None else 'true',
            "discussion_category_name": obj.get("discussion_category_name")
        })
        return _obj


