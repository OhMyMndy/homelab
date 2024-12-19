# GitRefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**sha** | **str** | SHA for the reference | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.git_ref_object import GitRefObject

# TODO update the JSON string below
json = "{}"
# create an instance of GitRefObject from a JSON string
git_ref_object_instance = GitRefObject.from_json(json)
# print the JSON string representation of the object
print(GitRefObject.to_json())

# convert the object into a dict
git_ref_object_dict = git_ref_object_instance.to_dict()
# create an instance of GitRefObject from a dict
git_ref_object_from_dict = GitRefObject.from_dict(git_ref_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


