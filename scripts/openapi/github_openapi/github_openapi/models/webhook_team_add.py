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
from github_openapi.models.enterprise_webhooks import EnterpriseWebhooks
from github_openapi.models.organization_simple_webhooks import OrganizationSimpleWebhooks
from github_openapi.models.repository_webhooks import RepositoryWebhooks
from github_openapi.models.simple_installation import SimpleInstallation
from github_openapi.models.simple_user import SimpleUser
from github_openapi.models.webhooks_team1 import WebhooksTeam1
from typing import Optional, Set
from typing_extensions import Self

class WebhookTeamAdd(BaseModel):
    """
    WebhookTeamAdd
    """ # noqa: E501
    enterprise: Optional[EnterpriseWebhooks] = None
    installation: Optional[SimpleInstallation] = None
    organization: Optional[OrganizationSimpleWebhooks] = None
    repository: RepositoryWebhooks
    sender: SimpleUser
    team: WebhooksTeam1
    __properties: ClassVar[List[str]] = ["enterprise", "installation", "organization", "repository", "sender", "team"]

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
        """Create an instance of WebhookTeamAdd from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of enterprise
        if self.enterprise:
            _dict['enterprise'] = self.enterprise.to_dict()
        # override the default output from pydantic by calling `to_dict()` of installation
        if self.installation:
            _dict['installation'] = self.installation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookTeamAdd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enterprise": EnterpriseWebhooks.from_dict(obj["enterprise"]) if obj.get("enterprise") is not None else None,
            "installation": SimpleInstallation.from_dict(obj["installation"]) if obj.get("installation") is not None else None,
            "organization": OrganizationSimpleWebhooks.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "repository": RepositoryWebhooks.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "sender": SimpleUser.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "team": WebhooksTeam1.from_dict(obj["team"]) if obj.get("team") is not None else None
        })
        return _obj


