# ProjectsV2IterationSetting

An iteration setting for an iteration field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**duration** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.projects_v2_iteration_setting import ProjectsV2IterationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsV2IterationSetting from a JSON string
projects_v2_iteration_setting_instance = ProjectsV2IterationSetting.from_json(json)
# print the JSON string representation of the object
print(ProjectsV2IterationSetting.to_json())

# convert the object into a dict
projects_v2_iteration_setting_dict = projects_v2_iteration_setting_instance.to_dict()
# create an instance of ProjectsV2IterationSetting from a dict
projects_v2_iteration_setting_from_dict = ProjectsV2IterationSetting.from_dict(projects_v2_iteration_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


