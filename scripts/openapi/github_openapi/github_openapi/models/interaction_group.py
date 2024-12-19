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


class InteractionGroup(str, Enum):
    """
    The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect.
    """

    """
    allowed enum values
    """
    EXISTING_USERS = 'existing_users'
    CONTRIBUTORS_ONLY = 'contributors_only'
    COLLABORATORS_ONLY = 'collaborators_only'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InteractionGroup from a JSON string"""
        return cls(json.loads(json_str))


