# SCIMSourceGroupRequest

SCIMSourceGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group** | **str** |  | 
**source** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.scim_source_group_request import SCIMSourceGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSourceGroupRequest from a JSON string
scim_source_group_request_instance = SCIMSourceGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMSourceGroupRequest.to_json())

# convert the object into a dict
scim_source_group_request_dict = scim_source_group_request_instance.to_dict()
# create an instance of SCIMSourceGroupRequest from a dict
scim_source_group_request_from_dict = SCIMSourceGroupRequest.from_dict(scim_source_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


