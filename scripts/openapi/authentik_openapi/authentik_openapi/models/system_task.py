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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from authentik_openapi.models.log_event import LogEvent
from authentik_openapi.models.system_task_status_enum import SystemTaskStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class SystemTask(BaseModel):
    """
    Serialize TaskInfo and TaskResult
    """ # noqa: E501
    uuid: StrictStr
    name: StrictStr
    full_name: StrictStr = Field(description="Get full name with UID")
    uid: Optional[StrictStr] = None
    description: StrictStr
    start_timestamp: datetime
    finish_timestamp: datetime
    duration: Union[StrictFloat, StrictInt]
    status: SystemTaskStatusEnum
    messages: List[LogEvent]
    expires: Optional[datetime] = None
    expiring: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["uuid", "name", "full_name", "uid", "description", "start_timestamp", "finish_timestamp", "duration", "status", "messages", "expires", "expiring"]

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
        """Create an instance of SystemTask from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "uuid",
            "full_name",
            "start_timestamp",
            "finish_timestamp",
            "duration",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item_messages in self.messages:
                if _item_messages:
                    _items.append(_item_messages.to_dict())
            _dict['messages'] = _items
        # set to None if expires (nullable) is None
        # and model_fields_set contains the field
        if self.expires is None and "expires" in self.model_fields_set:
            _dict['expires'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "full_name": obj.get("full_name"),
            "uid": obj.get("uid"),
            "description": obj.get("description"),
            "start_timestamp": obj.get("start_timestamp"),
            "finish_timestamp": obj.get("finish_timestamp"),
            "duration": obj.get("duration"),
            "status": obj.get("status"),
            "messages": [LogEvent.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None,
            "expires": obj.get("expires"),
            "expiring": obj.get("expiring")
        })
        return _obj

