# SCIMProviderGroupRequest

SCIMProviderGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scim_id** | **str** |  | 
**group** | **str** |  | 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.scim_provider_group_request import SCIMProviderGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProviderGroupRequest from a JSON string
scim_provider_group_request_instance = SCIMProviderGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMProviderGroupRequest.to_json())

# convert the object into a dict
scim_provider_group_request_dict = scim_provider_group_request_instance.to_dict()
# create an instance of SCIMProviderGroupRequest from a dict
scim_provider_group_request_from_dict = SCIMProviderGroupRequest.from_dict(scim_provider_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


