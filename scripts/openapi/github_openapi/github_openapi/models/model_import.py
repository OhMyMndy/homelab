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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.import_project_choices_inner import ImportProjectChoicesInner
from typing import Optional, Set
from typing_extensions import Self

class ModelImport(BaseModel):
    """
    A repository import from an external source.
    """ # noqa: E501
    vcs: Optional[StrictStr]
    use_lfs: Optional[StrictBool] = None
    vcs_url: StrictStr = Field(description="The URL of the originating repository.")
    svc_root: Optional[StrictStr] = None
    tfvc_project: Optional[StrictStr] = None
    status: StrictStr
    status_text: Optional[StrictStr] = None
    failed_step: Optional[StrictStr] = None
    error_message: Optional[StrictStr] = None
    import_percent: Optional[StrictInt] = None
    commit_count: Optional[StrictInt] = None
    push_percent: Optional[StrictInt] = None
    has_large_files: Optional[StrictBool] = None
    large_files_size: Optional[StrictInt] = None
    large_files_count: Optional[StrictInt] = None
    project_choices: Optional[List[ImportProjectChoicesInner]] = None
    message: Optional[StrictStr] = None
    authors_count: Optional[StrictInt] = None
    url: StrictStr
    html_url: StrictStr
    authors_url: StrictStr
    repository_url: StrictStr
    svn_root: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["vcs", "use_lfs", "vcs_url", "svc_root", "tfvc_project", "status", "status_text", "failed_step", "error_message", "import_percent", "commit_count", "push_percent", "has_large_files", "large_files_size", "large_files_count", "project_choices", "message", "authors_count", "url", "html_url", "authors_url", "repository_url", "svn_root"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['auth', 'error', 'none', 'detecting', 'choose', 'auth_failed', 'importing', 'mapping', 'waiting_to_push', 'pushing', 'complete', 'setup', 'unknown', 'detection_found_multiple', 'detection_found_nothing', 'detection_needs_auth']):
            raise ValueError("must be one of enum values ('auth', 'error', 'none', 'detecting', 'choose', 'auth_failed', 'importing', 'mapping', 'waiting_to_push', 'pushing', 'complete', 'setup', 'unknown', 'detection_found_multiple', 'detection_found_nothing', 'detection_needs_auth')")
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
        """Create an instance of ModelImport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in project_choices (list)
        _items = []
        if self.project_choices:
            for _item_project_choices in self.project_choices:
                if _item_project_choices:
                    _items.append(_item_project_choices.to_dict())
            _dict['project_choices'] = _items
        # set to None if vcs (nullable) is None
        # and model_fields_set contains the field
        if self.vcs is None and "vcs" in self.model_fields_set:
            _dict['vcs'] = None

        # set to None if status_text (nullable) is None
        # and model_fields_set contains the field
        if self.status_text is None and "status_text" in self.model_fields_set:
            _dict['status_text'] = None

        # set to None if failed_step (nullable) is None
        # and model_fields_set contains the field
        if self.failed_step is None and "failed_step" in self.model_fields_set:
            _dict['failed_step'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['error_message'] = None

        # set to None if import_percent (nullable) is None
        # and model_fields_set contains the field
        if self.import_percent is None and "import_percent" in self.model_fields_set:
            _dict['import_percent'] = None

        # set to None if commit_count (nullable) is None
        # and model_fields_set contains the field
        if self.commit_count is None and "commit_count" in self.model_fields_set:
            _dict['commit_count'] = None

        # set to None if push_percent (nullable) is None
        # and model_fields_set contains the field
        if self.push_percent is None and "push_percent" in self.model_fields_set:
            _dict['push_percent'] = None

        # set to None if authors_count (nullable) is None
        # and model_fields_set contains the field
        if self.authors_count is None and "authors_count" in self.model_fields_set:
            _dict['authors_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelImport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vcs": obj.get("vcs"),
            "use_lfs": obj.get("use_lfs"),
            "vcs_url": obj.get("vcs_url"),
            "svc_root": obj.get("svc_root"),
            "tfvc_project": obj.get("tfvc_project"),
            "status": obj.get("status"),
            "status_text": obj.get("status_text"),
            "failed_step": obj.get("failed_step"),
            "error_message": obj.get("error_message"),
            "import_percent": obj.get("import_percent"),
            "commit_count": obj.get("commit_count"),
            "push_percent": obj.get("push_percent"),
            "has_large_files": obj.get("has_large_files"),
            "large_files_size": obj.get("large_files_size"),
            "large_files_count": obj.get("large_files_count"),
            "project_choices": [ImportProjectChoicesInner.from_dict(_item) for _item in obj["project_choices"]] if obj.get("project_choices") is not None else None,
            "message": obj.get("message"),
            "authors_count": obj.get("authors_count"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "authors_url": obj.get("authors_url"),
            "repository_url": obj.get("repository_url"),
            "svn_root": obj.get("svn_root")
        })
        return _obj

