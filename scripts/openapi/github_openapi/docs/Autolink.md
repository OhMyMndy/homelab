# Autolink

An autolink reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**key_prefix** | **str** | The prefix of a key that is linkified. | 
**url_template** | **str** | A template for the target URL that is generated if a key was found. | 
**is_alphanumeric** | **bool** | Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters. | 

## Example

```python
from github_openapi.models.autolink import Autolink

# TODO update the JSON string below
json = "{}"
# create an instance of Autolink from a JSON string
autolink_instance = Autolink.from_json(json)
# print the JSON string representation of the object
print(Autolink.to_json())

# convert the object into a dict
autolink_dict = autolink_instance.to_dict()
# create an instance of Autolink from a dict
autolink_from_dict = Autolink.from_dict(autolink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


