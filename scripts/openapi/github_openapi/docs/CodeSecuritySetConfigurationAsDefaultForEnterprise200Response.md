# CodeSecuritySetConfigurationAsDefaultForEnterprise200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_for_new_repos** | **str** | Specifies which types of repository this security configuration is applied to by default. | [optional] 
**configuration** | [**CodeSecurityConfiguration**](CodeSecurityConfiguration.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise200_response import CodeSecuritySetConfigurationAsDefaultForEnterprise200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecuritySetConfigurationAsDefaultForEnterprise200Response from a JSON string
code_security_set_configuration_as_default_for_enterprise200_response_instance = CodeSecuritySetConfigurationAsDefaultForEnterprise200Response.from_json(json)
# print the JSON string representation of the object
print(CodeSecuritySetConfigurationAsDefaultForEnterprise200Response.to_json())

# convert the object into a dict
code_security_set_configuration_as_default_for_enterprise200_response_dict = code_security_set_configuration_as_default_for_enterprise200_response_instance.to_dict()
# create an instance of CodeSecuritySetConfigurationAsDefaultForEnterprise200Response from a dict
code_security_set_configuration_as_default_for_enterprise200_response_from_dict = CodeSecuritySetConfigurationAsDefaultForEnterprise200Response.from_dict(code_security_set_configuration_as_default_for_enterprise200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


