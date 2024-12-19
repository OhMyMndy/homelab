# Permission

Global permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**codename** | **str** |  | 
**model** | **str** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**app_label_verbose** | **str** | Human-readable app label | [readonly] 
**model_verbose** | **str** | Human-readable model name | [readonly] 

## Example

```python
from authentik_openapi.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_from_dict = Permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


