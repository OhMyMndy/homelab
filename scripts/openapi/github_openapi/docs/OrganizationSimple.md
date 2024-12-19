# OrganizationSimple

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
from github_openapi.models.organization_simple import OrganizationSimple

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSimple from a JSON string
organization_simple_instance = OrganizationSimple.from_json(json)
# print the JSON string representation of the object
print(OrganizationSimple.to_json())

# convert the object into a dict
organization_simple_dict = organization_simple_instance.to_dict()
# create an instance of OrganizationSimple from a dict
organization_simple_from_dict = OrganizationSimple.from_dict(organization_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


