# TypeCreate

Types of an object that can be created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**component** | **str** |  | 
**model_name** | **str** |  | 
**icon_url** | **str** |  | [optional] 
**requires_enterprise** | **bool** |  | [optional] [default to False]

## Example

```python
from authentik_openapi.models.type_create import TypeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TypeCreate from a JSON string
type_create_instance = TypeCreate.from_json(json)
# print the JSON string representation of the object
print(TypeCreate.to_json())

# convert the object into a dict
type_create_dict = type_create_instance.to_dict()
# create an instance of TypeCreate from a dict
type_create_from_dict = TypeCreate.from_dict(type_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


