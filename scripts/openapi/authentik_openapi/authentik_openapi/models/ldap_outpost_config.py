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
from typing_extensions import Annotated
from authentik_openapi.models.ldapapi_access_mode import LDAPAPIAccessMode
from typing import Optional, Set
from typing_extensions import Self

class LDAPOutpostConfig(BaseModel):
    """
    LDAPProvider Serializer
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    base_dn: Optional[StrictStr] = Field(default=None, description="DN under which objects are accessible.")
    bind_flow_slug: StrictStr
    application_slug: StrictStr = Field(description="Prioritise backchannel slug over direct application slug")
    search_group: Optional[StrictStr] = Field(default=None, description="Users in this group can do search queries. If not set, every user can execute search queries.")
    certificate: Optional[StrictStr] = None
    tls_server_name: Optional[StrictStr] = None
    uid_start_number: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren't too low for POSIX users. Default is 2000 to ensure that we don't collide with local users uidNumber")
    gid_start_number: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren't too low for POSIX groups. Default is 4000 to ensure that we don't collide with local groups or users primary groups gidNumber")
    search_mode: Optional[LDAPAPIAccessMode] = None
    bind_mode: Optional[LDAPAPIAccessMode] = None
    mfa_support: Optional[StrictBool] = Field(default=None, description="When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon.")
    __properties: ClassVar[List[str]] = ["pk", "name", "base_dn", "bind_flow_slug", "application_slug", "search_group", "certificate", "tls_server_name", "uid_start_number", "gid_start_number", "search_mode", "bind_mode", "mfa_support"]

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
        """Create an instance of LDAPOutpostConfig from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pk",
            "application_slug",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if search_group (nullable) is None
        # and model_fields_set contains the field
        if self.search_group is None and "search_group" in self.model_fields_set:
            _dict['search_group'] = None

        # set to None if certificate (nullable) is None
        # and model_fields_set contains the field
        if self.certificate is None and "certificate" in self.model_fields_set:
            _dict['certificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LDAPOutpostConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "base_dn": obj.get("base_dn"),
            "bind_flow_slug": obj.get("bind_flow_slug"),
            "application_slug": obj.get("application_slug"),
            "search_group": obj.get("search_group"),
            "certificate": obj.get("certificate"),
            "tls_server_name": obj.get("tls_server_name"),
            "uid_start_number": obj.get("uid_start_number"),
            "gid_start_number": obj.get("gid_start_number"),
            "search_mode": obj.get("search_mode"),
            "bind_mode": obj.get("bind_mode"),
            "mfa_support": obj.get("mfa_support")
        })
        return _obj


