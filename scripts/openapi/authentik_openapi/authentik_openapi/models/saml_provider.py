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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.digest_algorithm_enum import DigestAlgorithmEnum
from authentik_openapi.models.signature_algorithm_enum import SignatureAlgorithmEnum
from authentik_openapi.models.sp_binding_enum import SpBindingEnum
from typing import Optional, Set
from typing_extensions import Self

class SAMLProvider(BaseModel):
    """
    SAMLProvider Serializer
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: StrictStr = Field(description="Flow used when authorizing this provider.")
    property_mappings: Optional[List[StrictStr]] = None
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    assigned_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_application_name: StrictStr = Field(description="Application's display Name.")
    assigned_backchannel_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_backchannel_application_name: StrictStr = Field(description="Application's display Name.")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    acs_url: Annotated[str, Field(strict=True, max_length=200)]
    audience: Optional[StrictStr] = Field(default=None, description="Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added.")
    issuer: Optional[StrictStr] = Field(default=None, description="Also known as EntityID")
    assertion_valid_not_before: Optional[StrictStr] = Field(default=None, description="Assertion valid not before current time + this value (Format: hours=-1;minutes=-2;seconds=-3).")
    assertion_valid_not_on_or_after: Optional[StrictStr] = Field(default=None, description="Assertion not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    session_valid_not_on_or_after: Optional[StrictStr] = Field(default=None, description="Session not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    name_id_mapping: Optional[StrictStr] = Field(default=None, description="Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered")
    digest_algorithm: Optional[DigestAlgorithmEnum] = None
    signature_algorithm: Optional[SignatureAlgorithmEnum] = None
    signing_kp: Optional[StrictStr] = Field(default=None, description="Keypair used to sign outgoing Responses going to the Service Provider.")
    verification_kp: Optional[StrictStr] = Field(default=None, description="When selected, incoming assertion's Signatures will be validated against this certificate. To allow unsigned Requests, leave on default.")
    sp_binding: Optional[SpBindingEnum] = Field(default=None, description="This determines how authentik sends the response back to the Service Provider.")
    default_relay_state: Optional[StrictStr] = Field(default=None, description="Default relay_state value for IDP-initiated logins")
    url_download_metadata: StrictStr = Field(description="Get metadata download URL")
    url_sso_post: StrictStr = Field(description="Get SSO Post URL")
    url_sso_redirect: StrictStr = Field(description="Get SSO Redirect URL")
    url_sso_init: StrictStr = Field(description="Get SSO IDP-Initiated URL")
    url_slo_post: StrictStr = Field(description="Get SLO POST URL")
    url_slo_redirect: StrictStr = Field(description="Get SLO redirect URL")
    __properties: ClassVar[List[str]] = ["pk", "name", "authentication_flow", "authorization_flow", "property_mappings", "component", "assigned_application_slug", "assigned_application_name", "assigned_backchannel_application_slug", "assigned_backchannel_application_name", "verbose_name", "verbose_name_plural", "meta_model_name", "acs_url", "audience", "issuer", "assertion_valid_not_before", "assertion_valid_not_on_or_after", "session_valid_not_on_or_after", "name_id_mapping", "digest_algorithm", "signature_algorithm", "signing_kp", "verification_kp", "sp_binding", "default_relay_state", "url_download_metadata", "url_sso_post", "url_sso_redirect", "url_sso_init", "url_slo_post", "url_slo_redirect"]

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
        """Create an instance of SAMLProvider from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "component",
            "assigned_application_slug",
            "assigned_application_name",
            "assigned_backchannel_application_slug",
            "assigned_backchannel_application_name",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
            "url_download_metadata",
            "url_sso_post",
            "url_sso_redirect",
            "url_sso_init",
            "url_slo_post",
            "url_slo_redirect",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if authentication_flow (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_flow is None and "authentication_flow" in self.model_fields_set:
            _dict['authentication_flow'] = None

        # set to None if name_id_mapping (nullable) is None
        # and model_fields_set contains the field
        if self.name_id_mapping is None and "name_id_mapping" in self.model_fields_set:
            _dict['name_id_mapping'] = None

        # set to None if signing_kp (nullable) is None
        # and model_fields_set contains the field
        if self.signing_kp is None and "signing_kp" in self.model_fields_set:
            _dict['signing_kp'] = None

        # set to None if verification_kp (nullable) is None
        # and model_fields_set contains the field
        if self.verification_kp is None and "verification_kp" in self.model_fields_set:
            _dict['verification_kp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SAMLProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "component": obj.get("component"),
            "assigned_application_slug": obj.get("assigned_application_slug"),
            "assigned_application_name": obj.get("assigned_application_name"),
            "assigned_backchannel_application_slug": obj.get("assigned_backchannel_application_slug"),
            "assigned_backchannel_application_name": obj.get("assigned_backchannel_application_name"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "acs_url": obj.get("acs_url"),
            "audience": obj.get("audience"),
            "issuer": obj.get("issuer"),
            "assertion_valid_not_before": obj.get("assertion_valid_not_before"),
            "assertion_valid_not_on_or_after": obj.get("assertion_valid_not_on_or_after"),
            "session_valid_not_on_or_after": obj.get("session_valid_not_on_or_after"),
            "name_id_mapping": obj.get("name_id_mapping"),
            "digest_algorithm": obj.get("digest_algorithm"),
            "signature_algorithm": obj.get("signature_algorithm"),
            "signing_kp": obj.get("signing_kp"),
            "verification_kp": obj.get("verification_kp"),
            "sp_binding": obj.get("sp_binding"),
            "default_relay_state": obj.get("default_relay_state"),
            "url_download_metadata": obj.get("url_download_metadata"),
            "url_sso_post": obj.get("url_sso_post"),
            "url_sso_redirect": obj.get("url_sso_redirect"),
            "url_sso_init": obj.get("url_sso_init"),
            "url_slo_post": obj.get("url_slo_post"),
            "url_slo_redirect": obj.get("url_slo_redirect")
        })
        return _obj


