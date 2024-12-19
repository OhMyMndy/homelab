# CodeOfConduct

Code Of Conduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**body** | **str** |  | [optional] 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.code_of_conduct import CodeOfConduct

# TODO update the JSON string below
json = "{}"
# create an instance of CodeOfConduct from a JSON string
code_of_conduct_instance = CodeOfConduct.from_json(json)
# print the JSON string representation of the object
print(CodeOfConduct.to_json())

# convert the object into a dict
code_of_conduct_dict = code_of_conduct_instance.to_dict()
# create an instance of CodeOfConduct from a dict
code_of_conduct_from_dict = CodeOfConduct.from_dict(code_of_conduct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


