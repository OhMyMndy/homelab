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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CodeScanningUploadSarifRequest(BaseModel):
    """
    CodeScanningUploadSarifRequest
    """ # noqa: E501
    commit_sha: Annotated[str, Field(min_length=40, strict=True, max_length=40)] = Field(description="The SHA of the commit to which the analysis you are uploading relates.")
    ref: Annotated[str, Field(strict=True)] = Field(description="The full Git reference, formatted as `refs/heads/<branch name>`, `refs/tags/<tag>`, `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.")
    sarif: StrictStr = Field(description="A Base64 string representing the SARIF file to upload. You must first compress your SARIF file using [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate the contents of the file into a Base64 encoding string. For more information, see \"[SARIF support for code scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning).\"")
    checkout_uri: Optional[StrictStr] = Field(default=None, description="The base directory used in the analysis, as it appears in the SARIF file. This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository.")
    started_at: Optional[datetime] = Field(default=None, description="The time that the analysis run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.")
    tool_name: Optional[StrictStr] = Field(default=None, description="The name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to \"API\". If the uploaded SARIF contains a tool GUID, this will be available for filtering using the `tool_guid` parameter of operations such as `GET /repos/{owner}/{repo}/code-scanning/alerts`.")
    validate: Optional[StrictBool] = Field(default=None, description="Whether the SARIF file will be validated according to the code scanning specifications. This parameter is intended to help integrators ensure that the uploaded SARIF files are correctly rendered by code scanning.")
    __properties: ClassVar[List[str]] = ["commit_sha", "ref", "sarif", "checkout_uri", "started_at", "tool_name", "validate"]

    @field_validator('commit_sha')
    def commit_sha_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9a-fA-F]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]+$/")
        return value

    @field_validator('ref')
    def ref_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^refs\/(heads|tags|pull)\/.*$", value):
            raise ValueError(r"must validate the regular expression /^refs\/(heads|tags|pull)\/.*$/")
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
        """Create an instance of CodeScanningUploadSarifRequest from a JSON string"""
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
        """Create an instance of CodeScanningUploadSarifRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commit_sha": obj.get("commit_sha"),
            "ref": obj.get("ref"),
            "sarif": obj.get("sarif"),
            "checkout_uri": obj.get("checkout_uri"),
            "started_at": obj.get("started_at"),
            "tool_name": obj.get("tool_name"),
            "validate": obj.get("validate")
        })
        return _obj


