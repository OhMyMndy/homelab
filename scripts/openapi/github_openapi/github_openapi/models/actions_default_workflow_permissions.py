# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ActionsDefaultWorkflowPermissions(str, Enum):
    """
    The default workflow permissions granted to the GITHUB_TOKEN when running workflows.
    """

    """
    allowed enum values
    """
    READ = 'read'
    WRITE = 'write'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionsDefaultWorkflowPermissions from a JSON string"""
        return cls(json.loads(json_str))


