# GitCreateTreeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tree** | [**List[GitCreateTreeRequestTreeInner]**](GitCreateTreeRequestTreeInner.md) | Objects (of &#x60;path&#x60;, &#x60;mode&#x60;, &#x60;type&#x60;, and &#x60;sha&#x60;) specifying a tree structure. | 
**base_tree** | **str** | The SHA1 of an existing Git tree object which will be used as the base for the new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to by &#x60;base_tree&#x60; and entries defined in the &#x60;tree&#x60; parameter. Entries defined in the &#x60;tree&#x60; parameter will overwrite items from &#x60;base_tree&#x60; with the same &#x60;path&#x60;. If you&#39;re creating new changes on a branch, then normally you&#39;d set &#x60;base_tree&#x60; to the SHA1 of the Git tree object of the current latest commit on the branch you&#39;re working on. If not provided, GitHub will create a new Git tree object from only the entries defined in the &#x60;tree&#x60; parameter. If you create a new commit pointing to such a tree, then all files which were a part of the parent commit&#39;s tree and were not defined in the &#x60;tree&#x60; parameter will be listed as deleted by the new commit. | [optional] 

## Example

```python
from github_openapi.models.git_create_tree_request import GitCreateTreeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateTreeRequest from a JSON string
git_create_tree_request_instance = GitCreateTreeRequest.from_json(json)
# print the JSON string representation of the object
print(GitCreateTreeRequest.to_json())

# convert the object into a dict
git_create_tree_request_dict = git_create_tree_request_instance.to_dict()
# create an instance of GitCreateTreeRequest from a dict
git_create_tree_request_from_dict = GitCreateTreeRequest.from_dict(git_create_tree_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


