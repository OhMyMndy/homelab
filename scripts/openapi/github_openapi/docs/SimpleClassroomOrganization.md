# SimpleClassroomOrganization

A GitHub organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**login** | **str** |  | 
**node_id** | **str** |  | 
**html_url** | **str** |  | 
**name** | **str** |  | 
**avatar_url** | **str** |  | 

## Example

```python
from github_openapi.models.simple_classroom_organization import SimpleClassroomOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleClassroomOrganization from a JSON string
simple_classroom_organization_instance = SimpleClassroomOrganization.from_json(json)
# print the JSON string representation of the object
print(SimpleClassroomOrganization.to_json())

# convert the object into a dict
simple_classroom_organization_dict = simple_classroom_organization_instance.to_dict()
# create an instance of SimpleClassroomOrganization from a dict
simple_classroom_organization_from_dict = SimpleClassroomOrganization.from_dict(simple_classroom_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


