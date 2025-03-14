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
from authentik_openapi.models.access_denied_challenge import AccessDeniedChallenge
from authentik_openapi.models.apple_login_challenge import AppleLoginChallenge
from authentik_openapi.models.authenticator_duo_challenge import AuthenticatorDuoChallenge
from authentik_openapi.models.authenticator_sms_challenge import AuthenticatorSMSChallenge
from authentik_openapi.models.authenticator_static_challenge import AuthenticatorStaticChallenge
from authentik_openapi.models.authenticator_totp_challenge import AuthenticatorTOTPChallenge
from authentik_openapi.models.authenticator_validation_challenge import AuthenticatorValidationChallenge
from authentik_openapi.models.authenticator_web_authn_challenge import AuthenticatorWebAuthnChallenge
from authentik_openapi.models.autosubmit_challenge import AutosubmitChallenge
from authentik_openapi.models.captcha_challenge import CaptchaChallenge
from authentik_openapi.models.consent_challenge import ConsentChallenge
from authentik_openapi.models.email_challenge import EmailChallenge
from authentik_openapi.models.flow_error_challenge import FlowErrorChallenge
from authentik_openapi.models.identification_challenge import IdentificationChallenge
from authentik_openapi.models.o_auth_device_code_challenge import OAuthDeviceCodeChallenge
from authentik_openapi.models.o_auth_device_code_finish_challenge import OAuthDeviceCodeFinishChallenge
from authentik_openapi.models.password_challenge import PasswordChallenge
from authentik_openapi.models.plex_authentication_challenge import PlexAuthenticationChallenge
from authentik_openapi.models.prompt_challenge import PromptChallenge
from authentik_openapi.models.redirect_challenge import RedirectChallenge
from authentik_openapi.models.shell_challenge import ShellChallenge
from authentik_openapi.models.user_login_challenge import UserLoginChallenge
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CHALLENGETYPES_ONE_OF_SCHEMAS = ["AccessDeniedChallenge", "AppleLoginChallenge", "AuthenticatorDuoChallenge", "AuthenticatorSMSChallenge", "AuthenticatorStaticChallenge", "AuthenticatorTOTPChallenge", "AuthenticatorValidationChallenge", "AuthenticatorWebAuthnChallenge", "AutosubmitChallenge", "CaptchaChallenge", "ConsentChallenge", "EmailChallenge", "FlowErrorChallenge", "IdentificationChallenge", "OAuthDeviceCodeChallenge", "OAuthDeviceCodeFinishChallenge", "PasswordChallenge", "PlexAuthenticationChallenge", "PromptChallenge", "RedirectChallenge", "ShellChallenge", "UserLoginChallenge"]

