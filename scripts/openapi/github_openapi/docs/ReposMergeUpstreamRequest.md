# ReposMergeUpstreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The name of the branch which should be updated to match upstream. | 

## Example

```python
from github_openapi.models.repos_merge_upstream_request import ReposMergeUpstreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposMergeUpstreamRequest from a JSON string
repos_merge_upstream_request_instance = ReposMergeUpstreamRequest.from_json(json)
# print the JSON string representation of the object
print(ReposMergeUpstreamRequest.to_json())

# convert the object into a dict
repos_merge_upstream_request_dict = repos_merge_upstream_request_instance.to_dict()
# create an instance of ReposMergeUpstreamRequest from a dict
repos_merge_upstream_request_from_dict = ReposMergeUpstreamRequest.from_dict(repos_merge_upstream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


