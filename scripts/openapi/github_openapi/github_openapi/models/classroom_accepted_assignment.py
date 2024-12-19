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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from github_openapi.models.simple_classroom_assignment import SimpleClassroomAssignment
from github_openapi.models.simple_classroom_repository import SimpleClassroomRepository
from github_openapi.models.simple_classroom_user import SimpleClassroomUser
from typing import Optional, Set
from typing_extensions import Self

class ClassroomAcceptedAssignment(BaseModel):
    """
    A GitHub Classroom accepted assignment
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier of the repository.")
    submitted: StrictBool = Field(description="Whether an accepted assignment has been submitted.")
    passing: StrictBool = Field(description="Whether a submission passed.")
    commit_count: StrictInt = Field(description="Count of student commits.")
    grade: StrictStr = Field(description="Most recent grade.")
    students: List[SimpleClassroomUser]
    repository: SimpleClassroomRepository
    assignment: SimpleClassroomAssignment
    __properties: ClassVar[List[str]] = ["id", "submitted", "passing", "commit_count", "grade", "students", "repository", "assignment"]

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
        """Create an instance of ClassroomAcceptedAssignment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in students (list)
        _items = []
        if self.students:
            for _item_students in self.students:
                if _item_students:
                    _items.append(_item_students.to_dict())
            _dict['students'] = _items
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assignment
        if self.assignment:
            _dict['assignment'] = self.assignment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClassroomAcceptedAssignment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "submitted": obj.get("submitted"),
            "passing": obj.get("passing"),
            "commit_count": obj.get("commit_count"),
            "grade": obj.get("grade"),
            "students": [SimpleClassroomUser.from_dict(_item) for _item in obj["students"]] if obj.get("students") is not None else None,
            "repository": SimpleClassroomRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "assignment": SimpleClassroomAssignment.from_dict(obj["assignment"]) if obj.get("assignment") is not None else None
        })
        return _obj


