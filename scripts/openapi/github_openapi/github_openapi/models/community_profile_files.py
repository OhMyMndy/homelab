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
from github_openapi.models.nullable_code_of_conduct_simple import NullableCodeOfConductSimple
from github_openapi.models.nullable_community_health_file import NullableCommunityHealthFile
from github_openapi.models.nullable_license_simple import NullableLicenseSimple
from typing import Optional, Set
from typing_extensions import Self

class CommunityProfileFiles(BaseModel):
    """
    CommunityProfileFiles
    """ # noqa: E501
    code_of_conduct: Optional[NullableCodeOfConductSimple]
    code_of_conduct_file: Optional[NullableCommunityHealthFile]
    license: Optional[NullableLicenseSimple]
    contributing: Optional[NullableCommunityHealthFile]
    readme: Optional[NullableCommunityHealthFile]
    issue_template: Optional[NullableCommunityHealthFile]
    pull_request_template: Optional[NullableCommunityHealthFile]
    __properties: ClassVar[List[str]] = ["code_of_conduct", "code_of_conduct_file", "license", "contributing", "readme", "issue_template", "pull_request_template"]

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
        """Create an instance of CommunityProfileFiles from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code_of_conduct
        if self.code_of_conduct:
            _dict['code_of_conduct'] = self.code_of_conduct.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_of_conduct_file
        if self.code_of_conduct_file:
            _dict['code_of_conduct_file'] = self.code_of_conduct_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of license
        if self.license:
            _dict['license'] = self.license.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contributing
        if self.contributing:
            _dict['contributing'] = self.contributing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of readme
        if self.readme:
            _dict['readme'] = self.readme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issue_template
        if self.issue_template:
            _dict['issue_template'] = self.issue_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pull_request_template
        if self.pull_request_template:
            _dict['pull_request_template'] = self.pull_request_template.to_dict()
        # set to None if code_of_conduct (nullable) is None
        # and model_fields_set contains the field
        if self.code_of_conduct is None and "code_of_conduct" in self.model_fields_set:
            _dict['code_of_conduct'] = None

        # set to None if code_of_conduct_file (nullable) is None
        # and model_fields_set contains the field
        if self.code_of_conduct_file is None and "code_of_conduct_file" in self.model_fields_set:
            _dict['code_of_conduct_file'] = None

        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if contributing (nullable) is None
        # and model_fields_set contains the field
        if self.contributing is None and "contributing" in self.model_fields_set:
            _dict['contributing'] = None

        # set to None if readme (nullable) is None
        # and model_fields_set contains the field
        if self.readme is None and "readme" in self.model_fields_set:
            _dict['readme'] = None

        # set to None if issue_template (nullable) is None
        # and model_fields_set contains the field
        if self.issue_template is None and "issue_template" in self.model_fields_set:
            _dict['issue_template'] = None

        # set to None if pull_request_template (nullable) is None
        # and model_fields_set contains the field
        if self.pull_request_template is None and "pull_request_template" in self.model_fields_set:
            _dict['pull_request_template'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommunityProfileFiles from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code_of_conduct": NullableCodeOfConductSimple.from_dict(obj["code_of_conduct"]) if obj.get("code_of_conduct") is not None else None,
            "code_of_conduct_file": NullableCommunityHealthFile.from_dict(obj["code_of_conduct_file"]) if obj.get("code_of_conduct_file") is not None else None,
            "license": NullableLicenseSimple.from_dict(obj["license"]) if obj.get("license") is not None else None,
            "contributing": NullableCommunityHealthFile.from_dict(obj["contributing"]) if obj.get("contributing") is not None else None,
            "readme": NullableCommunityHealthFile.from_dict(obj["readme"]) if obj.get("readme") is not None else None,
            "issue_template": NullableCommunityHealthFile.from_dict(obj["issue_template"]) if obj.get("issue_template") is not None else None,
            "pull_request_template": NullableCommunityHealthFile.from_dict(obj["pull_request_template"]) if obj.get("pull_request_template") is not None else None
        })
        return _obj


