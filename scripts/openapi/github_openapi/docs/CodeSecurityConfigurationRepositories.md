# CodeSecurityConfigurationRepositories

Repositories associated with a code security configuration and attachment status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The attachment status of the code security configuration on the repository. | [optional] 
**repository** | [**SimpleRepository**](SimpleRepository.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_security_configuration_repositories import CodeSecurityConfigurationRepositories

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityConfigurationRepositories from a JSON string
code_security_configuration_repositories_instance = CodeSecurityConfigurationRepositories.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityConfigurationRepositories.to_json())

# convert the object into a dict
code_security_configuration_repositories_dict = code_security_configuration_repositories_instance.to_dict()
# create an instance of CodeSecurityConfigurationRepositories from a dict
code_security_configuration_repositories_from_dict = CodeSecurityConfigurationRepositories.from_dict(code_security_configuration_repositories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


