# AppsListInstallationReposForAuthenticatedUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**repository_selection** | **str** |  | [optional] 
**repositories** | [**List[Repository]**](Repository.md) |  | 

## Example

```python
from github_openapi.models.apps_list_installation_repos_for_authenticated_user200_response import AppsListInstallationReposForAuthenticatedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AppsListInstallationReposForAuthenticatedUser200Response from a JSON string
apps_list_installation_repos_for_authenticated_user200_response_instance = AppsListInstallationReposForAuthenticatedUser200Response.from_json(json)
# print the JSON string representation of the object
print(AppsListInstallationReposForAuthenticatedUser200Response.to_json())

# convert the object into a dict
apps_list_installation_repos_for_authenticated_user200_response_dict = apps_list_installation_repos_for_authenticated_user200_response_instance.to_dict()
# create an instance of AppsListInstallationReposForAuthenticatedUser200Response from a dict
apps_list_installation_repos_for_authenticated_user200_response_from_dict = AppsListInstallationReposForAuthenticatedUser200Response.from_dict(apps_list_installation_repos_for_authenticated_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


