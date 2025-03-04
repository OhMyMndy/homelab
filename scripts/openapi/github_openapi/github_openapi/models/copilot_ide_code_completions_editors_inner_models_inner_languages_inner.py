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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner(BaseModel):
    """
    Usage metrics for a given language for the given editor for Copilot code completions.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the language used for Copilot code completion suggestions, for the given editor.")
    total_engaged_users: Optional[StrictInt] = Field(default=None, description="Number of users who accepted at least one Copilot code completion suggestion for the given editor, for the given language. Includes both full and partial acceptances.")
    total_code_suggestions: Optional[StrictInt] = Field(default=None, description="The number of Copilot code suggestions generated for the given editor, for the given language.")
    total_code_acceptances: Optional[StrictInt] = Field(default=None, description="The number of Copilot code suggestions accepted for the given editor, for the given language. Includes both full and partial acceptances.")
    total_code_lines_suggested: Optional[StrictInt] = Field(default=None, description="The number of lines of code suggested by Copilot code completions for the given editor, for the given language.")
    total_code_lines_accepted: Optional[StrictInt] = Field(default=None, description="The number of lines of code accepted from Copilot code suggestions for the given editor, for the given language.")
    __properties: ClassVar[List[str]] = ["name", "total_engaged_users", "total_code_suggestions", "total_code_acceptances", "total_code_lines_suggested", "total_code_lines_accepted"]

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
        """Create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner from a JSON string"""
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
        """Create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "total_engaged_users": obj.get("total_engaged_users"),
            "total_code_suggestions": obj.get("total_code_suggestions"),
            "total_code_acceptances": obj.get("total_code_acceptances"),
            "total_code_lines_suggested": obj.get("total_code_lines_suggested"),
            "total_code_lines_accepted": obj.get("total_code_lines_accepted")
        })
        return _obj


