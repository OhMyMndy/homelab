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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.api_overview_domains import ApiOverviewDomains
from github_openapi.models.api_overview_ssh_key_fingerprints import ApiOverviewSshKeyFingerprints
from typing import Optional, Set
from typing_extensions import Self

class ApiOverview(BaseModel):
    """
    Api Overview
    """ # noqa: E501
    verifiable_password_authentication: StrictBool
    ssh_key_fingerprints: Optional[ApiOverviewSshKeyFingerprints] = None
    ssh_keys: Optional[List[StrictStr]] = None
    hooks: Optional[List[StrictStr]] = None
    github_enterprise_importer: Optional[List[StrictStr]] = None
    web: Optional[List[StrictStr]] = None
    api: Optional[List[StrictStr]] = None
    git: Optional[List[StrictStr]] = None
    packages: Optional[List[StrictStr]] = None
    pages: Optional[List[StrictStr]] = None
    importer: Optional[List[StrictStr]] = None
    actions: Optional[List[StrictStr]] = None
    actions_macos: Optional[List[StrictStr]] = None
    codespaces: Optional[List[StrictStr]] = None
    dependabot: Optional[List[StrictStr]] = None
    copilot: Optional[List[StrictStr]] = None
    domains: Optional[ApiOverviewDomains] = None
    __properties: ClassVar[List[str]] = ["verifiable_password_authentication", "ssh_key_fingerprints", "ssh_keys", "hooks", "github_enterprise_importer", "web", "api", "git", "packages", "pages", "importer", "actions", "actions_macos", "codespaces", "dependabot", "copilot", "domains"]

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
        """Create an instance of ApiOverview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ssh_key_fingerprints
        if self.ssh_key_fingerprints:
            _dict['ssh_key_fingerprints'] = self.ssh_key_fingerprints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domains
        if self.domains:
            _dict['domains'] = self.domains.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiOverview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "verifiable_password_authentication": obj.get("verifiable_password_authentication"),
            "ssh_key_fingerprints": ApiOverviewSshKeyFingerprints.from_dict(obj["ssh_key_fingerprints"]) if obj.get("ssh_key_fingerprints") is not None else None,
            "ssh_keys": obj.get("ssh_keys"),
            "hooks": obj.get("hooks"),
            "github_enterprise_importer": obj.get("github_enterprise_importer"),
            "web": obj.get("web"),
            "api": obj.get("api"),
            "git": obj.get("git"),
            "packages": obj.get("packages"),
            "pages": obj.get("pages"),
            "importer": obj.get("importer"),
            "actions": obj.get("actions"),
            "actions_macos": obj.get("actions_macos"),
            "codespaces": obj.get("codespaces"),
            "dependabot": obj.get("dependabot"),
            "copilot": obj.get("copilot"),
            "domains": ApiOverviewDomains.from_dict(obj["domains"]) if obj.get("domains") is not None else None
        })
        return _obj


