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
from enum import Enum
from typing_extensions import Self


class AppEnum(str, Enum):
    """
    AppEnum
    """

    """
    allowed enum values
    """
    AUTHENTIK_DOT_TENANTS = 'authentik.tenants'
    AUTHENTIK_DOT_ADMIN = 'authentik.admin'
    AUTHENTIK_DOT_API = 'authentik.api'
    AUTHENTIK_DOT_CRYPTO = 'authentik.crypto'
    AUTHENTIK_DOT_FLOWS = 'authentik.flows'
    AUTHENTIK_DOT_OUTPOSTS = 'authentik.outposts'
    AUTHENTIK_DOT_POLICIES_DOT_DUMMY = 'authentik.policies.dummy'
    AUTHENTIK_DOT_POLICIES_DOT_EVENT_MATCHER = 'authentik.policies.event_matcher'
    AUTHENTIK_DOT_POLICIES_DOT_EXPIRY = 'authentik.policies.expiry'
    AUTHENTIK_DOT_POLICIES_DOT_EXPRESSION = 'authentik.policies.expression'
    AUTHENTIK_DOT_POLICIES_DOT_PASSWORD = 'authentik.policies.password'
    AUTHENTIK_DOT_POLICIES_DOT_REPUTATION = 'authentik.policies.reputation'
    AUTHENTIK_DOT_POLICIES = 'authentik.policies'
    AUTHENTIK_DOT_PROVIDERS_DOT_LDAP = 'authentik.providers.ldap'
    AUTHENTIK_DOT_PROVIDERS_DOT_OAUTH2 = 'authentik.providers.oauth2'
    AUTHENTIK_DOT_PROVIDERS_DOT_PROXY = 'authentik.providers.proxy'
    AUTHENTIK_DOT_PROVIDERS_DOT_RADIUS = 'authentik.providers.radius'
    AUTHENTIK_DOT_PROVIDERS_DOT_SAML = 'authentik.providers.saml'
    AUTHENTIK_DOT_PROVIDERS_DOT_SCIM = 'authentik.providers.scim'
    AUTHENTIK_DOT_RBAC = 'authentik.rbac'
    AUTHENTIK_DOT_RECOVERY = 'authentik.recovery'
    AUTHENTIK_DOT_SOURCES_DOT_LDAP = 'authentik.sources.ldap'
    AUTHENTIK_DOT_SOURCES_DOT_OAUTH = 'authentik.sources.oauth'
    AUTHENTIK_DOT_SOURCES_DOT_PLEX = 'authentik.sources.plex'
    AUTHENTIK_DOT_SOURCES_DOT_SAML = 'authentik.sources.saml'
    AUTHENTIK_DOT_SOURCES_DOT_SCIM = 'authentik.sources.scim'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR = 'authentik.stages.authenticator'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_DUO = 'authentik.stages.authenticator_duo'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_SMS = 'authentik.stages.authenticator_sms'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_STATIC = 'authentik.stages.authenticator_static'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_TOTP = 'authentik.stages.authenticator_totp'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_VALIDATE = 'authentik.stages.authenticator_validate'
    AUTHENTIK_DOT_STAGES_DOT_AUTHENTICATOR_WEBAUTHN = 'authentik.stages.authenticator_webauthn'
    AUTHENTIK_DOT_STAGES_DOT_CAPTCHA = 'authentik.stages.captcha'
    AUTHENTIK_DOT_STAGES_DOT_CONSENT = 'authentik.stages.consent'
    AUTHENTIK_DOT_STAGES_DOT_DENY = 'authentik.stages.deny'
    AUTHENTIK_DOT_STAGES_DOT_DUMMY = 'authentik.stages.dummy'
    AUTHENTIK_DOT_STAGES_DOT_EMAIL = 'authentik.stages.email'
    AUTHENTIK_DOT_STAGES_DOT_IDENTIFICATION = 'authentik.stages.identification'
    AUTHENTIK_DOT_STAGES_DOT_INVITATION = 'authentik.stages.invitation'
    AUTHENTIK_DOT_STAGES_DOT_PASSWORD = 'authentik.stages.password'
    AUTHENTIK_DOT_STAGES_DOT_PROMPT = 'authentik.stages.prompt'
    AUTHENTIK_DOT_STAGES_DOT_USER_DELETE = 'authentik.stages.user_delete'
    AUTHENTIK_DOT_STAGES_DOT_USER_LOGIN = 'authentik.stages.user_login'
    AUTHENTIK_DOT_STAGES_DOT_USER_LOGOUT = 'authentik.stages.user_logout'
    AUTHENTIK_DOT_STAGES_DOT_USER_WRITE = 'authentik.stages.user_write'
    AUTHENTIK_DOT_BRANDS = 'authentik.brands'
    AUTHENTIK_DOT_BLUEPRINTS = 'authentik.blueprints'
    AUTHENTIK_DOT_CORE = 'authentik.core'
    AUTHENTIK_DOT_ENTERPRISE = 'authentik.enterprise'
    AUTHENTIK_DOT_ENTERPRISE_DOT_AUDIT = 'authentik.enterprise.audit'
    AUTHENTIK_DOT_ENTERPRISE_DOT_PROVIDERS_DOT_GOOGLE_WORKSPACE = 'authentik.enterprise.providers.google_workspace'
    AUTHENTIK_DOT_ENTERPRISE_DOT_PROVIDERS_DOT_MICROSOFT_ENTRA = 'authentik.enterprise.providers.microsoft_entra'
    AUTHENTIK_DOT_ENTERPRISE_DOT_PROVIDERS_DOT_RAC = 'authentik.enterprise.providers.rac'
    AUTHENTIK_DOT_ENTERPRISE_DOT_STAGES_DOT_SOURCE = 'authentik.enterprise.stages.source'
    AUTHENTIK_DOT_EVENTS = 'authentik.events'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppEnum from a JSON string"""
        return cls(json.loads(json_str))


