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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from github_openapi.models.code_scanning_variant_analysis_repository import CodeScanningVariantAnalysisRepository
from typing import Optional, Set
from typing_extensions import Self

class CodeScanningVariantAnalysisSkippedRepoGroup(BaseModel):
    """
    CodeScanningVariantAnalysisSkippedRepoGroup
    """ # noqa: E501
    repository_count: StrictInt = Field(description="The total number of repositories that were skipped for this reason.")
    repositories: List[CodeScanningVariantAnalysisRepository] = Field(description="A list of repositories that were skipped. This list may not include all repositories that were skipped. This is only available when the repository was found and the user has access to it.")
    __properties: ClassVar[List[str]] = ["repository_count", "repositories"]

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
        """Create an instance of CodeScanningVariantAnalysisSkippedRepoGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in repositories (list)
        _items = []
        if self.repositories:
            for _item_repositories in self.repositories:
                if _item_repositories:
                    _items.append(_item_repositories.to_dict())
            _dict['repositories'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeScanningVariantAnalysisSkippedRepoGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "repository_count": obj.get("repository_count"),
            "repositories": [CodeScanningVariantAnalysisRepository.from_dict(_item) for _item in obj["repositories"]] if obj.get("repositories") is not None else None
        })
        return _obj


