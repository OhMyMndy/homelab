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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment_branch_policy_settings import DeploymentBranchPolicySettings
from github_openapi.models.repos_create_or_update_environment_request_reviewers_inner import ReposCreateOrUpdateEnvironmentRequestReviewersInner
from typing import Optional, Set
from typing_extensions import Self

class ReposCreateOrUpdateEnvironmentRequest(BaseModel):
    """
    ReposCreateOrUpdateEnvironmentRequest
    """ # noqa: E501
    wait_timer: Optional[StrictInt] = Field(default=None, description="The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days).")
    prevent_self_review: Optional[StrictBool] = Field(default=None, description="Whether or not a user who created the job is prevented from approving their own job.")
    reviewers: Optional[List[ReposCreateOrUpdateEnvironmentRequestReviewersInner]] = Field(default=None, description="The people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.")
    deployment_branch_policy: Optional[DeploymentBranchPolicySettings] = None
    __properties: ClassVar[List[str]] = ["wait_timer", "prevent_self_review", "reviewers", "deployment_branch_policy"]

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
        """Create an instance of ReposCreateOrUpdateEnvironmentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item_reviewers in self.reviewers:
                if _item_reviewers:
                    _items.append(_item_reviewers.to_dict())
            _dict['reviewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of deployment_branch_policy
        if self.deployment_branch_policy:
            _dict['deployment_branch_policy'] = self.deployment_branch_policy.to_dict()
        # set to None if reviewers (nullable) is None
        # and model_fields_set contains the field
        if self.reviewers is None and "reviewers" in self.model_fields_set:
            _dict['reviewers'] = None

        # set to None if deployment_branch_policy (nullable) is None
        # and model_fields_set contains the field
        if self.deployment_branch_policy is None and "deployment_branch_policy" in self.model_fields_set:
            _dict['deployment_branch_policy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReposCreateOrUpdateEnvironmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "wait_timer": obj.get("wait_timer"),
            "prevent_self_review": obj.get("prevent_self_review"),
            "reviewers": [ReposCreateOrUpdateEnvironmentRequestReviewersInner.from_dict(_item) for _item in obj["reviewers"]] if obj.get("reviewers") is not None else None,
            "deployment_branch_policy": DeploymentBranchPolicySettings.from_dict(obj["deployment_branch_policy"]) if obj.get("deployment_branch_policy") is not None else None
        })
        return _obj

