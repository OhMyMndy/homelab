# RoleRequest

Role serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from authentik_openapi.models.role_request import RoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleRequest from a JSON string
role_request_instance = RoleRequest.from_json(json)
# print the JSON string representation of the object
print(RoleRequest.to_json())

# convert the object into a dict
role_request_dict = role_request_instance.to_dict()
# create an instance of RoleRequest from a dict
role_request_from_dict = RoleRequest.from_dict(role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


