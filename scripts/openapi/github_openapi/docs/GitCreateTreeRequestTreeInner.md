# GitCreateTreeRequestTreeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The file referenced in the tree. | [optional] 
**mode** | **str** | The file mode; one of &#x60;100644&#x60; for file (blob), &#x60;100755&#x60; for executable (blob), &#x60;040000&#x60; for subdirectory (tree), &#x60;160000&#x60; for submodule (commit), or &#x60;120000&#x60; for a blob that specifies the path of a symlink. | [optional] 
**type** | **str** | Either &#x60;blob&#x60;, &#x60;tree&#x60;, or &#x60;commit&#x60;. | [optional] 
**sha** | **str** | The SHA1 checksum ID of the object in the tree. Also called &#x60;tree.sha&#x60;. If the value is &#x60;null&#x60; then the file will be deleted.      **Note:** Use either &#x60;tree.sha&#x60; or &#x60;content&#x60; to specify the contents of the entry. Using both &#x60;tree.sha&#x60; and &#x60;content&#x60; will return an error. | [optional] 
**content** | **str** | The content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, or &#x60;tree.sha&#x60;.      **Note:** Use either &#x60;tree.sha&#x60; or &#x60;content&#x60; to specify the contents of the entry. Using both &#x60;tree.sha&#x60; and &#x60;content&#x60; will return an error. | [optional] 

## Example

```python
from github_openapi.models.git_create_tree_request_tree_inner import GitCreateTreeRequestTreeInner

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateTreeRequestTreeInner from a JSON string
git_create_tree_request_tree_inner_instance = GitCreateTreeRequestTreeInner.from_json(json)
# print the JSON string representation of the object
print(GitCreateTreeRequestTreeInner.to_json())

# convert the object into a dict
git_create_tree_request_tree_inner_dict = git_create_tree_request_tree_inner_instance.to_dict()
# create an instance of GitCreateTreeRequestTreeInner from a dict
git_create_tree_request_tree_inner_from_dict = GitCreateTreeRequestTreeInner.from_dict(git_create_tree_request_tree_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


