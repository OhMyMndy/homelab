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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.gpg_key_emails_inner import GpgKeyEmailsInner
from typing import Optional, Set
from typing_extensions import Self

class GpgKeySubkeysInner(BaseModel):
    """
    GpgKeySubkeysInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    primary_key_id: Optional[StrictInt] = None
    key_id: Optional[StrictStr] = None
    public_key: Optional[StrictStr] = None
    emails: Optional[List[GpgKeyEmailsInner]] = None
    subkeys: Optional[List[Any]] = None
    can_sign: Optional[StrictBool] = None
    can_encrypt_comms: Optional[StrictBool] = None
    can_encrypt_storage: Optional[StrictBool] = None
    can_certify: Optional[StrictBool] = None
    created_at: Optional[StrictStr] = None
    expires_at: Optional[StrictStr] = None
    raw_key: Optional[StrictStr] = None
    revoked: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "primary_key_id", "key_id", "public_key", "emails", "subkeys", "can_sign", "can_encrypt_comms", "can_encrypt_storage", "can_certify", "created_at", "expires_at", "raw_key", "revoked"]

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
        """Create an instance of GpgKeySubkeysInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item_emails in self.emails:
                if _item_emails:
                    _items.append(_item_emails.to_dict())
            _dict['emails'] = _items
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if raw_key (nullable) is None
        # and model_fields_set contains the field
        if self.raw_key is None and "raw_key" in self.model_fields_set:
            _dict['raw_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GpgKeySubkeysInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "primary_key_id": obj.get("primary_key_id"),
            "key_id": obj.get("key_id"),
            "public_key": obj.get("public_key"),
            "emails": [GpgKeyEmailsInner.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "subkeys": obj.get("subkeys"),
            "can_sign": obj.get("can_sign"),
            "can_encrypt_comms": obj.get("can_encrypt_comms"),
            "can_encrypt_storage": obj.get("can_encrypt_storage"),
            "can_certify": obj.get("can_certify"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at"),
            "raw_key": obj.get("raw_key"),
            "revoked": obj.get("revoked")
        })
        return _obj


