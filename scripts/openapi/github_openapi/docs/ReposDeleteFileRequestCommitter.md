# ReposDeleteFileRequestCommitter

object containing information about the committer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author (or committer) of the commit | [optional] 
**email** | **str** | The email of the author (or committer) of the commit | [optional] 

## Example

```python
from github_openapi.models.repos_delete_file_request_committer import ReposDeleteFileRequestCommitter

# TODO update the JSON string below
json = "{}"
# create an instance of ReposDeleteFileRequestCommitter from a JSON string
repos_delete_file_request_committer_instance = ReposDeleteFileRequestCommitter.from_json(json)
# print the JSON string representation of the object
print(ReposDeleteFileRequestCommitter.to_json())

# convert the object into a dict
repos_delete_file_request_committer_dict = repos_delete_file_request_committer_instance.to_dict()
# create an instance of ReposDeleteFileRequestCommitter from a dict
repos_delete_file_request_committer_from_dict = ReposDeleteFileRequestCommitter.from_dict(repos_delete_file_request_committer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


