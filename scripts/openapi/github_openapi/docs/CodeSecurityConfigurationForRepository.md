# CodeSecurityConfigurationForRepository

Code security configuration associated with a repository and attachment status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The attachment status of the code security configuration on the repository. | [optional] 
**configuration** | [**CodeSecurityConfiguration**](CodeSecurityConfiguration.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_security_configuration_for_repository import CodeSecurityConfigurationForRepository

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityConfigurationForRepository from a JSON string
code_security_configuration_for_repository_instance = CodeSecurityConfigurationForRepository.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityConfigurationForRepository.to_json())

# convert the object into a dict
code_security_configuration_for_repository_dict = code_security_configuration_for_repository_instance.to_dict()
# create an instance of CodeSecurityConfigurationForRepository from a dict
code_security_configuration_for_repository_from_dict = CodeSecurityConfigurationForRepository.from_dict(code_security_configuration_for_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


