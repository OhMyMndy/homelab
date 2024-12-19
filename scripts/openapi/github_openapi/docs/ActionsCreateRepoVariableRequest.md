# ActionsCreateRepoVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable. | 
**value** | **str** | The value of the variable. | 

## Example

```python
from github_openapi.models.actions_create_repo_variable_request import ActionsCreateRepoVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCreateRepoVariableRequest from a JSON string
actions_create_repo_variable_request_instance = ActionsCreateRepoVariableRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsCreateRepoVariableRequest.to_json())

# convert the object into a dict
actions_create_repo_variable_request_dict = actions_create_repo_variable_request_instance.to_dict()
# create an instance of ActionsCreateRepoVariableRequest from a dict
actions_create_repo_variable_request_from_dict = ActionsCreateRepoVariableRequest.from_dict(actions_create_repo_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


