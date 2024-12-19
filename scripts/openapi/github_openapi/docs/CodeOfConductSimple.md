# CodeOfConductSimple

Code of Conduct Simple

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.code_of_conduct_simple import CodeOfConductSimple

# TODO update the JSON string below
json = "{}"
# create an instance of CodeOfConductSimple from a JSON string
code_of_conduct_simple_instance = CodeOfConductSimple.from_json(json)
# print the JSON string representation of the object
print(CodeOfConductSimple.to_json())

# convert the object into a dict
code_of_conduct_simple_dict = code_of_conduct_simple_instance.to_dict()
# create an instance of CodeOfConductSimple from a dict
code_of_conduct_simple_from_dict = CodeOfConductSimple.from_dict(code_of_conduct_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


