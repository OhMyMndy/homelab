# OrgsListOrgRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of organization roles available to the organization. | [optional] 
**roles** | [**List[OrganizationRole]**](OrganizationRole.md) | The list of organization roles available to the organization. | [optional] 

## Example

```python
from github_openapi.models.orgs_list_org_roles200_response import OrgsListOrgRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsListOrgRoles200Response from a JSON string
orgs_list_org_roles200_response_instance = OrgsListOrgRoles200Response.from_json(json)
# print the JSON string representation of the object
print(OrgsListOrgRoles200Response.to_json())

# convert the object into a dict
orgs_list_org_roles200_response_dict = orgs_list_org_roles200_response_instance.to_dict()
# create an instance of OrgsListOrgRoles200Response from a dict
orgs_list_org_roles200_response_from_dict = OrgsListOrgRoles200Response.from_dict(orgs_list_org_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


