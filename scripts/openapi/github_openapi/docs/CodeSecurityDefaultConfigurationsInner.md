# CodeSecurityDefaultConfigurationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_for_new_repos** | **str** | The visibility of newly created repositories for which the code security configuration will be applied to by default | [optional] 
**configuration** | [**CodeSecurityConfiguration**](CodeSecurityConfiguration.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_security_default_configurations_inner import CodeSecurityDefaultConfigurationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityDefaultConfigurationsInner from a JSON string
code_security_default_configurations_inner_instance = CodeSecurityDefaultConfigurationsInner.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityDefaultConfigurationsInner.to_json())

# convert the object into a dict
code_security_default_configurations_inner_dict = code_security_default_configurations_inner_instance.to_dict()
# create an instance of CodeSecurityDefaultConfigurationsInner from a dict
code_security_default_configurations_inner_from_dict = CodeSecurityDefaultConfigurationsInner.from_dict(code_security_default_configurations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


