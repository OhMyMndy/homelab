# IssueEventRename

Issue Event Rename

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 

## Example

```python
from github_openapi.models.issue_event_rename import IssueEventRename

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventRename from a JSON string
issue_event_rename_instance = IssueEventRename.from_json(json)
# print the JSON string representation of the object
print(IssueEventRename.to_json())

# convert the object into a dict
issue_event_rename_dict = issue_event_rename_instance.to_dict()
# create an instance of IssueEventRename from a dict
issue_event_rename_from_dict = IssueEventRename.from_dict(issue_event_rename_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


