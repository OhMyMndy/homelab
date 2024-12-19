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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from github_openapi.models.search_result_text_matches_inner import SearchResultTextMatchesInner
from typing import Optional, Set
from typing_extensions import Self

class LabelSearchResultItem(BaseModel):
    """
    Label Search Result Item
    """ # noqa: E501
    id: StrictInt
    node_id: StrictStr
    url: StrictStr
    name: StrictStr
    color: StrictStr
    default: StrictBool
    description: Optional[StrictStr]
    score: Union[StrictFloat, StrictInt]
    text_matches: Optional[List[SearchResultTextMatchesInner]] = None
    __properties: ClassVar[List[str]] = ["id", "node_id", "url", "name", "color", "default", "description", "score", "text_matches"]

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
        """Create an instance of LabelSearchResultItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in text_matches (list)
        _items = []
        if self.text_matches:
            for _item_text_matches in self.text_matches:
                if _item_text_matches:
                    _items.append(_item_text_matches.to_dict())
            _dict['text_matches'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LabelSearchResultItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "url": obj.get("url"),
            "name": obj.get("name"),
            "color": obj.get("color"),
            "default": obj.get("default"),
            "description": obj.get("description"),
            "score": obj.get("score"),
            "text_matches": [SearchResultTextMatchesInner.from_dict(_item) for _item in obj["text_matches"]] if obj.get("text_matches") is not None else None
        })
        return _obj


