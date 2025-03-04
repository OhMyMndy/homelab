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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.repos_update_request_security_and_analysis_advanced_security import ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning import ReposUpdateRequestSecurityAndAnalysisSecretScanning
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_ai_detection import ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns import ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_push_protection import ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection
from typing import Optional, Set
from typing_extensions import Self

class ReposUpdateRequestSecurityAndAnalysis(BaseModel):
    """
    Specify which security and analysis features to enable or disable for the repository.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  For example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request: `{ \"security_and_analysis\": {\"advanced_security\": { \"status\": \"enabled\" } } }`.  You can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.
    """ # noqa: E501
    advanced_security: Optional[ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity] = None
    secret_scanning: Optional[ReposUpdateRequestSecurityAndAnalysisSecretScanning] = None
    secret_scanning_push_protection: Optional[ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection] = None
    secret_scanning_ai_detection: Optional[ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection] = None
    secret_scanning_non_provider_patterns: Optional[ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns] = None
    __properties: ClassVar[List[str]] = ["advanced_security", "secret_scanning", "secret_scanning_push_protection", "secret_scanning_ai_detection", "secret_scanning_non_provider_patterns"]

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
        """Create an instance of ReposUpdateRequestSecurityAndAnalysis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of advanced_security
        if self.advanced_security:
            _dict['advanced_security'] = self.advanced_security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_scanning
        if self.secret_scanning:
            _dict['secret_scanning'] = self.secret_scanning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_scanning_push_protection
        if self.secret_scanning_push_protection:
            _dict['secret_scanning_push_protection'] = self.secret_scanning_push_protection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_scanning_ai_detection
        if self.secret_scanning_ai_detection:
            _dict['secret_scanning_ai_detection'] = self.secret_scanning_ai_detection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_scanning_non_provider_patterns
        if self.secret_scanning_non_provider_patterns:
            _dict['secret_scanning_non_provider_patterns'] = self.secret_scanning_non_provider_patterns.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReposUpdateRequestSecurityAndAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advanced_security": ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.from_dict(obj["advanced_security"]) if obj.get("advanced_security") is not None else None,
            "secret_scanning": ReposUpdateRequestSecurityAndAnalysisSecretScanning.from_dict(obj["secret_scanning"]) if obj.get("secret_scanning") is not None else None,
            "secret_scanning_push_protection": ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.from_dict(obj["secret_scanning_push_protection"]) if obj.get("secret_scanning_push_protection") is not None else None,
            "secret_scanning_ai_detection": ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection.from_dict(obj["secret_scanning_ai_detection"]) if obj.get("secret_scanning_ai_detection") is not None else None,
            "secret_scanning_non_provider_patterns": ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns.from_dict(obj["secret_scanning_non_provider_patterns"]) if obj.get("secret_scanning_non_provider_patterns") is not None else None
        })
        return _obj


