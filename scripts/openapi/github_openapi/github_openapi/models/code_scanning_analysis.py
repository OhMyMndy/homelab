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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from github_openapi.models.code_scanning_analysis_tool import CodeScanningAnalysisTool
from typing import Optional, Set
from typing_extensions import Self

class CodeScanningAnalysis(BaseModel):
    """
    CodeScanningAnalysis
    """ # noqa: E501
    ref: StrictStr = Field(description="The Git reference, formatted as `refs/pull/<number>/merge`, `refs/pull/<number>/head`, `refs/heads/<branch name>` or simply `<branch name>`.")
    commit_sha: Annotated[str, Field(min_length=40, strict=True, max_length=40)] = Field(description="The SHA of the commit to which the analysis you are uploading relates.")
    analysis_key: StrictStr = Field(description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name.")
    environment: StrictStr = Field(description="Identifies the variable values associated with the environment in which this analysis was performed.")
    category: Optional[StrictStr] = Field(default=None, description="Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code.")
    error: StrictStr
    created_at: datetime = Field(description="The time that the analysis was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.")
    results_count: StrictInt = Field(description="The total number of results in the analysis.")
    rules_count: StrictInt = Field(description="The total number of rules used in the analysis.")
    id: StrictInt = Field(description="Unique identifier for this analysis.")
    url: StrictStr = Field(description="The REST API URL of the analysis resource.")
    sarif_id: StrictStr = Field(description="An identifier for the upload.")
    tool: CodeScanningAnalysisTool
    deletable: StrictBool
    warning: StrictStr = Field(description="Warning generated when processing the analysis")
    __properties: ClassVar[List[str]] = ["ref", "commit_sha", "analysis_key", "environment", "category", "error", "created_at", "results_count", "rules_count", "id", "url", "sarif_id", "tool", "deletable", "warning"]

    @field_validator('commit_sha')
    def commit_sha_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9a-fA-F]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]+$/")
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
        """Create an instance of CodeScanningAnalysis from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tool
        if self.tool:
            _dict['tool'] = self.tool.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeScanningAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ref": obj.get("ref"),
            "commit_sha": obj.get("commit_sha"),
            "analysis_key": obj.get("analysis_key"),
            "environment": obj.get("environment"),
            "category": obj.get("category"),
            "error": obj.get("error"),
            "created_at": obj.get("created_at"),
            "results_count": obj.get("results_count"),
            "rules_count": obj.get("rules_count"),
            "id": obj.get("id"),
            "url": obj.get("url"),
            "sarif_id": obj.get("sarif_id"),
            "tool": CodeScanningAnalysisTool.from_dict(obj["tool"]) if obj.get("tool") is not None else None,
            "deletable": obj.get("deletable"),
            "warning": obj.get("warning")
        })
        return _obj

