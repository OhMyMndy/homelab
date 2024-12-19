# AppsScopeTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token used to authenticate to the GitHub API. | 
**target** | **str** | The name of the user or organization to scope the user access token to. **Required** unless &#x60;target_id&#x60; is specified. | [optional] 
**target_id** | **int** | The ID of the user or organization to scope the user access token to. **Required** unless &#x60;target&#x60; is specified. | [optional] 
**repositories** | **List[str]** | The list of repository names to scope the user access token to. &#x60;repositories&#x60; may not be specified if &#x60;repository_ids&#x60; is specified. | [optional] 
**repository_ids** | **List[int]** | The list of repository IDs to scope the user access token to. &#x60;repository_ids&#x60; may not be specified if &#x60;repositories&#x60; is specified. | [optional] 
**permissions** | [**AppPermissions**](AppPermissions.md) |  | [optional] 

## Example

```python
from github_openapi.models.apps_scope_token_request import AppsScopeTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppsScopeTokenRequest from a JSON string
apps_scope_token_request_instance = AppsScopeTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AppsScopeTokenRequest.to_json())

# convert the object into a dict
apps_scope_token_request_dict = apps_scope_token_request_instance.to_dict()
# create an instance of AppsScopeTokenRequest from a dict
apps_scope_token_request_from_dict = AppsScopeTokenRequest.from_dict(apps_scope_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


