# ContentTreeEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**size** | **int** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 
**git_url** | **str** |  | 
**html_url** | **str** |  | 
**download_url** | **str** |  | 
**links** | [**ContentTreeEntriesInnerLinks**](ContentTreeEntriesInnerLinks.md) |  | 

## Example

```python
from github_openapi.models.content_tree_entries_inner import ContentTreeEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTreeEntriesInner from a JSON string
content_tree_entries_inner_instance = ContentTreeEntriesInner.from_json(json)
# print the JSON string representation of the object
print(ContentTreeEntriesInner.to_json())

# convert the object into a dict
content_tree_entries_inner_dict = content_tree_entries_inner_instance.to_dict()
# create an instance of ContentTreeEntriesInner from a dict
content_tree_entries_inner_from_dict = ContentTreeEntriesInner.from_dict(content_tree_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


