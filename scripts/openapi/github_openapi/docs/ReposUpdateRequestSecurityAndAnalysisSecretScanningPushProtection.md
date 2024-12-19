# ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection

Use the `status` property to enable or disable secret scanning push protection for this repository. For more information, see \"[Protecting pushes with secret scanning](/code-security/secret-scanning/protecting-pushes-with-secret-scanning).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning_push_protection import ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection from a JSON string
repos_update_request_security_and_analysis_secret_scanning_push_protection_instance = ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_secret_scanning_push_protection_dict = repos_update_request_security_and_analysis_secret_scanning_push_protection_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection from a dict
repos_update_request_security_and_analysis_secret_scanning_push_protection_from_dict = ReposUpdateRequestSecurityAndAnalysisSecretScanningPushProtection.from_dict(repos_update_request_security_and_analysis_secret_scanning_push_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


