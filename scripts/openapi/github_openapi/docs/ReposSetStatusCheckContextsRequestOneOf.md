# ReposSetStatusCheckContextsRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contexts** | **List[str]** | The name of the status checks | 

## Example

```python
from github_openapi.models.repos_set_status_check_contexts_request_one_of import ReposSetStatusCheckContextsRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetStatusCheckContextsRequestOneOf from a JSON string
repos_set_status_check_contexts_request_one_of_instance = ReposSetStatusCheckContextsRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ReposSetStatusCheckContextsRequestOneOf.to_json())

# convert the object into a dict
repos_set_status_check_contexts_request_one_of_dict = repos_set_status_check_contexts_request_one_of_instance.to_dict()
# create an instance of ReposSetStatusCheckContextsRequestOneOf from a dict
repos_set_status_check_contexts_request_one_of_from_dict = ReposSetStatusCheckContextsRequestOneOf.from_dict(repos_set_status_check_contexts_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


