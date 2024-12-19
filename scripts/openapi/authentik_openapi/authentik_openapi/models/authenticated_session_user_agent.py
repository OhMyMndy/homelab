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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from authentik_openapi.models.authenticated_session_user_agent_device import AuthenticatedSessionUserAgentDevice
from authentik_openapi.models.authenticated_session_user_agent_os import AuthenticatedSessionUserAgentOs
from authentik_openapi.models.authenticated_session_user_agent_user_agent import AuthenticatedSessionUserAgentUserAgent
from typing import Optional, Set
from typing_extensions import Self

class AuthenticatedSessionUserAgent(BaseModel):
    """
    Get parsed user agent
    """ # noqa: E501
    device: AuthenticatedSessionUserAgentDevice
    os: AuthenticatedSessionUserAgentOs
    user_agent: AuthenticatedSessionUserAgentUserAgent
    string: StrictStr
    __properties: ClassVar[List[str]] = ["device", "os", "user_agent", "string"]

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
        """Create an instance of AuthenticatedSessionUserAgent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of os
        if self.os:
            _dict['os'] = self.os.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_agent
        if self.user_agent:
            _dict['user_agent'] = self.user_agent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticatedSessionUserAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "device": AuthenticatedSessionUserAgentDevice.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "os": AuthenticatedSessionUserAgentOs.from_dict(obj["os"]) if obj.get("os") is not None else None,
            "user_agent": AuthenticatedSessionUserAgentUserAgent.from_dict(obj["user_agent"]) if obj.get("user_agent") is not None else None,
            "string": obj.get("string")
        })
        return _obj


