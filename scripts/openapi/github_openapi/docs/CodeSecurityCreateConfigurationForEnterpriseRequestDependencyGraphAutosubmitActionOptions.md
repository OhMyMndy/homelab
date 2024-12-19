# CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions

Feature options for Automatic dependency submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labeled_runners** | **bool** | Whether to use runners labeled with &#39;dependency-submission&#39; or standard GitHub runners. | [optional] [default to False]

## Example

```python
from github_openapi.models.code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options import CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions from a JSON string
code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options_instance = CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions.to_json())

# convert the object into a dict
code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options_dict = code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options_instance.to_dict()
# create an instance of CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions from a dict
code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options_from_dict = CodeSecurityCreateConfigurationForEnterpriseRequestDependencyGraphAutosubmitActionOptions.from_dict(code_security_create_configuration_for_enterprise_request_dependency_graph_autosubmit_action_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


