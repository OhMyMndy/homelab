# CodeSecurityConfigurationCodeScanningDefaultSetupOptions

Feature options for code scanning default setup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_type** | **str** | Whether to use labeled runners or standard GitHub runners. | [optional] 
**runner_label** | **str** | The label of the runner to use for code scanning when runner_type is &#39;labeled&#39;. | [optional] 

## Example

```python
from github_openapi.models.code_security_configuration_code_scanning_default_setup_options import CodeSecurityConfigurationCodeScanningDefaultSetupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityConfigurationCodeScanningDefaultSetupOptions from a JSON string
code_security_configuration_code_scanning_default_setup_options_instance = CodeSecurityConfigurationCodeScanningDefaultSetupOptions.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityConfigurationCodeScanningDefaultSetupOptions.to_json())

# convert the object into a dict
code_security_configuration_code_scanning_default_setup_options_dict = code_security_configuration_code_scanning_default_setup_options_instance.to_dict()
# create an instance of CodeSecurityConfigurationCodeScanningDefaultSetupOptions from a dict
code_security_configuration_code_scanning_default_setup_options_from_dict = CodeSecurityConfigurationCodeScanningDefaultSetupOptions.from_dict(code_security_configuration_code_scanning_default_setup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


