# WebhookSecurityAndAnalysisChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**WebhookSecurityAndAnalysisChangesFrom**](WebhookSecurityAndAnalysisChangesFrom.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_security_and_analysis_changes import WebhookSecurityAndAnalysisChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecurityAndAnalysisChanges from a JSON string
webhook_security_and_analysis_changes_instance = WebhookSecurityAndAnalysisChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookSecurityAndAnalysisChanges.to_json())

# convert the object into a dict
webhook_security_and_analysis_changes_dict = webhook_security_and_analysis_changes_instance.to_dict()
# create an instance of WebhookSecurityAndAnalysisChanges from a dict
webhook_security_and_analysis_changes_from_dict = WebhookSecurityAndAnalysisChanges.from_dict(webhook_security_and_analysis_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


