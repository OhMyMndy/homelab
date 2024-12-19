# UsedBy

A list of all objects referencing the queried object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | 
**model_name** | **str** |  | 
**pk** | **str** |  | 
**name** | **str** |  | 
**action** | [**UsedByActionEnum**](UsedByActionEnum.md) |  | 

## Example

```python
from authentik_openapi.models.used_by import UsedBy

# TODO update the JSON string below
json = "{}"
# create an instance of UsedBy from a JSON string
used_by_instance = UsedBy.from_json(json)
# print the JSON string representation of the object
print(UsedBy.to_json())

# convert the object into a dict
used_by_dict = used_by_instance.to_dict()
# create an instance of UsedBy from a dict
used_by_from_dict = UsedBy.from_dict(used_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


