# CodeSecurityCreateConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the code security configuration. Must be unique within the organization. | 
**description** | **str** | A description of the code security configuration | 
**advanced_security** | **str** | The enablement status of GitHub Advanced Security | [optional] [default to 'disabled']
**dependency_graph** | **str** | The enablement status of Dependency Graph | [optional] [default to 'enabled']
**dependency_graph_autosubmit_action** | **str** | The enablement status of Automatic dependency submission | [optional] [default to 'disabled']
**dependency_graph_autosubmit_action_options** | [**CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions**](CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions.md) |  | [optional] 
**dependabot_alerts** | **str** | The enablement status of Dependabot alerts | [optional] [default to 'disabled']
**dependabot_security_updates** | **str** | The enablement status of Dependabot security updates | [optional] [default to 'disabled']
**code_scanning_default_setup** | **str** | The enablement status of code scanning default setup | [optional] [default to 'disabled']
**code_scanning_default_setup_options** | [**CodeScanningDefaultSetupOptions**](CodeScanningDefaultSetupOptions.md) |  | [optional] 
**secret_scanning** | **str** | The enablement status of secret scanning | [optional] [default to 'disabled']
**secret_scanning_push_protection** | **str** | The enablement status of secret scanning push protection | [optional] [default to 'disabled']
**secret_scanning_delegated_bypass** | **str** | The enablement status of secret scanning delegated bypass | [optional] [default to 'disabled']
**secret_scanning_delegated_bypass_options** | [**CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions**](CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions.md) |  | [optional] 
**secret_scanning_validity_checks** | **str** | The enablement status of secret scanning validity checks | [optional] [default to 'disabled']
**secret_scanning_non_provider_patterns** | **str** | The enablement status of secret scanning non provider patterns | [optional] [default to 'disabled']
**private_vulnerability_reporting** | **str** | The enablement status of private vulnerability reporting | [optional] [default to 'disabled']
**enforcement** | **str** | The enforcement status for a security configuration | [optional] [default to 'enforced']

## Example

```python
from github_openapi.models.code_security_create_configuration_request import CodeSecurityCreateConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityCreateConfigurationRequest from a JSON string
code_security_create_configuration_request_instance = CodeSecurityCreateConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityCreateConfigurationRequest.to_json())

# convert the object into a dict
code_security_create_configuration_request_dict = code_security_create_configuration_request_instance.to_dict()
# create an instance of CodeSecurityCreateConfigurationRequest from a dict
code_security_create_configuration_request_from_dict = CodeSecurityCreateConfigurationRequest.from_dict(code_security_create_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


