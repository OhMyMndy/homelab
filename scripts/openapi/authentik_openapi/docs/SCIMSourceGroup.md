# SCIMSourceGroup

SCIMSourceGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group** | **str** |  | 
**group_obj** | [**UserGroup**](UserGroup.md) |  | [readonly] 
**source** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.scim_source_group import SCIMSourceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSourceGroup from a JSON string
scim_source_group_instance = SCIMSourceGroup.from_json(json)
# print the JSON string representation of the object
print(SCIMSourceGroup.to_json())

# convert the object into a dict
scim_source_group_dict = scim_source_group_instance.to_dict()
# create an instance of SCIMSourceGroup from a dict
scim_source_group_from_dict = SCIMSourceGroup.from_dict(scim_source_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


