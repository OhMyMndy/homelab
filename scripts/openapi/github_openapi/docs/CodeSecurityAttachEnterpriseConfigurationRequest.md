# CodeSecurityAttachEnterpriseConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The type of repositories to attach the configuration to. &#x60;selected&#x60; means the configuration will be attached to only the repositories specified by &#x60;selected_repository_ids&#x60; | 

## Example

```python
from github_openapi.models.code_security_attach_enterprise_configuration_request import CodeSecurityAttachEnterpriseConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityAttachEnterpriseConfigurationRequest from a JSON string
code_security_attach_enterprise_configuration_request_instance = CodeSecurityAttachEnterpriseConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityAttachEnterpriseConfigurationRequest.to_json())

# convert the object into a dict
code_security_attach_enterprise_configuration_request_dict = code_security_attach_enterprise_configuration_request_instance.to_dict()
# create an instance of CodeSecurityAttachEnterpriseConfigurationRequest from a dict
code_security_attach_enterprise_configuration_request_from_dict = CodeSecurityAttachEnterpriseConfigurationRequest.from_dict(code_security_attach_enterprise_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


