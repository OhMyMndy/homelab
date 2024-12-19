# ContentSubmodule

An object describing a submodule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**submodule_git_url** | **str** |  | 
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
from github_openapi.models.content_submodule import ContentSubmodule

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSubmodule from a JSON string
content_submodule_instance = ContentSubmodule.from_json(json)
# print the JSON string representation of the object
print(ContentSubmodule.to_json())

# convert the object into a dict
content_submodule_dict = content_submodule_instance.to_dict()
# create an instance of ContentSubmodule from a dict
content_submodule_from_dict = ContentSubmodule.from_dict(content_submodule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


