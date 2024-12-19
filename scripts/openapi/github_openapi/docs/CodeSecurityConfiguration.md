# CodeSecurityConfiguration

A code security configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the code security configuration | [optional] 
**name** | **str** | The name of the code security configuration. Must be unique within the organization. | [optional] 
**target_type** | **str** | The type of the code security configuration. | [optional] 
**description** | **str** | A description of the code security configuration | [optional] 
**advanced_security** | **str** | The enablement status of GitHub Advanced Security | [optional] 
**dependency_graph** | **str** | The enablement status of Dependency Graph | [optional] 
**dependency_graph_autosubmit_action** | **str** | The enablement status of Automatic dependency submission | [optional] 
**dependency_graph_autosubmit_action_options** | [**CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions**](CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions.md) |  | [optional] 
**dependabot_alerts** | **str** | The enablement status of Dependabot alerts | [optional] 
**dependabot_security_updates** | **str** | The enablement status of Dependabot security updates | [optional] 
**code_scanning_default_setup** | **str** | The enablement status of code scanning default setup | [optional] 
**code_scanning_default_setup_options** | [**CodeSecurityConfigurationCodeScanningDefaultSetupOptions**](CodeSecurityConfigurationCodeScanningDefaultSetupOptions.md) |  | [optional] 
**secret_scanning** | **str** | The enablement status of secret scanning | [optional] 
**secret_scanning_push_protection** | **str** | The enablement status of secret scanning push protection | [optional] 
**secret_scanning_delegated_bypass** | **str** | The enablement status of secret scanning delegated bypass | [optional] 
**secret_scanning_delegated_bypass_options** | [**CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions**](CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions.md) |  | [optional] 
**secret_scanning_validity_checks** | **str** | The enablement status of secret scanning validity checks | [optional] 
**secret_scanning_non_provider_patterns** | **str** | The enablement status of secret scanning non-provider patterns | [optional] 
**private_vulnerability_reporting** | **str** | The enablement status of private vulnerability reporting | [optional] 
**enforcement** | **str** | The enforcement status for a security configuration | [optional] 
**url** | **str** | The URL of the configuration | [optional] 
**html_url** | **str** | The URL of the configuration | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityConfiguration from a JSON string
code_security_configuration_instance = CodeSecurityConfiguration.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityConfiguration.to_json())

# convert the object into a dict
code_security_configuration_dict = code_security_configuration_instance.to_dict()
# create an instance of CodeSecurityConfiguration from a dict
code_security_configuration_from_dict = CodeSecurityConfiguration.from_dict(code_security_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


