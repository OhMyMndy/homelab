# ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns

Use the `status` property to enable or disable secret scanning non-provider patterns for this repository. For more information, see \"[Supported secret scanning patterns](/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns import ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns from a JSON string
repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns_instance = ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns_dict = repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns from a dict
repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns_from_dict = ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns.from_dict(repos_update_request_security_and_analysis_secret_scanning_non_provider_patterns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


