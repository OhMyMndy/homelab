# SecurityAndAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_security** | [**SecurityAndAnalysisAdvancedSecurity**](SecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 
**dependabot_security_updates** | [**SecurityAndAnalysisDependabotSecurityUpdates**](SecurityAndAnalysisDependabotSecurityUpdates.md) |  | [optional] 
**secret_scanning** | [**SecurityAndAnalysisAdvancedSecurity**](SecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 
**secret_scanning_push_protection** | [**SecurityAndAnalysisAdvancedSecurity**](SecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 
**secret_scanning_non_provider_patterns** | [**SecurityAndAnalysisAdvancedSecurity**](SecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 
**secret_scanning_ai_detection** | [**SecurityAndAnalysisAdvancedSecurity**](SecurityAndAnalysisAdvancedSecurity.md) |  | [optional] 

## Example

```python
from github_openapi.models.security_and_analysis import SecurityAndAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityAndAnalysis from a JSON string
security_and_analysis_instance = SecurityAndAnalysis.from_json(json)
# print the JSON string representation of the object
print(SecurityAndAnalysis.to_json())

# convert the object into a dict
security_and_analysis_dict = security_and_analysis_instance.to_dict()
# create an instance of SecurityAndAnalysis from a dict
security_and_analysis_from_dict = SecurityAndAnalysis.from_dict(security_and_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


