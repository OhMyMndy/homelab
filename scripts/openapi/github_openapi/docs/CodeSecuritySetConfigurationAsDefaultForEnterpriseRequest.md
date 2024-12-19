# CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_for_new_repos** | **str** | Specify which types of repository this security configuration should be applied to by default. | [optional] 

## Example

```python
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise_request import CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest from a JSON string
code_security_set_configuration_as_default_for_enterprise_request_instance = CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest.from_json(json)
# print the JSON string representation of the object
print(CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest.to_json())

# convert the object into a dict
code_security_set_configuration_as_default_for_enterprise_request_dict = code_security_set_configuration_as_default_for_enterprise_request_instance.to_dict()
# create an instance of CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest from a dict
code_security_set_configuration_as_default_for_enterprise_request_from_dict = CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest.from_dict(code_security_set_configuration_as_default_for_enterprise_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


