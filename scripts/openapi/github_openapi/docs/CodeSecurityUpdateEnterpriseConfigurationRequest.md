# CodeSecurityUpdateEnterpriseConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the code security configuration. Must be unique across the enterprise. | [optional] 
**description** | **str** | A description of the code security configuration | [optional] 
**advanced_security** | **str** | The enablement status of GitHub Advanced Security. Must be set to enabled if you want to enable any GHAS settings. | [optional] 
**dependency_graph** | **str** | The enablement status of Dependency Graph | [optional] 
**dependency_graph_autosubmit_action** | **str** | The enablement status of Automatic dependency submission | [optional] 
**dependency_graph_autosubmit_action_options** | [**CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions**](CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions.md) |  | [optional] 
**dependabot_alerts** | **str** | The enablement status of Dependabot alerts | [optional] 
**dependabot_security_updates** | **str** | The enablement status of Dependabot security updates | [optional] 
**code_scanning_default_setup** | **str** | The enablement status of code scanning default setup | [optional] 
**code_scanning_default_setup_options** | [**CodeScanningDefaultSetupOptions**](CodeScanningDefaultSetupOptions.md) |  | [optional] 
**secret_scanning** | **str** | The enablement status of secret scanning | [optional] 
**secret_scanning_push_protection** | **str** | The enablement status of secret scanning push protection | [optional] 
**secret_scanning_validity_checks** | **str** | The enablement status of secret scanning validity checks | [optional] 
**secret_scanning_non_provider_patterns** | **str** | The enablement status of secret scanning non-provider patterns | [optional] 
**private_vulnerability_reporting** | **str** | The enablement status of private vulnerability reporting | [optional] 
**enforcement** | **str** | The enforcement status for a security configuration | [optional] 

## Example

```python
from github_openapi.models.code_security_update_enterprise_configuration_request import CodeSecurityUpdateEnterpriseConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityUpdateEnterpriseConfigurationRequest from a JSON string
code_security_update_enterprise_configuration_request_instance = CodeSecurityUpdateEnterpriseConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityUpdateEnterpriseConfigurationRequest.to_json())

# convert the object into a dict
code_security_update_enterprise_configuration_request_dict = code_security_update_enterprise_configuration_request_instance.to_dict()
# create an instance of CodeSecurityUpdateEnterpriseConfigurationRequest from a dict
code_security_update_enterprise_configuration_request_from_dict = CodeSecurityUpdateEnterpriseConfigurationRequest.from_dict(code_security_update_enterprise_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


