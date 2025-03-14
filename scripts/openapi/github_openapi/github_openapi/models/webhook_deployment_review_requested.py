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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment_workflow_run3 import DeploymentWorkflowRun3
from github_openapi.models.enterprise_webhooks import EnterpriseWebhooks
from github_openapi.models.organization_simple_webhooks import OrganizationSimpleWebhooks
from github_openapi.models.repository_webhooks import RepositoryWebhooks
from github_openapi.models.simple_installation import SimpleInstallation
from github_openapi.models.simple_user import SimpleUser
from github_openapi.models.webhook_deployment_review_requested_reviewers_inner import WebhookDeploymentReviewRequestedReviewersInner
from github_openapi.models.webhook_deployment_review_requested_workflow_job_run import WebhookDeploymentReviewRequestedWorkflowJobRun
from github_openapi.models.webhooks_user import WebhooksUser
from typing import Optional, Set
from typing_extensions import Self

class WebhookDeploymentReviewRequested(BaseModel):
    """
    WebhookDeploymentReviewRequested
    """ # noqa: E501
    action: StrictStr
    enterprise: Optional[EnterpriseWebhooks] = None
    environment: StrictStr
    installation: Optional[SimpleInstallation] = None
    organization: OrganizationSimpleWebhooks
    repository: RepositoryWebhooks
    requestor: Optional[WebhooksUser]
    reviewers: List[WebhookDeploymentReviewRequestedReviewersInner]
    sender: SimpleUser
    since: StrictStr
    workflow_job_run: WebhookDeploymentReviewRequestedWorkflowJobRun
    workflow_run: Optional[DeploymentWorkflowRun3]
    __properties: ClassVar[List[str]] = ["action", "enterprise", "environment", "installation", "organization", "repository", "requestor", "reviewers", "sender", "since", "workflow_job_run", "workflow_run"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of WebhookDeploymentReviewRequested from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requestor
        if self.requestor:
            _dict['requestor'] = self.requestor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item_reviewers in self.reviewers:
                if _item_reviewers:
                    _items.append(_item_reviewers.to_dict())
            _dict['reviewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow_job_run
        if self.workflow_job_run:
            _dict['workflow_job_run'] = self.workflow_job_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow_run
        if self.workflow_run:
            _dict['workflow_run'] = self.workflow_run.to_dict()
        # set to None if requestor (nullable) is None
        # and model_fields_set contains the field
        if self.requestor is None and "requestor" in self.model_fields_set:
            _dict['requestor'] = None

        # set to None if workflow_run (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_run is None and "workflow_run" in self.model_fields_set:
            _dict['workflow_run'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookDeploymentReviewRequested from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "enterprise": EnterpriseWebhooks.from_dict(obj["enterprise"]) if obj.get("enterprise") is not None else None,
            "environment": obj.get("environment"),
            "installation": SimpleInstallation.from_dict(obj["installation"]) if obj.get("installation") is not None else None,
            "organization": OrganizationSimpleWebhooks.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "repository": RepositoryWebhooks.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "requestor": WebhooksUser.from_dict(obj["requestor"]) if obj.get("requestor") is not None else None,
            "reviewers": [WebhookDeploymentReviewRequestedReviewersInner.from_dict(_item) for _item in obj["reviewers"]] if obj.get("reviewers") is not None else None,
            "sender": SimpleUser.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "since": obj.get("since"),
            "workflow_job_run": WebhookDeploymentReviewRequestedWorkflowJobRun.from_dict(obj["workflow_job_run"]) if obj.get("workflow_job_run") is not None else None,
            "workflow_run": DeploymentWorkflowRun3.from_dict(obj["workflow_run"]) if obj.get("workflow_run") is not None else None
        })
        return _obj


