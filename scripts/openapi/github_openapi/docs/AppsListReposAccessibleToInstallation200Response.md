# AppsListReposAccessibleToInstallation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**repositories** | [**List[Repository]**](Repository.md) |  | 
**repository_selection** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.apps_list_repos_accessible_to_installation200_response import AppsListReposAccessibleToInstallation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AppsListReposAccessibleToInstallation200Response from a JSON string
apps_list_repos_accessible_to_installation200_response_instance = AppsListReposAccessibleToInstallation200Response.from_json(json)
# print the JSON string representation of the object
print(AppsListReposAccessibleToInstallation200Response.to_json())

# convert the object into a dict
apps_list_repos_accessible_to_installation200_response_dict = apps_list_repos_accessible_to_installation200_response_instance.to_dict()
# create an instance of AppsListReposAccessibleToInstallation200Response from a dict
apps_list_repos_accessible_to_installation200_response_from_dict = AppsListReposAccessibleToInstallation200Response.from_dict(apps_list_repos_accessible_to_installation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


