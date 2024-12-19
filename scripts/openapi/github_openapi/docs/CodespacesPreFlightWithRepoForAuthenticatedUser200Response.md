# CodespacesPreFlightWithRepoForAuthenticatedUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_owner** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**defaults** | [**CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults**](CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults.md) |  | [optional] 

## Example

```python
from github_openapi.models.codespaces_pre_flight_with_repo_for_authenticated_user200_response import CodespacesPreFlightWithRepoForAuthenticatedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesPreFlightWithRepoForAuthenticatedUser200Response from a JSON string
codespaces_pre_flight_with_repo_for_authenticated_user200_response_instance = CodespacesPreFlightWithRepoForAuthenticatedUser200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesPreFlightWithRepoForAuthenticatedUser200Response.to_json())

# convert the object into a dict
codespaces_pre_flight_with_repo_for_authenticated_user200_response_dict = codespaces_pre_flight_with_repo_for_authenticated_user200_response_instance.to_dict()
# create an instance of CodespacesPreFlightWithRepoForAuthenticatedUser200Response from a dict
codespaces_pre_flight_with_repo_for_authenticated_user200_response_from_dict = CodespacesPreFlightWithRepoForAuthenticatedUser200Response.from_dict(codespaces_pre_flight_with_repo_for_authenticated_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


