# CodeScanningAlertInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | The Git reference, formatted as &#x60;refs/pull/&lt;number&gt;/merge&#x60;, &#x60;refs/pull/&lt;number&gt;/head&#x60;, &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. | [optional] 
**analysis_key** | **str** | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. | [optional] 
**environment** | **str** | Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed. | [optional] 
**category** | **str** | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. | [optional] 
**state** | [**CodeScanningAlertState**](CodeScanningAlertState.md) |  | [optional] 
**commit_sha** | **str** |  | [optional] 
**message** | [**CodeScanningAlertInstanceMessage**](CodeScanningAlertInstanceMessage.md) |  | [optional] 
**location** | [**CodeScanningAlertLocation**](CodeScanningAlertLocation.md) |  | [optional] 
**html_url** | **str** |  | [optional] 
**classifications** | [**List[CodeScanningAlertClassification]**](CodeScanningAlertClassification.md) | Classifications that have been applied to the file that triggered the alert. For example identifying it as documentation, or a generated file. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_alert_instance import CodeScanningAlertInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAlertInstance from a JSON string
code_scanning_alert_instance_instance = CodeScanningAlertInstance.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAlertInstance.to_json())

# convert the object into a dict
code_scanning_alert_instance_dict = code_scanning_alert_instance_instance.to_dict()
# create an instance of CodeScanningAlertInstance from a dict
code_scanning_alert_instance_from_dict = CodeScanningAlertInstance.from_dict(code_scanning_alert_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


