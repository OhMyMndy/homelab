# BasicError

Basic Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.basic_error import BasicError

# TODO update the JSON string below
json = "{}"
# create an instance of BasicError from a JSON string
basic_error_instance = BasicError.from_json(json)
# print the JSON string representation of the object
print(BasicError.to_json())

# convert the object into a dict
basic_error_dict = basic_error_instance.to_dict()
# create an instance of BasicError from a dict
basic_error_from_dict = BasicError.from_dict(basic_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


