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
from typing import Optional, Set
from typing_extensions import Self

class PagesHealthCheckDomain(BaseModel):
    """
    PagesHealthCheckDomain
    """ # noqa: E501
    host: Optional[StrictStr] = None
    uri: Optional[StrictStr] = None
    nameservers: Optional[StrictStr] = None
    dns_resolves: Optional[StrictBool] = None
    is_proxied: Optional[StrictBool] = None
    is_cloudflare_ip: Optional[StrictBool] = None
    is_fastly_ip: Optional[StrictBool] = None
    is_old_ip_address: Optional[StrictBool] = None
    is_a_record: Optional[StrictBool] = None
    has_cname_record: Optional[StrictBool] = None
    has_mx_records_present: Optional[StrictBool] = None
    is_valid_domain: Optional[StrictBool] = None
    is_apex_domain: Optional[StrictBool] = None
    should_be_a_record: Optional[StrictBool] = None
    is_cname_to_github_user_domain: Optional[StrictBool] = None
    is_cname_to_pages_dot_github_dot_com: Optional[StrictBool] = None
    is_cname_to_fastly: Optional[StrictBool] = None
    is_pointed_to_github_pages_ip: Optional[StrictBool] = None
    is_non_github_pages_ip_present: Optional[StrictBool] = None
    is_pages_domain: Optional[StrictBool] = None
    is_served_by_pages: Optional[StrictBool] = None
    is_valid: Optional[StrictBool] = None
    reason: Optional[StrictStr] = None
    responds_to_https: Optional[StrictBool] = None
    enforces_https: Optional[StrictBool] = None
    https_error: Optional[StrictStr] = None
    is_https_eligible: Optional[StrictBool] = None
    caa_error: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["host", "uri", "nameservers", "dns_resolves", "is_proxied", "is_cloudflare_ip", "is_fastly_ip", "is_old_ip_address", "is_a_record", "has_cname_record", "has_mx_records_present", "is_valid_domain", "is_apex_domain", "should_be_a_record", "is_cname_to_github_user_domain", "is_cname_to_pages_dot_github_dot_com", "is_cname_to_fastly", "is_pointed_to_github_pages_ip", "is_non_github_pages_ip_present", "is_pages_domain", "is_served_by_pages", "is_valid", "reason", "responds_to_https", "enforces_https", "https_error", "is_https_eligible", "caa_error"]

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
        """Create an instance of PagesHealthCheckDomain from a JSON string"""
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
        # set to None if is_proxied (nullable) is None
        # and model_fields_set contains the field
        if self.is_proxied is None and "is_proxied" in self.model_fields_set:
            _dict['is_proxied'] = None

        # set to None if is_cloudflare_ip (nullable) is None
        # and model_fields_set contains the field
        if self.is_cloudflare_ip is None and "is_cloudflare_ip" in self.model_fields_set:
            _dict['is_cloudflare_ip'] = None

        # set to None if is_fastly_ip (nullable) is None
        # and model_fields_set contains the field
        if self.is_fastly_ip is None and "is_fastly_ip" in self.model_fields_set:
            _dict['is_fastly_ip'] = None

        # set to None if is_old_ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.is_old_ip_address is None and "is_old_ip_address" in self.model_fields_set:
            _dict['is_old_ip_address'] = None

        # set to None if is_a_record (nullable) is None
        # and model_fields_set contains the field
        if self.is_a_record is None and "is_a_record" in self.model_fields_set:
            _dict['is_a_record'] = None

        # set to None if has_cname_record (nullable) is None
        # and model_fields_set contains the field
        if self.has_cname_record is None and "has_cname_record" in self.model_fields_set:
            _dict['has_cname_record'] = None

        # set to None if has_mx_records_present (nullable) is None
        # and model_fields_set contains the field
        if self.has_mx_records_present is None and "has_mx_records_present" in self.model_fields_set:
            _dict['has_mx_records_present'] = None

        # set to None if should_be_a_record (nullable) is None
        # and model_fields_set contains the field
        if self.should_be_a_record is None and "should_be_a_record" in self.model_fields_set:
            _dict['should_be_a_record'] = None

        # set to None if is_cname_to_github_user_domain (nullable) is None
        # and model_fields_set contains the field
        if self.is_cname_to_github_user_domain is None and "is_cname_to_github_user_domain" in self.model_fields_set:
            _dict['is_cname_to_github_user_domain'] = None

        # set to None if is_cname_to_pages_dot_github_dot_com (nullable) is None
        # and model_fields_set contains the field
        if self.is_cname_to_pages_dot_github_dot_com is None and "is_cname_to_pages_dot_github_dot_com" in self.model_fields_set:
            _dict['is_cname_to_pages_dot_github_dot_com'] = None

        # set to None if is_cname_to_fastly (nullable) is None
        # and model_fields_set contains the field
        if self.is_cname_to_fastly is None and "is_cname_to_fastly" in self.model_fields_set:
            _dict['is_cname_to_fastly'] = None

        # set to None if is_pointed_to_github_pages_ip (nullable) is None
        # and model_fields_set contains the field
        if self.is_pointed_to_github_pages_ip is None and "is_pointed_to_github_pages_ip" in self.model_fields_set:
            _dict['is_pointed_to_github_pages_ip'] = None

        # set to None if is_non_github_pages_ip_present (nullable) is None
        # and model_fields_set contains the field
        if self.is_non_github_pages_ip_present is None and "is_non_github_pages_ip_present" in self.model_fields_set:
            _dict['is_non_github_pages_ip_present'] = None

        # set to None if is_served_by_pages (nullable) is None
        # and model_fields_set contains the field
        if self.is_served_by_pages is None and "is_served_by_pages" in self.model_fields_set:
            _dict['is_served_by_pages'] = None

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if https_error (nullable) is None
        # and model_fields_set contains the field
        if self.https_error is None and "https_error" in self.model_fields_set:
            _dict['https_error'] = None

        # set to None if is_https_eligible (nullable) is None
        # and model_fields_set contains the field
        if self.is_https_eligible is None and "is_https_eligible" in self.model_fields_set:
            _dict['is_https_eligible'] = None

        # set to None if caa_error (nullable) is None
        # and model_fields_set contains the field
        if self.caa_error is None and "caa_error" in self.model_fields_set:
            _dict['caa_error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PagesHealthCheckDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "uri": obj.get("uri"),
            "nameservers": obj.get("nameservers"),
            "dns_resolves": obj.get("dns_resolves"),
            "is_proxied": obj.get("is_proxied"),
            "is_cloudflare_ip": obj.get("is_cloudflare_ip"),
            "is_fastly_ip": obj.get("is_fastly_ip"),
            "is_old_ip_address": obj.get("is_old_ip_address"),
            "is_a_record": obj.get("is_a_record"),
            "has_cname_record": obj.get("has_cname_record"),
            "has_mx_records_present": obj.get("has_mx_records_present"),
            "is_valid_domain": obj.get("is_valid_domain"),
            "is_apex_domain": obj.get("is_apex_domain"),
            "should_be_a_record": obj.get("should_be_a_record"),
            "is_cname_to_github_user_domain": obj.get("is_cname_to_github_user_domain"),
            "is_cname_to_pages_dot_github_dot_com": obj.get("is_cname_to_pages_dot_github_dot_com"),
            "is_cname_to_fastly": obj.get("is_cname_to_fastly"),
            "is_pointed_to_github_pages_ip": obj.get("is_pointed_to_github_pages_ip"),
            "is_non_github_pages_ip_present": obj.get("is_non_github_pages_ip_present"),
            "is_pages_domain": obj.get("is_pages_domain"),
            "is_served_by_pages": obj.get("is_served_by_pages"),
            "is_valid": obj.get("is_valid"),
            "reason": obj.get("reason"),
            "responds_to_https": obj.get("responds_to_https"),
            "enforces_https": obj.get("enforces_https"),
            "https_error": obj.get("https_error"),
            "is_https_eligible": obj.get("is_https_eligible"),
            "caa_error": obj.get("caa_error")
        })
        return _obj

