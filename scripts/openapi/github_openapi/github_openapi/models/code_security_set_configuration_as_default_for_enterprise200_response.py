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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
from typing import Optional, Set
from typing_extensions import Self

class CodeSecuritySetConfigurationAsDefaultForEnterprise200Response(BaseModel):
    """
    CodeSecuritySetConfigurationAsDefaultForEnterprise200Response
    """ # noqa: E501
    default_for_new_repos: Optional[StrictStr] = Field(default=None, description="Specifies which types of repository this security configuration is applied to by default.")
    configuration: Optional[CodeSecurityConfiguration] = None
    __properties: ClassVar[List[str]] = ["default_for_new_repos", "configuration"]

    @field_validator('default_for_new_repos')
    def default_for_new_repos_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['all', 'none', 'private_and_internal', 'public']):
            raise ValueError("must be one of enum values ('all', 'none', 'private_and_internal', 'public')")
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
        """Create an instance of CodeSecuritySetConfigurationAsDefaultForEnterprise200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeSecuritySetConfigurationAsDefaultForEnterprise200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default_for_new_repos": obj.get("default_for_new_repos"),
            "configuration": CodeSecurityConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None
        })
        return _obj


