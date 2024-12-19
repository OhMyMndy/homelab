# GitTagObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.git_tag_object import GitTagObject

# TODO update the JSON string below
json = "{}"
# create an instance of GitTagObject from a JSON string
git_tag_object_instance = GitTagObject.from_json(json)
# print the JSON string representation of the object
print(GitTagObject.to_json())

# convert the object into a dict
git_tag_object_dict = git_tag_object_instance.to_dict()
# create an instance of GitTagObject from a dict
git_tag_object_from_dict = GitTagObject.from_dict(git_tag_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


