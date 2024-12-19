# OrganizationRole

Organization roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the role. | 
**name** | **str** | The name of the role. | 
**description** | **str** | A short description about who this role is for or what permissions it grants. | [optional] 
**base_role** | **str** | The system role from which this role inherits permissions. | [optional] 
**source** | **str** | Source answers the question, \&quot;where did this role come from?\&quot; | [optional] 
**permissions** | **List[str]** | A list of permissions included in this role. | 
**organization** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**created_at** | **datetime** | The date and time the role was created. | 
**updated_at** | **datetime** | The date and time the role was last updated. | 

## Example

```python
from github_openapi.models.organization_role import OrganizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRole from a JSON string
organization_role_instance = OrganizationRole.from_json(json)
# print the JSON string representation of the object
print(OrganizationRole.to_json())

# convert the object into a dict
organization_role_dict = organization_role_instance.to_dict()
# create an instance of OrganizationRole from a dict
organization_role_from_dict = OrganizationRole.from_dict(organization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


