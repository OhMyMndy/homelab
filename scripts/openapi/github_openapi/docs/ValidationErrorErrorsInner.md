# ValidationErrorErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | [optional] 
**var_field** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **str** |  | 
**index** | **int** |  | [optional] 
**value** | [**ValidationErrorErrorsInnerValue**](ValidationErrorErrorsInnerValue.md) |  | [optional] 

## Example

```python
from github_openapi.models.validation_error_errors_inner import ValidationErrorErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorErrorsInner from a JSON string
validation_error_errors_inner_instance = ValidationErrorErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorErrorsInner.to_json())

# convert the object into a dict
validation_error_errors_inner_dict = validation_error_errors_inner_instance.to_dict()
# create an instance of ValidationErrorErrorsInner from a dict
validation_error_errors_inner_from_dict = ValidationErrorErrorsInner.from_dict(validation_error_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


