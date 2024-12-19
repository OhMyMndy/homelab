# DependabotAlertWithRepositoryDependency

Details for the vulnerable dependency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**DependabotAlertPackage**](DependabotAlertPackage.md) |  | [optional] 
**manifest_path** | **str** | The full path to the dependency manifest file, relative to the root of the repository. | [optional] [readonly] 
**scope** | **str** | The execution scope of the vulnerable dependency. | [optional] [readonly] 

## Example

```python
from github_openapi.models.dependabot_alert_with_repository_dependency import DependabotAlertWithRepositoryDependency

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotAlertWithRepositoryDependency from a JSON string
dependabot_alert_with_repository_dependency_instance = DependabotAlertWithRepositoryDependency.from_json(json)
# print the JSON string representation of the object
print(DependabotAlertWithRepositoryDependency.to_json())

# convert the object into a dict
dependabot_alert_with_repository_dependency_dict = dependabot_alert_with_repository_dependency_instance.to_dict()
# create an instance of DependabotAlertWithRepositoryDependency from a dict
dependabot_alert_with_repository_dependency_from_dict = DependabotAlertWithRepositoryDependency.from_dict(dependabot_alert_with_repository_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


