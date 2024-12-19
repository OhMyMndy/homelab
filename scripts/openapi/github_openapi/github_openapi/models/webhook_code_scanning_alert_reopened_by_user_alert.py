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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.alert_instance import AlertInstance
from github_openapi.models.webhook_code_scanning_alert_appeared_in_branch_alert_rule import WebhookCodeScanningAlertAppearedInBranchAlertRule
from github_openapi.models.webhook_code_scanning_alert_appeared_in_branch_alert_tool import WebhookCodeScanningAlertAppearedInBranchAlertTool
from typing import Optional, Set
from typing_extensions import Self

class WebhookCodeScanningAlertReopenedByUserAlert(BaseModel):
    """
    The code scanning alert involved in the event.
    """ # noqa: E501
    created_at: datetime = Field(description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`")
    dismissed_at: Optional[Any] = Field(description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.")
    dismissed_by: Optional[Any]
    dismissed_reason: Optional[Any] = Field(description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.")
    html_url: StrictStr = Field(description="The GitHub URL of the alert resource.")
    most_recent_instance: Optional[AlertInstance] = None
    number: StrictInt = Field(description="The code scanning alert number.")
    rule: WebhookCodeScanningAlertAppearedInBranchAlertRule
    state: StrictStr = Field(description="State of a code scanning alert.")
    tool: WebhookCodeScanningAlertAppearedInBranchAlertTool
    url: StrictStr
    __properties: ClassVar[List[str]] = ["created_at", "dismissed_at", "dismissed_by", "dismissed_reason", "html_url", "most_recent_instance", "number", "rule", "state", "tool", "url"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['open', 'fixed']):
            raise ValueError("must be one of enum values ('open', 'fixed')")
        return value

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
        """Create an instance of WebhookCodeScanningAlertReopenedByUserAlert from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of most_recent_instance
        if self.most_recent_instance:
            _dict['most_recent_instance'] = self.most_recent_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule
        if self.rule:
            _dict['rule'] = self.rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tool
        if self.tool:
            _dict['tool'] = self.tool.to_dict()
        # set to None if dismissed_at (nullable) is None
        # and model_fields_set contains the field
        if self.dismissed_at is None and "dismissed_at" in self.model_fields_set:
            _dict['dismissed_at'] = None

        # set to None if dismissed_by (nullable) is None
        # and model_fields_set contains the field
        if self.dismissed_by is None and "dismissed_by" in self.model_fields_set:
            _dict['dismissed_by'] = None

        # set to None if dismissed_reason (nullable) is None
        # and model_fields_set contains the field
        if self.dismissed_reason is None and "dismissed_reason" in self.model_fields_set:
            _dict['dismissed_reason'] = None

        # set to None if most_recent_instance (nullable) is None
        # and model_fields_set contains the field
        if self.most_recent_instance is None and "most_recent_instance" in self.model_fields_set:
            _dict['most_recent_instance'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookCodeScanningAlertReopenedByUserAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "dismissed_at": obj.get("dismissed_at"),
            "dismissed_by": obj.get("dismissed_by"),
            "dismissed_reason": obj.get("dismissed_reason"),
            "html_url": obj.get("html_url"),
            "most_recent_instance": AlertInstance.from_dict(obj["most_recent_instance"]) if obj.get("most_recent_instance") is not None else None,
            "number": obj.get("number"),
            "rule": WebhookCodeScanningAlertAppearedInBranchAlertRule.from_dict(obj["rule"]) if obj.get("rule") is not None else None,
            "state": obj.get("state"),
            "tool": WebhookCodeScanningAlertAppearedInBranchAlertTool.from_dict(obj["tool"]) if obj.get("tool") is not None else None,
            "url": obj.get("url")
        })
        return _obj


