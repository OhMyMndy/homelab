# ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity

Use the `status` property to enable or disable GitHub Advanced Security for this repository. For more information, see \"[About GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-security).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_request_security_and_analysis_advanced_security import ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity from a JSON string
repos_update_request_security_and_analysis_advanced_security_instance = ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.to_json())

# convert the object into a dict
repos_update_request_security_and_analysis_advanced_security_dict = repos_update_request_security_and_analysis_advanced_security_instance.to_dict()
# create an instance of ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity from a dict
repos_update_request_security_and_analysis_advanced_security_from_dict = ReposUpdateRequestSecurityAndAnalysisAdvancedSecurity.from_dict(repos_update_request_security_and_analysis_advanced_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


