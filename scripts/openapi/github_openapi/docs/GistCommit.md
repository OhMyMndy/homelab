# GistCommit

Gist Commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**version** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**change_status** | [**GistHistoryChangeStatus**](GistHistoryChangeStatus.md) |  | 
**committed_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.gist_commit import GistCommit

# TODO update the JSON string below
json = "{}"
# create an instance of GistCommit from a JSON string
gist_commit_instance = GistCommit.from_json(json)
# print the JSON string representation of the object
print(GistCommit.to_json())

# convert the object into a dict
gist_commit_dict = gist_commit_instance.to_dict()
# create an instance of GistCommit from a dict
gist_commit_from_dict = GistCommit.from_dict(gist_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


