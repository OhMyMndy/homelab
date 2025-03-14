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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from authentik_openapi.models.app_enum import AppEnum
from authentik_openapi.models.event_actions import EventActions
from authentik_openapi.models.model_enum import ModelEnum
from typing import Optional, Set
from typing_extensions import Self

class EventMatcherPolicy(BaseModel):
    """
    Event Matcher Policy Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    execution_logging: Optional[StrictBool] = Field(default=None, description="When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.")
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    bound_to: StrictInt = Field(description="Return objects policy is bound to")
    action: Optional[EventActions] = Field(default=None, description="Match created events with this action type. When left empty, all action types will be matched.")
    client_ip: Optional[StrictStr] = Field(default=None, description="Matches Event's Client IP (strict matching, for network matching use an Expression Policy)")
    app: Optional[AppEnum] = Field(default=None, description="Match events created by selected application. When left empty, all applications are matched.")
    model: Optional[ModelEnum] = Field(default=None, description="Match events created by selected model. When left empty, all models are matched. When an app is selected, all the application's models are matched.")
    __properties: ClassVar[List[str]] = ["pk", "name", "execution_logging", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "bound_to", "action", "client_ip", "app", "model"]

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
        """Create an instance of EventMatcherPolicy from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "component",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
            "bound_to",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if client_ip (nullable) is None
        # and model_fields_set contains the field
        if self.client_ip is None and "client_ip" in self.model_fields_set:
            _dict['client_ip'] = None

        # set to None if app (nullable) is None
        # and model_fields_set contains the field
        if self.app is None and "app" in self.model_fields_set:
            _dict['app'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventMatcherPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "execution_logging": obj.get("execution_logging"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "bound_to": obj.get("bound_to"),
            "action": obj.get("action"),
            "client_ip": obj.get("client_ip"),
            "app": obj.get("app"),
            "model": obj.get("model")
        })
        return _obj


