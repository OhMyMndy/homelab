# ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection

Use the `status` property to enable or disable secret scanning AI detection for this repository. For more information, see \"[Responsible detection of generic secrets with AI](https://docs.github.com/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/generic-secret-detection/responsible-ai-generic-secrets).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_ai_detection import ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection from a JSON string
repos_update_request_security_and_analysis_secret_scanning_ai_detection_instance = ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_secret_scanning_ai_detection_dict = repos_update_request_security_and_analysis_secret_scanning_ai_detection_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection from a dict
repos_update_request_security_and_analysis_secret_scanning_ai_detection_from_dict = ReposUpdateRequestSecurityAndAnalysisSecretScanningAiDetection.from_dict(repos_update_request_security_and_analysis_secret_scanning_ai_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


