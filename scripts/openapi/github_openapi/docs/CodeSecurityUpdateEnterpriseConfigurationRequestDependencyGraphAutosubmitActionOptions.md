# CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions

Feature options for Automatic dependency submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labeled_runners** | **bool** | Whether to use runners labeled with &#39;dependency-submission&#39; or standard GitHub runners. | [optional] 

## Example

```python
from github_openapi.models.code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options import CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions from a JSON string
code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options_instance = CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions.to_json())

# convert the object into a dict
code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options_dict = code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options_instance.to_dict()
# create an instance of CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions from a dict
code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options_from_dict = CodeSecurityUpdateEnterpriseConfigurationRequestDependencyGraphAutosubmitActionOptions.from_dict(code_security_update_enterprise_configuration_request_dependency_graph_autosubmit_action_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


