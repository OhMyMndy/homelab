# AppsCreateInstallationAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repositories** | **List[str]** | List of repository names that the token should have access to | [optional] 
**repository_ids** | **List[int]** | List of repository IDs that the token should have access to | [optional] 
**permissions** | [**AppPermissions**](AppPermissions.md) |  | [optional] 

## Example

```python
from github_openapi.models.apps_create_installation_access_token_request import AppsCreateInstallationAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppsCreateInstallationAccessTokenRequest from a JSON string
apps_create_installation_access_token_request_instance = AppsCreateInstallationAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AppsCreateInstallationAccessTokenRequest.to_json())

# convert the object into a dict
apps_create_installation_access_token_request_dict = apps_create_installation_access_token_request_instance.to_dict()
# create an instance of AppsCreateInstallationAccessTokenRequest from a dict
apps_create_installation_access_token_request_from_dict = AppsCreateInstallationAccessTokenRequest.from_dict(apps_create_installation_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


