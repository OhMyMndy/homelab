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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest
from authentik_openapi.models.ldap_provider_request import LDAPProviderRequest
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest
from authentik_openapi.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik_openapi.models.proxy_provider_request import ProxyProviderRequest
from authentik_openapi.models.rac_provider_request import RACProviderRequest
from authentik_openapi.models.radius_provider_request import RadiusProviderRequest
from authentik_openapi.models.saml_provider_request import SAMLProviderRequest
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

MODELREQUEST_ONE_OF_SCHEMAS = ["GoogleWorkspaceProviderRequest", "LDAPProviderRequest", "MicrosoftEntraProviderRequest", "OAuth2ProviderRequest", "ProxyProviderRequest", "RACProviderRequest", "RadiusProviderRequest", "SAMLProviderRequest", "SCIMProviderRequest"]

class ModelRequest(BaseModel):
    """
    ModelRequest
    """
    # data type: GoogleWorkspaceProviderRequest
    oneof_schema_1_validator: Optional[GoogleWorkspaceProviderRequest] = None
    # data type: LDAPProviderRequest
    oneof_schema_2_validator: Optional[LDAPProviderRequest] = None
    # data type: MicrosoftEntraProviderRequest
    oneof_schema_3_validator: Optional[MicrosoftEntraProviderRequest] = None
    # data type: OAuth2ProviderRequest
    oneof_schema_4_validator: Optional[OAuth2ProviderRequest] = None
    # data type: ProxyProviderRequest
    oneof_schema_5_validator: Optional[ProxyProviderRequest] = None
    # data type: RACProviderRequest
    oneof_schema_6_validator: Optional[RACProviderRequest] = None
    # data type: RadiusProviderRequest
    oneof_schema_7_validator: Optional[RadiusProviderRequest] = None
    # data type: SAMLProviderRequest
    oneof_schema_8_validator: Optional[SAMLProviderRequest] = None
    # data type: SCIMProviderRequest
    oneof_schema_9_validator: Optional[SCIMProviderRequest] = None
    actual_instance: Optional[Union[GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest]] = None
    one_of_schemas: Set[str] = { "GoogleWorkspaceProviderRequest", "LDAPProviderRequest", "MicrosoftEntraProviderRequest", "OAuth2ProviderRequest", "ProxyProviderRequest", "RACProviderRequest", "RadiusProviderRequest", "SAMLProviderRequest", "SCIMProviderRequest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ModelRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: GoogleWorkspaceProviderRequest
        if not isinstance(v, GoogleWorkspaceProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GoogleWorkspaceProviderRequest`")
        else:
            match += 1
        # validate data type: LDAPProviderRequest
        if not isinstance(v, LDAPProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LDAPProviderRequest`")
        else:
            match += 1
        # validate data type: MicrosoftEntraProviderRequest
        if not isinstance(v, MicrosoftEntraProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MicrosoftEntraProviderRequest`")
        else:
            match += 1
        # validate data type: OAuth2ProviderRequest
        if not isinstance(v, OAuth2ProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuth2ProviderRequest`")
        else:
            match += 1
        # validate data type: ProxyProviderRequest
        if not isinstance(v, ProxyProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProxyProviderRequest`")
        else:
            match += 1
        # validate data type: RACProviderRequest
        if not isinstance(v, RACProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RACProviderRequest`")
        else:
            match += 1
        # validate data type: RadiusProviderRequest
        if not isinstance(v, RadiusProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RadiusProviderRequest`")
        else:
            match += 1
        # validate data type: SAMLProviderRequest
        if not isinstance(v, SAMLProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SAMLProviderRequest`")
        else:
            match += 1
        # validate data type: SCIMProviderRequest
        if not isinstance(v, SCIMProviderRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SCIMProviderRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ModelRequest with oneOf schemas: GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ModelRequest with oneOf schemas: GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into GoogleWorkspaceProviderRequest
        try:
            instance.actual_instance = GoogleWorkspaceProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LDAPProviderRequest
        try:
            instance.actual_instance = LDAPProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MicrosoftEntraProviderRequest
        try:
            instance.actual_instance = MicrosoftEntraProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuth2ProviderRequest
        try:
            instance.actual_instance = OAuth2ProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProxyProviderRequest
        try:
            instance.actual_instance = ProxyProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RACProviderRequest
        try:
            instance.actual_instance = RACProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RadiusProviderRequest
        try:
            instance.actual_instance = RadiusProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SAMLProviderRequest
        try:
            instance.actual_instance = SAMLProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SCIMProviderRequest
        try:
            instance.actual_instance = SCIMProviderRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ModelRequest with oneOf schemas: GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ModelRequest with oneOf schemas: GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], GoogleWorkspaceProviderRequest, LDAPProviderRequest, MicrosoftEntraProviderRequest, OAuth2ProviderRequest, ProxyProviderRequest, RACProviderRequest, RadiusProviderRequest, SAMLProviderRequest, SCIMProviderRequest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


