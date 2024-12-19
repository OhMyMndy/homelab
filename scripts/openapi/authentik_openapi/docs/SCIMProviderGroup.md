# SCIMProviderGroup

SCIMProviderGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**scim_id** | **str** |  | 
**group** | **str** |  | 
**group_obj** | [**UserGroup**](UserGroup.md) |  | [readonly] 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.scim_provider_group import SCIMProviderGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProviderGroup from a JSON string
scim_provider_group_instance = SCIMProviderGroup.from_json(json)
# print the JSON string representation of the object
print(SCIMProviderGroup.to_json())

# convert the object into a dict
scim_provider_group_dict = scim_provider_group_instance.to_dict()
# create an instance of SCIMProviderGroup from a dict
scim_provider_group_from_dict = SCIMProviderGroup.from_dict(scim_provider_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


