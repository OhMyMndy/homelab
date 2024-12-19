# NullableOrganizationSimple

A GitHub organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**hooks_url** | **str** |  | 
**issues_url** | **str** |  | 
**members_url** | **str** |  | 
**public_members_url** | **str** |  | 
**avatar_url** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from github_openapi.models.nullable_organization_simple import NullableOrganizationSimple

# TODO update the JSON string below
json = "{}"
# create an instance of NullableOrganizationSimple from a JSON string
nullable_organization_simple_instance = NullableOrganizationSimple.from_json(json)
# print the JSON string representation of the object
print(NullableOrganizationSimple.to_json())

# convert the object into a dict
nullable_organization_simple_dict = nullable_organization_simple_instance.to_dict()
# create an instance of NullableOrganizationSimple from a dict
nullable_organization_simple_from_dict = NullableOrganizationSimple.from_dict(nullable_organization_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


