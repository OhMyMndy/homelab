# CustomPropertySetPayload

Custom property set payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_type** | **str** | The type of the value for the property | 
**required** | **bool** | Whether the property is required. | [optional] 
**default_value** | [**CustomPropertyDefaultValue**](CustomPropertyDefaultValue.md) |  | [optional] 
**description** | **str** | Short description of the property | [optional] 
**allowed_values** | **List[str]** | An ordered list of the allowed values of the property. The property can have up to 200 allowed values. | [optional] 

## Example

```python
from github_openapi.models.custom_property_set_payload import CustomPropertySetPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPropertySetPayload from a JSON string
custom_property_set_payload_instance = CustomPropertySetPayload.from_json(json)
# print the JSON string representation of the object
print(CustomPropertySetPayload.to_json())

# convert the object into a dict
custom_property_set_payload_dict = custom_property_set_payload_instance.to_dict()
# create an instance of CustomPropertySetPayload from a dict
custom_property_set_payload_from_dict = CustomPropertySetPayload.from_dict(custom_property_set_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


