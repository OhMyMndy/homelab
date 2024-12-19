# DependabotAlertPackage

Details for the vulnerable package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** | The package&#39;s language or package management ecosystem. | [readonly] 
**name** | **str** | The unique package name within its ecosystem. | [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_package import DependabotAlertPackage

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertPackage from a JSON string
dependabot_alert_package_instance = DependabotAlertPackage.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertPackage.to_json())

# convert the object into a dict
dependabot_alert_package_dict = dependabot_alert_package_instance.to_dict()
# create an instance of DependabotAlertPackage from a dict
dependabot_alert_package_from_dict = DependabotAlertPackage.from_dict(dependabot_alert_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


