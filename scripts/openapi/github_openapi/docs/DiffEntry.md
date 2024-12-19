# DiffEntry

Diff Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**filename** | **str** |  | 
**status** | **str** |  | 
**additions** | **int** |  | 
**deletions** | **int** |  | 
**changes** | **int** |  | 
**blob_url** | **str** |  | 
**raw_url** | **str** |  | 
**contents_url** | **str** |  | 
**patch** | **str** |  | [optional] 
**previous_filename** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.diff_entry import DiffEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DiffEntry from a JSON string
diff_entry_instance = DiffEntry.from_json(json)
# print the JSON string representation of the object
print(DiffEntry.to_json())

# convert the object into a dict
diff_entry_dict = diff_entry_instance.to_dict()
# create an instance of DiffEntry from a dict
diff_entry_from_dict = DiffEntry.from_dict(diff_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


