# AlertInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_key** | **str** | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. | 
**category** | **str** | Identifies the configuration under which the analysis was executed. | [optional] 
**classifications** | **List[str]** |  | [optional] 
**commit_sha** | **str** |  | [optional] 
**environment** | **str** | Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed. | 
**location** | [**AlertInstanceLocation**](AlertInstanceLocation.md) |  | [optional] 
**message** | [**CodeScanningAlertInstanceMessage**](CodeScanningAlertInstanceMessage.md) |  | [optional] 
**ref** | **str** | The full Git reference, formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;. | 
**state** | **str** | State of a code scanning alert. | 

## Example

```python
from github_openapi.models.alert_instance import AlertInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AlertInstance from a JSON string
alert_instance_instance = AlertInstance.from_json(json)
# print the JSON string representation of the object
print(AlertInstance.to_json())

# convert the object into a dict
alert_instance_dict = alert_instance_instance.to_dict()
# create an instance of AlertInstance from a dict
alert_instance_from_dict = AlertInstance.from_dict(alert_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


