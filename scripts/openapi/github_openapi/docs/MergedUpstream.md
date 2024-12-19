# MergedUpstream

Results of a successful merge upstream request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**merge_type** | **str** |  | [optional] 
**base_branch** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.merged_upstream import MergedUpstream

# TODO update the JSON string below
json = "{}"
# create an instance of MergedUpstream from a JSON string
merged_upstream_instance = MergedUpstream.from_json(json)
# print the JSON string representation of the object
print(MergedUpstream.to_json())

# convert the object into a dict
merged_upstream_dict = merged_upstream_instance.to_dict()
# create an instance of MergedUpstream from a dict
merged_upstream_from_dict = MergedUpstream.from_dict(merged_upstream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


