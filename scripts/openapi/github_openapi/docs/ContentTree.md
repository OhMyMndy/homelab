# ContentTree

Content Tree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**size** | **int** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**sha** | **str** |  | 
**content** | **str** |  | [optional] 
**url** | **str** |  | 
**git_url** | **str** |  | 
**html_url** | **str** |  | 
**download_url** | **str** |  | 
**entries** | [**List[ContentTreeEntriesInner]**](ContentTreeEntriesInner.md) |  | [optional] 
**links** | [**ContentTreeEntriesInnerLinks**](ContentTreeEntriesInnerLinks.md) |  | 

## Example

```python
from github_openapi.models.content_tree import ContentTree

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTree from a JSON string
content_tree_instance = ContentTree.from_json(json)
# print the JSON string representation of the object
print(ContentTree.to_json())

# convert the object into a dict
content_tree_dict = content_tree_instance.to_dict()
# create an instance of ContentTree from a dict
content_tree_from_dict = ContentTree.from_dict(content_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


