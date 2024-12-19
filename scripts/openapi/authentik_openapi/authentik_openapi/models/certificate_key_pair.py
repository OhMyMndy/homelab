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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CertificateKeyPair(BaseModel):
    """
    CertificateKeyPair Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    fingerprint_sha256: Optional[StrictStr] = Field(description="Get certificate Hash (SHA256)")
    fingerprint_sha1: Optional[StrictStr] = Field(description="Get certificate Hash (SHA1)")
    cert_expiry: Optional[datetime] = Field(description="Get certificate expiry")
    cert_subject: Optional[StrictStr] = Field(description="Get certificate subject as full rfc4514")
    private_key_available: StrictBool = Field(description="Show if this keypair has a private key configured or not")
    private_key_type: Optional[StrictStr] = Field(description="Get the private key's type, if set")
    certificate_download_url: StrictStr = Field(description="Get URL to download certificate")
    private_key_download_url: StrictStr = Field(description="Get URL to download private key")
    managed: Optional[StrictStr] = Field(description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    __properties: ClassVar[List[str]] = ["pk", "name", "fingerprint_sha256", "fingerprint_sha1", "cert_expiry", "cert_subject", "private_key_available", "private_key_type", "certificate_download_url", "private_key_download_url", "managed"]

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
        """Create an instance of CertificateKeyPair from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "fingerprint_sha256",
            "fingerprint_sha1",
            "cert_expiry",
            "cert_subject",
            "private_key_available",
            "private_key_type",
            "certificate_download_url",
            "private_key_download_url",
            "managed",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if fingerprint_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint_sha256 is None and "fingerprint_sha256" in self.model_fields_set:
            _dict['fingerprint_sha256'] = None

        # set to None if fingerprint_sha1 (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint_sha1 is None and "fingerprint_sha1" in self.model_fields_set:
            _dict['fingerprint_sha1'] = None

        # set to None if cert_expiry (nullable) is None
        # and model_fields_set contains the field
        if self.cert_expiry is None and "cert_expiry" in self.model_fields_set:
            _dict['cert_expiry'] = None

        # set to None if cert_subject (nullable) is None
        # and model_fields_set contains the field
        if self.cert_subject is None and "cert_subject" in self.model_fields_set:
            _dict['cert_subject'] = None

        # set to None if private_key_type (nullable) is None
        # and model_fields_set contains the field
        if self.private_key_type is None and "private_key_type" in self.model_fields_set:
            _dict['private_key_type'] = None

        # set to None if managed (nullable) is None
        # and model_fields_set contains the field
        if self.managed is None and "managed" in self.model_fields_set:
            _dict['managed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateKeyPair from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "fingerprint_sha256": obj.get("fingerprint_sha256"),
            "fingerprint_sha1": obj.get("fingerprint_sha1"),
            "cert_expiry": obj.get("cert_expiry"),
            "cert_subject": obj.get("cert_subject"),
            "private_key_available": obj.get("private_key_available"),
            "private_key_type": obj.get("private_key_type"),
            "certificate_download_url": obj.get("certificate_download_url"),
            "private_key_download_url": obj.get("private_key_download_url"),
            "managed": obj.get("managed")
        })
        return _obj


