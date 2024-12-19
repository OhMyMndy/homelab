# ReposUpdateRequestSecurityAndAnalysis

Specify which security and analysis features to enable or disable for the repository.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  For example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request: `{ \"security_and_analysis\": {\"advanced_security\": { \"status\": \"enabled\" } } }`.  You can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_security** | [**ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity**](ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 
**secret_scanning** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanning**](ReposUpdateRequestSecurityAndAnalysisSecretScanning.md) |  | [optional] 
**secret_scanning_push_protection** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection**](ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.md) |  | [optional] 
**secret_scanning_ai_detection** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection**](ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection.md) |  | [optional] 
**secret_scanning_non_provider_patterns** | [**ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns**](ReposUpdateRequestSecurityAndAnalysisSecretScanningNonProviderPatterns.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis import ReposUpdateRequestSecurityAndAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysis from a JSON string
repos_update_request_security_and_analysis_instance = ReposUpdateRequestSecurityAndAnalysis.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysis.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_dict = repos_update_request_security_and_analysis_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysis from a dict
repos_update_request_security_and_analysis_from_dict = ReposUpdateRequestSecurityAndAnalysis.from_dict(repos_update_request_security_and_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


