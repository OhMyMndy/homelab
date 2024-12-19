# ProjectsV2SingleSelectOption

An option for a single select field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.projects_v2_single_select_option import ProjectsV2SingleSelectOption

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsV2SingleSelectOption from a JSON string
projects_v2_single_select_option_instance = ProjectsV2SingleSelectOption.from_json(json)
# print the JSON string representation of the object
print(ProjectsV2SingleSelectOption.to_json())

# convert the object into a dict
projects_v2_single_select_option_dict = projects_v2_single_select_option_instance.to_dict()
# create an instance of ProjectsV2SingleSelectOption from a dict
projects_v2_single_select_option_from_dict = ProjectsV2SingleSelectOption.from_dict(projects_v2_single_select_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


