# ReposSetStatusCheckContextsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contexts** | **List[str]** | The name of the status checks | 

## Example

```python
from github_openapi.models.repos_set_status_check_contexts_request import ReposSetStatusCheckContextsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetStatusCheckContextsRequest from a JSON string
repos_set_status_check_contexts_request_instance = ReposSetStatusCheckContextsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposSetStatusCheckContextsRequest.to_json())

# convert the object into a dict
repos_set_status_check_contexts_request_dict = repos_set_status_check_contexts_request_instance.to_dict()
# create an instance of ReposSetStatusCheckContextsRequest from a dict
repos_set_status_check_contexts_request_from_dict = ReposSetStatusCheckContextsRequest.from_dict(repos_set_status_check_contexts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


