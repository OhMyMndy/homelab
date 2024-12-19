# CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions

Feature options for secret scanning delegated bypass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | [**List[CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner]**](CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner.md) | The bypass reviewers for secret scanning delegated bypass | [optional] 

## Example

```python
from github_openapi.models.code_security_create_configuration_request_secret_scanning_delegated_bypass_options import CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions from a JSON string
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_instance = CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions.to_json())

# convert the object into a dict
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_dict = code_security_create_configuration_request_secret_scanning_delegated_bypass_options_instance.to_dict()
# create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions from a dict
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_from_dict = CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptions.from_dict(code_security_create_configuration_request_secret_scanning_delegated_bypass_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


