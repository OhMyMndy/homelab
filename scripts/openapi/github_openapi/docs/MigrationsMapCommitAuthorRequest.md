# MigrationsMapCommitAuthorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The new Git author email. | [optional] 
**name** | **str** | The new Git author name. | [optional] 

## Example

```python
from github_openapi.models.migrations_map_commit_author_request import MigrationsMapCommitAuthorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsMapCommitAuthorRequest from a JSON string
migrations_map_commit_author_request_instance = MigrationsMapCommitAuthorRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsMapCommitAuthorRequest.to_json())

# convert the object into a dict
migrations_map_commit_author_request_dict = migrations_map_commit_author_request_instance.to_dict()
# create an instance of MigrationsMapCommitAuthorRequest from a dict
migrations_map_commit_author_request_from_dict = MigrationsMapCommitAuthorRequest.from_dict(migrations_map_commit_author_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


