# ActionsListOrgSecrets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**secrets** | [**List[OrganizationActionsSecret]**](OrganizationActionsSecret.md) |  | 

## Example

```python
from github_openapi.models.actions_list_org_secrets200_response import ActionsListOrgSecrets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListOrgSecrets200Response from a JSON string
actions_list_org_secrets200_response_instance = ActionsListOrgSecrets200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListOrgSecrets200Response.to_json())

# convert the object into a dict
actions_list_org_secrets200_response_dict = actions_list_org_secrets200_response_instance.to_dict()
# create an instance of ActionsListOrgSecrets200Response from a dict
actions_list_org_secrets200_response_from_dict = ActionsListOrgSecrets200Response.from_dict(actions_list_org_secrets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


