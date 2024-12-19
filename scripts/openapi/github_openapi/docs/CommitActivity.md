# CommitActivity

Commit Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[int]** |  | 
**total** | **int** |  | 
**week** | **int** |  | 

## Example

```python
from github_openapi.models.commit_activity import CommitActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CommitActivity from a JSON string
commit_activity_instance = CommitActivity.from_json(json)
# print the JSON string representation of the object
print(CommitActivity.to_json())

# convert the object into a dict
commit_activity_dict = commit_activity_instance.to_dict()
# create an instance of CommitActivity from a dict
commit_activity_from_dict = CommitActivity.from_dict(commit_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


