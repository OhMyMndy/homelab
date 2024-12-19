# AutoMerge

The status of auto merging a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_by** | [**SimpleUser**](SimpleUser.md) |  | 
**merge_method** | **str** | The merge method to use. | 
**commit_title** | **str** | Title for the merge commit message. | 
**commit_message** | **str** | Commit message for the merge commit. | 

## Example

```python
from github_openapi.models.auto_merge import AutoMerge

# TODO update the JSON string below
json = "{}"
# create an instance of AutoMerge from a JSON string
auto_merge_instance = AutoMerge.from_json(json)
# print the JSON string representation of the object
print(AutoMerge.to_json())

# convert the object into a dict
auto_merge_dict = auto_merge_instance.to_dict()
# create an instance of AutoMerge from a dict
auto_merge_from_dict = AutoMerge.from_dict(auto_merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


