# RenamedIssueEventRename


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 

## Example

```python
from github_openapi.models.renamed_issue_event_rename import RenamedIssueEventRename

# TODO update the JSON string below
json = "{}"
# create an instance of RenamedIssueEventRename from a JSON string
renamed_issue_event_rename_instance = RenamedIssueEventRename.from_json(json)
# print the JSON string representation of the object
print(RenamedIssueEventRename.to_json())

# convert the object into a dict
renamed_issue_event_rename_dict = renamed_issue_event_rename_instance.to_dict()
# create an instance of RenamedIssueEventRename from a dict
renamed_issue_event_rename_from_dict = RenamedIssueEventRename.from_dict(renamed_issue_event_rename_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


