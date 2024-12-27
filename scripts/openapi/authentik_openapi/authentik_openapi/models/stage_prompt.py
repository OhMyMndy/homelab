# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from authentik_openapi.models.prompt_type_enum import PromptTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class StagePrompt(BaseModel):
    """
    Serializer for a single Prompt field
    """ # noqa: E501
    field_key: StrictStr
    label: StrictStr
    type: PromptTypeEnum
    required: StrictBool
    placeholder: StrictStr
    initial_value: StrictStr
    order: StrictInt
    sub_text: StrictStr
    choices: Optional[List[StrictStr]]
    __properties: ClassVar[List[str]] = ["field_key", "label", "type", "required", "placeholder", "initial_value", "order", "sub_text", "choices"]

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
        """Create an instance of StagePrompt from a JSON string"""
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
        # set to None if choices (nullable) is None
        # and model_fields_set contains the field
        if self.choices is None and "choices" in self.model_fields_set:
            _dict['choices'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StagePrompt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field_key": obj.get("field_key"),
            "label": obj.get("label"),
            "type": obj.get("type"),
            "required": obj.get("required"),
            "placeholder": obj.get("placeholder"),
            "initial_value": obj.get("initial_value"),
            "order": obj.get("order"),
            "sub_text": obj.get("sub_text"),
            "choices": obj.get("choices")
        })
        return _obj

