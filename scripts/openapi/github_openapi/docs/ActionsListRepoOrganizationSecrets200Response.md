# ActionsListRepoOrganizationSecrets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**secrets** | [**List[ActionsSecret]**](ActionsSecret.md) |  | 

## Example

```python
from github_openapi.models.actions_list_repo_organization_secrets200_response import ActionsListRepoOrganizationSecrets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListRepoOrganizationSecrets200Response from a JSON string
actions_list_repo_organization_secrets200_response_instance = ActionsListRepoOrganizationSecrets200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListRepoOrganizationSecrets200Response.to_json())

# convert the object into a dict
actions_list_repo_organization_secrets200_response_dict = actions_list_repo_organization_secrets200_response_instance.to_dict()
# create an instance of ActionsListRepoOrganizationSecrets200Response from a dict
actions_list_repo_organization_secrets200_response_from_dict = ActionsListRepoOrganizationSecrets200Response.from_dict(actions_list_repo_organization_secrets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


