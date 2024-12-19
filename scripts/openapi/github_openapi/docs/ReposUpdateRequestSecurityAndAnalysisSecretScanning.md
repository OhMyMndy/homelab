# ReposUpdateRequestSecurityAndAnalysisSecretScanning

Use the `status` property to enable or disable secret scanning for this repository. For more information, see \"[About secret scanning](/code-security/secret-security/about-secret-scanning).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis_secret_scanning import ReposUpdateRequestSecurityAndAnalysisSecretScanning

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanning from a JSON string
repos_update_request_security_and_analysis_secret_scanning_instance = ReposUpdateRequestSecurityAndAnalysisSecretScanning.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysisSecretScanning.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_secret_scanning_dict = repos_update_request_security_and_analysis_secret_scanning_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysisSecretScanning from a dict
repos_update_request_security_and_analysis_secret_scanning_from_dict = ReposUpdateRequestSecurityAndAnalysisSecretScanning.from_dict(repos_update_request_security_and_analysis_secret_scanning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


