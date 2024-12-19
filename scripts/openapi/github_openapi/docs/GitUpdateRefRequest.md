# GitUpdateRefRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | The SHA1 value to set this reference to | 
**force** | **bool** | Indicates whether to force the update or to make sure the update is a fast-forward update. Leaving this out or setting it to &#x60;false&#x60; will make sure you&#39;re not overwriting work. | [optional] [default to False]

## Example

```python
from github_openapi.models.git_update_ref_request import GitUpdateRefRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitUpdateRefRequest from a JSON string
git_update_ref_request_instance = GitUpdateRefRequest.from_json(json)
# print the JSON string representation of the object
print(GitUpdateRefRequest.to_json())

# convert the object into a dict
git_update_ref_request_dict = git_update_ref_request_instance.to_dict()
# create an instance of GitUpdateRefRequest from a dict
git_update_ref_request_from_dict = GitUpdateRefRequest.from_dict(git_update_ref_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


