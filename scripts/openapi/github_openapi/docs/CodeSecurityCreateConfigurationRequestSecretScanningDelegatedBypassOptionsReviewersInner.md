# CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer_id** | **int** | The ID of the team or role selected as a bypass reviewer | 
**reviewer_type** | **str** | The type of the bypass reviewer | 

## Example

```python
from github_openapi.models.code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner import CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner from a JSON string
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner_instance = CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner.to_json())

# convert the object into a dict
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner_dict = code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner_instance.to_dict()
# create an instance of CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner from a dict
code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner_from_dict = CodeSecurityCreateConfigurationRequestSecretScanningDelegatedBypassOptionsReviewersInner.from_dict(code_security_create_configuration_request_secret_scanning_delegated_bypass_options_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


