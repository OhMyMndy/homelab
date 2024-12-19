# CustomPropertyValue

Custom property name and associated value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property | 
**value** | [**CustomPropertyValueValue**](CustomPropertyValueValue.md) |  | 

## Example

```python
from github_openapi.models.custom_property_value import CustomPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPropertyValue from a JSON string
custom_property_value_instance = CustomPropertyValue.from_json(json)
# print the JSON string representation of the object
print(CustomPropertyValue.to_json())

# convert the object into a dict
custom_property_value_dict = custom_property_value_instance.to_dict()
# create an instance of CustomPropertyValue from a dict
custom_property_value_from_dict = CustomPropertyValue.from_dict(custom_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


