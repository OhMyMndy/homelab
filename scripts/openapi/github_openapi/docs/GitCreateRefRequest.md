# GitCreateRefRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | The name of the fully qualified reference (ie: &#x60;refs/heads/master&#x60;). If it doesn&#39;t start with &#39;refs&#39; and have at least two slashes, it will be rejected. | 
**sha** | **str** | The SHA1 value for this reference. | 

## Example

```python
from github_openapi.models.git_create_ref_request import GitCreateRefRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateRefRequest from a JSON string
git_create_ref_request_instance = GitCreateRefRequest.from_json(json)
# print the JSON string representation of the object
print(GitCreateRefRequest.to_json())

# convert the object into a dict
git_create_ref_request_dict = git_create_ref_request_instance.to_dict()
# create an instance of GitCreateRefRequest from a dict
git_create_ref_request_from_dict = GitCreateRefRequest.from_dict(git_create_ref_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


