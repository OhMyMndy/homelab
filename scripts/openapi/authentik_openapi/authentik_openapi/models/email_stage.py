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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.flow_set import FlowSet
from typing import Optional, Set
from typing_extensions import Self

class EmailStage(BaseModel):
    """
    EmailStage Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    component: StrictStr = Field(description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    flow_set: Optional[List[FlowSet]] = None
    use_global_settings: Optional[StrictBool] = Field(default=None, description="When enabled, global Email connection settings will be used and connection settings below will be ignored.")
    host: Optional[StrictStr] = None
    port: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    username: Optional[StrictStr] = None
    use_tls: Optional[StrictBool] = None
    use_ssl: Optional[StrictBool] = None
    timeout: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    from_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = None
    token_expiry: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="Time in minutes the token sent is valid.")
    subject: Optional[StrictStr] = None
    template: Optional[StrictStr] = None
    activate_user_on_success: Optional[StrictBool] = Field(default=None, description="Activate users upon completion of stage.")
    __properties: ClassVar[List[str]] = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "use_global_settings", "host", "port", "username", "use_tls", "use_ssl", "timeout", "from_address", "token_expiry", "subject", "template", "activate_user_on_success"]

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
        """Create an instance of EmailStage from a JSON string"""
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
            "pk",
            "component",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item_flow_set in self.flow_set:
                if _item_flow_set:
                    _items.append(_item_flow_set.to_dict())
            _dict['flow_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmailStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj["flow_set"]] if obj.get("flow_set") is not None else None,
            "use_global_settings": obj.get("use_global_settings"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "username": obj.get("username"),
            "use_tls": obj.get("use_tls"),
            "use_ssl": obj.get("use_ssl"),
            "timeout": obj.get("timeout"),
            "from_address": obj.get("from_address"),
            "token_expiry": obj.get("token_expiry"),
            "subject": obj.get("subject"),
            "template": obj.get("template"),
            "activate_user_on_success": obj.get("activate_user_on_success")
        })
        return _obj