class ChallengeTypes(BaseModel):
    """
    ChallengeTypes
    """
    # data type: AccessDeniedChallenge
    oneof_schema_1_validator: Optional[AccessDeniedChallenge] = None
    # data type: AppleLoginChallenge
    oneof_schema_2_validator: Optional[AppleLoginChallenge] = None
    # data type: AuthenticatorDuoChallenge
    oneof_schema_3_validator: Optional[AuthenticatorDuoChallenge] = None
    # data type: AuthenticatorSMSChallenge
    oneof_schema_4_validator: Optional[AuthenticatorSMSChallenge] = None
    # data type: AuthenticatorStaticChallenge
    oneof_schema_5_validator: Optional[AuthenticatorStaticChallenge] = None
    # data type: AuthenticatorTOTPChallenge
    oneof_schema_6_validator: Optional[AuthenticatorTOTPChallenge] = None
    # data type: AuthenticatorValidationChallenge
    oneof_schema_7_validator: Optional[AuthenticatorValidationChallenge] = None
    # data type: AuthenticatorWebAuthnChallenge
    oneof_schema_8_validator: Optional[AuthenticatorWebAuthnChallenge] = None
    # data type: AutosubmitChallenge
    oneof_schema_9_validator: Optional[AutosubmitChallenge] = None
    # data type: CaptchaChallenge
    oneof_schema_10_validator: Optional[CaptchaChallenge] = None
    # data type: ConsentChallenge
    oneof_schema_11_validator: Optional[ConsentChallenge] = None
    # data type: EmailChallenge
    oneof_schema_12_validator: Optional[EmailChallenge] = None
    # data type: FlowErrorChallenge
    oneof_schema_13_validator: Optional[FlowErrorChallenge] = None
    # data type: IdentificationChallenge
    oneof_schema_14_validator: Optional[IdentificationChallenge] = None
    # data type: OAuthDeviceCodeChallenge
    oneof_schema_15_validator: Optional[OAuthDeviceCodeChallenge] = None
    # data type: OAuthDeviceCodeFinishChallenge
    oneof_schema_16_validator: Optional[OAuthDeviceCodeFinishChallenge] = None
    # data type: PasswordChallenge
    oneof_schema_17_validator: Optional[PasswordChallenge] = None
    # data type: PlexAuthenticationChallenge
    oneof_schema_18_validator: Optional[PlexAuthenticationChallenge] = None
    # data type: PromptChallenge
    oneof_schema_19_validator: Optional[PromptChallenge] = None
    # data type: RedirectChallenge
    oneof_schema_20_validator: Optional[RedirectChallenge] = None
    # data type: ShellChallenge
    oneof_schema_21_validator: Optional[ShellChallenge] = None
    # data type: UserLoginChallenge
    oneof_schema_22_validator: Optional[UserLoginChallenge] = None
    actual_instance: Optional[Union[AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge]] = None
    one_of_schemas: Set[str] = { "AccessDeniedChallenge", "AppleLoginChallenge", "AuthenticatorDuoChallenge", "AuthenticatorSMSChallenge", "AuthenticatorStaticChallenge", "AuthenticatorTOTPChallenge", "AuthenticatorValidationChallenge", "AuthenticatorWebAuthnChallenge", "AutosubmitChallenge", "CaptchaChallenge", "ConsentChallenge", "EmailChallenge", "FlowErrorChallenge", "IdentificationChallenge", "OAuthDeviceCodeChallenge", "OAuthDeviceCodeFinishChallenge", "PasswordChallenge", "PlexAuthenticationChallenge", "PromptChallenge", "RedirectChallenge", "ShellChallenge", "UserLoginChallenge" }

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
        instance = ChallengeTypes.model_construct()
        error_messages = []
        match = 0
        # validate data type: AccessDeniedChallenge
        if not isinstance(v, AccessDeniedChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccessDeniedChallenge`")
        else:
            match += 1
        # validate data type: AppleLoginChallenge
        if not isinstance(v, AppleLoginChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AppleLoginChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorDuoChallenge
        if not isinstance(v, AuthenticatorDuoChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorDuoChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorSMSChallenge
        if not isinstance(v, AuthenticatorSMSChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorSMSChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorStaticChallenge
        if not isinstance(v, AuthenticatorStaticChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorStaticChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorTOTPChallenge
        if not isinstance(v, AuthenticatorTOTPChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorTOTPChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorValidationChallenge
        if not isinstance(v, AuthenticatorValidationChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorValidationChallenge`")
        else:
            match += 1
        # validate data type: AuthenticatorWebAuthnChallenge
        if not isinstance(v, AuthenticatorWebAuthnChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AuthenticatorWebAuthnChallenge`")
        else:
            match += 1
        # validate data type: AutosubmitChallenge
        if not isinstance(v, AutosubmitChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AutosubmitChallenge`")
        else:
            match += 1
        # validate data type: CaptchaChallenge
        if not isinstance(v, CaptchaChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CaptchaChallenge`")
        else:
            match += 1
        # validate data type: ConsentChallenge
        if not isinstance(v, ConsentChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConsentChallenge`")
        else:
            match += 1
        # validate data type: EmailChallenge
        if not isinstance(v, EmailChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailChallenge`")
        else:
            match += 1
        # validate data type: FlowErrorChallenge
        if not isinstance(v, FlowErrorChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FlowErrorChallenge`")
        else:
            match += 1
        # validate data type: IdentificationChallenge
        if not isinstance(v, IdentificationChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentificationChallenge`")
        else:
            match += 1
        # validate data type: OAuthDeviceCodeChallenge
        if not isinstance(v, OAuthDeviceCodeChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuthDeviceCodeChallenge`")
        else:
            match += 1
        # validate data type: OAuthDeviceCodeFinishChallenge
        if not isinstance(v, OAuthDeviceCodeFinishChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuthDeviceCodeFinishChallenge`")
        else:
            match += 1
        # validate data type: PasswordChallenge
        if not isinstance(v, PasswordChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PasswordChallenge`")
        else:
            match += 1
        # validate data type: PlexAuthenticationChallenge
        if not isinstance(v, PlexAuthenticationChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlexAuthenticationChallenge`")
        else:
            match += 1
        # validate data type: PromptChallenge
        if not isinstance(v, PromptChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PromptChallenge`")
        else:
            match += 1
        # validate data type: RedirectChallenge
        if not isinstance(v, RedirectChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RedirectChallenge`")
        else:
            match += 1
        # validate data type: ShellChallenge
        if not isinstance(v, ShellChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ShellChallenge`")
        else:
            match += 1
        # validate data type: UserLoginChallenge
        if not isinstance(v, UserLoginChallenge):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserLoginChallenge`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ChallengeTypes with oneOf schemas: AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ChallengeTypes with oneOf schemas: AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge. Details: " + ", ".join(error_messages))
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

        # deserialize data into AccessDeniedChallenge
        try:
            instance.actual_instance = AccessDeniedChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AppleLoginChallenge
        try:
            instance.actual_instance = AppleLoginChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorDuoChallenge
        try:
            instance.actual_instance = AuthenticatorDuoChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorSMSChallenge
        try:
            instance.actual_instance = AuthenticatorSMSChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorStaticChallenge
        try:
            instance.actual_instance = AuthenticatorStaticChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorTOTPChallenge
        try:
            instance.actual_instance = AuthenticatorTOTPChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorValidationChallenge
        try:
            instance.actual_instance = AuthenticatorValidationChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AuthenticatorWebAuthnChallenge
        try:
            instance.actual_instance = AuthenticatorWebAuthnChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AutosubmitChallenge
        try:
            instance.actual_instance = AutosubmitChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CaptchaChallenge
        try:
            instance.actual_instance = CaptchaChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConsentChallenge
        try:
            instance.actual_instance = ConsentChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EmailChallenge
        try:
            instance.actual_instance = EmailChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FlowErrorChallenge
        try:
            instance.actual_instance = FlowErrorChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentificationChallenge
        try:
            instance.actual_instance = IdentificationChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuthDeviceCodeChallenge
        try:
            instance.actual_instance = OAuthDeviceCodeChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuthDeviceCodeFinishChallenge
        try:
            instance.actual_instance = OAuthDeviceCodeFinishChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PasswordChallenge
        try:
            instance.actual_instance = PasswordChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlexAuthenticationChallenge
        try:
            instance.actual_instance = PlexAuthenticationChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PromptChallenge
        try:
            instance.actual_instance = PromptChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RedirectChallenge
        try:
            instance.actual_instance = RedirectChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ShellChallenge
        try:
            instance.actual_instance = ShellChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserLoginChallenge
        try:
            instance.actual_instance = UserLoginChallenge.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ChallengeTypes with oneOf schemas: AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ChallengeTypes with oneOf schemas: AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AccessDeniedChallenge, AppleLoginChallenge, AuthenticatorDuoChallenge, AuthenticatorSMSChallenge, AuthenticatorStaticChallenge, AuthenticatorTOTPChallenge, AuthenticatorValidationChallenge, AuthenticatorWebAuthnChallenge, AutosubmitChallenge, CaptchaChallenge, ConsentChallenge, EmailChallenge, FlowErrorChallenge, IdentificationChallenge, OAuthDeviceCodeChallenge, OAuthDeviceCodeFinishChallenge, PasswordChallenge, PlexAuthenticationChallenge, PromptChallenge, RedirectChallenge, ShellChallenge, UserLoginChallenge]]:
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


