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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.webhook_registry_package_published_registry_package_owner import WebhookRegistryPackagePublishedRegistryPackageOwner
from github_openapi.models.webhook_registry_package_published_registry_package_package_version import WebhookRegistryPackagePublishedRegistryPackagePackageVersion
from github_openapi.models.webhook_registry_package_published_registry_package_registry import WebhookRegistryPackagePublishedRegistryPackageRegistry
from typing import Optional, Set
from typing_extensions import Self

class WebhookRegistryPackagePublishedRegistryPackage(BaseModel):
    """
    WebhookRegistryPackagePublishedRegistryPackage
    """ # noqa: E501
    created_at: Optional[StrictStr]
    description: Optional[StrictStr]
    ecosystem: StrictStr
    html_url: StrictStr
    id: StrictInt
    name: StrictStr
    namespace: StrictStr
    owner: WebhookRegistryPackagePublishedRegistryPackageOwner
    package_type: StrictStr
    package_version: Optional[WebhookRegistryPackagePublishedRegistryPackagePackageVersion]
    registry: Optional[WebhookRegistryPackagePublishedRegistryPackageRegistry]
    updated_at: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["created_at", "description", "ecosystem", "html_url", "id", "name", "namespace", "owner", "package_type", "package_version", "registry", "updated_at"]

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
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package_version
        if self.package_version:
            _dict['package_version'] = self.package_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of registry
        if self.registry:
            _dict['registry'] = self.registry.to_dict()
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if package_version (nullable) is None
        # and model_fields_set contains the field
        if self.package_version is None and "package_version" in self.model_fields_set:
            _dict['package_version'] = None

        # set to None if registry (nullable) is None
        # and model_fields_set contains the field
        if self.registry is None and "registry" in self.model_fields_set:
            _dict['registry'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "ecosystem": obj.get("ecosystem"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "owner": WebhookRegistryPackagePublishedRegistryPackageOwner.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "package_type": obj.get("package_type"),
            "package_version": WebhookRegistryPackagePublishedRegistryPackagePackageVersion.from_dict(obj["package_version"]) if obj.get("package_version") is not None else None,
            "registry": WebhookRegistryPackagePublishedRegistryPackageRegistry.from_dict(obj["registry"]) if obj.get("registry") is not None else None,
            "updated_at": obj.get("updated_at")
        })
        return _obj


