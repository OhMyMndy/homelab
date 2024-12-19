# SecurityAndAnalysisDependabotSecurityUpdates

Enable or disable Dependabot security updates for the repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The enablement status of Dependabot security updates for the repository. | [optional] 

## Example

```python
from github_openapi.models.security_and_analysis_dependabot_security_updates import SecurityAndAnalysisDependabotSecurityUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityAndAnalysisDependabotSecurityUpdates from a JSON string
security_and_analysis_dependabot_security_updates_instance = SecurityAndAnalysisDependabotSecurityUpdates.from_json(json)
# print the JSON string representation of the object
print(SecurityAndAnalysisDependabotSecurityUpdates.to_json())

# convert the object into a dict
security_and_analysis_dependabot_security_updates_dict = security_and_analysis_dependabot_security_updates_instance.to_dict()
# create an instance of SecurityAndAnalysisDependabotSecurityUpdates from a dict
security_and_analysis_dependabot_security_updates_from_dict = SecurityAndAnalysisDependabotSecurityUpdates.from_dict(security_and_analysis_dependabot_security_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


