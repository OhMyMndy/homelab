# CustomProperty

Custom property defined on an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property | 
**url** | **str** | The URL that can be used to fetch, update, or delete info about this property via the API. | [optional] 
**source_type** | **str** | The source type of the property | [optional] 
**value_type** | **str** | The type of the value for the property | 
**required** | **bool** | Whether the property is required. | [optional] 
**default_value** | [**CustomPropertyDefaultValue**](CustomPropertyDefaultValue.md) |  | [optional] 
**description** | **str** | Short description of the property | [optional] 
**allowed_values** | **List[str]** | An ordered list of the allowed values of the property. The property can have up to 200 allowed values. | [optional] 
**values_editable_by** | **str** | Who can edit the values of the property | [optional] 

## Example

```python
from github_openapi.models.custom_property import CustomProperty

# TODO update the JSON string below
json = "{}"
# create an instance of CustomProperty from a JSON string
custom_property_instance = CustomProperty.from_json(json)
# print the JSON string representation of the object
print(CustomProperty.to_json())

# convert the object into a dict
custom_property_dict = custom_property_instance.to_dict()
# create an instance of CustomProperty from a dict
custom_property_from_dict = CustomProperty.from_dict(custom_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


