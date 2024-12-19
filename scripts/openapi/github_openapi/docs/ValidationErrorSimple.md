# ValidationErrorSimple

Validation Error Simple

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**documentation_url** | **str** |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.validation_error_simple import ValidationErrorSimple

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorSimple from a JSON string
validation_error_simple_instance = ValidationErrorSimple.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorSimple.to_json())

# convert the object into a dict
validation_error_simple_dict = validation_error_simple_instance.to_dict()
# create an instance of ValidationErrorSimple from a dict
validation_error_simple_from_dict = ValidationErrorSimple.from_dict(validation_error_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


