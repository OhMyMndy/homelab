# MergeGroup

A group of pull requests that the merge queue has grouped together to be merged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_sha** | **str** | The SHA of the merge group. | 
**head_ref** | **str** | The full ref of the merge group. | 
**base_sha** | **str** | The SHA of the merge group&#39;s parent commit. | 
**base_ref** | **str** | The full ref of the branch the merge group will be merged into. | 
**head_commit** | [**SimpleCommit**](SimpleCommit.md) |  | 

## Example

```python
from github_openapi.models.merge_group import MergeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MergeGroup from a JSON string
merge_group_instance = MergeGroup.from_json(json)
# print the JSON string representation of the object
print(MergeGroup.to_json())

# convert the object into a dict
merge_group_dict = merge_group_instance.to_dict()
# create an instance of MergeGroup from a dict
merge_group_from_dict = MergeGroup.from_dict(merge_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


