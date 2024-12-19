# SCIMSourceUserRequest

SCIMSourceUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **int** |  | 
**source** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.scim_source_user_request import SCIMSourceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSourceUserRequest from a JSON string
scim_source_user_request_instance = SCIMSourceUserRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMSourceUserRequest.to_json())

# convert the object into a dict
scim_source_user_request_dict = scim_source_user_request_instance.to_dict()
# create an instance of SCIMSourceUserRequest from a dict
scim_source_user_request_from_dict = SCIMSourceUserRequest.from_dict(scim_source_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


