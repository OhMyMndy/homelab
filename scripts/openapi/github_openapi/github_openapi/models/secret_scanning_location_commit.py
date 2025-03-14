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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class SecretScanningLocationCommit(BaseModel):
    """
    Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository.
    """ # noqa: E501
    path: StrictStr = Field(description="The file path in the repository")
    start_line: Union[StrictFloat, StrictInt] = Field(description="Line number at which the secret starts in the file")
    end_line: Union[StrictFloat, StrictInt] = Field(description="Line number at which the secret ends in the file")
    start_column: Union[StrictFloat, StrictInt] = Field(description="The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII")
    end_column: Union[StrictFloat, StrictInt] = Field(description="The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII")
    blob_sha: StrictStr = Field(description="SHA-1 hash ID of the associated blob")
    blob_url: StrictStr = Field(description="The API URL to get the associated blob resource")
    commit_sha: StrictStr = Field(description="SHA-1 hash ID of the associated commit")
    commit_url: StrictStr = Field(description="The API URL to get the associated commit resource")
    __properties: ClassVar[List[str]] = ["path", "start_line", "end_line", "start_column", "end_column", "blob_sha", "blob_url", "commit_sha", "commit_url"]

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
        """Create an instance of SecretScanningLocationCommit from a JSON string"""
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
        """Create an instance of SecretScanningLocationCommit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "start_line": obj.get("start_line"),
            "end_line": obj.get("end_line"),
            "start_column": obj.get("start_column"),
            "end_column": obj.get("end_column"),
            "blob_sha": obj.get("blob_sha"),
            "blob_url": obj.get("blob_url"),
            "commit_sha": obj.get("commit_sha"),
            "commit_url": obj.get("commit_url")
        })
        return _obj


