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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment import Deployment
from github_openapi.models.organization_simple_webhooks import OrganizationSimpleWebhooks
from github_openapi.models.pull_request import PullRequest
from github_openapi.models.repository_webhooks import RepositoryWebhooks
from github_openapi.models.simple_installation import SimpleInstallation
from github_openapi.models.simple_user import SimpleUser
from typing import Optional, Set
from typing_extensions import Self

class WebhookDeploymentProtectionRuleRequested(BaseModel):
    """
    WebhookDeploymentProtectionRuleRequested
    """ # noqa: E501
    action: Optional[StrictStr] = None
    environment: Optional[StrictStr] = Field(default=None, description="The name of the environment that has the deployment protection rule.")
    event: Optional[StrictStr] = Field(default=None, description="The event that triggered the deployment protection rule.")
    deployment_callback_url: Optional[StrictStr] = Field(default=None, description="The URL to review the deployment protection rule.")
    deployment: Optional[Deployment] = None
    pull_requests: Optional[List[PullRequest]] = None
    repository: Optional[RepositoryWebhooks] = None
    organization: Optional[OrganizationSimpleWebhooks] = None
    installation: Optional[SimpleInstallation] = None
    sender: Optional[SimpleUser] = None
    __properties: ClassVar[List[str]] = ["action", "environment", "event", "deployment_callback_url", "deployment", "pull_requests", "repository", "organization", "installation", "sender"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['requested']):
            raise ValueError("must be one of enum values ('requested')")
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
        """Create an instance of WebhookDeploymentProtectionRuleRequested from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deployment
        if self.deployment:
            _dict['deployment'] = self.deployment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pull_requests (list)
        _items = []
        if self.pull_requests:
            for _item_pull_requests in self.pull_requests:
                if _item_pull_requests:
                    _items.append(_item_pull_requests.to_dict())
            _dict['pull_requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of installation
        if self.installation:
            _dict['installation'] = self.installation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookDeploymentProtectionRuleRequested from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "environment": obj.get("environment"),
            "event": obj.get("event"),
            "deployment_callback_url": obj.get("deployment_callback_url"),
            "deployment": Deployment.from_dict(obj["deployment"]) if obj.get("deployment") is not None else None,
            "pull_requests": [PullRequest.from_dict(_item) for _item in obj["pull_requests"]] if obj.get("pull_requests") is not None else None,
            "repository": RepositoryWebhooks.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "organization": OrganizationSimpleWebhooks.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "installation": SimpleInstallation.from_dict(obj["installation"]) if obj.get("installation") is not None else None,
            "sender": SimpleUser.from_dict(obj["sender"]) if obj.get("sender") is not None else None
        })
        return _obj


