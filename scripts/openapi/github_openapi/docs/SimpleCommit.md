# SimpleCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Committer**](Committer.md) |  | 
**committer** | [**Committer**](Committer.md) |  | 
**id** | **str** |  | 
**message** | **str** |  | 
**timestamp** | **str** |  | 
**tree_id** | **str** |  | 

## Example

```python
from github_openapi.models.simple_commit import SimpleCommit

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCommit from a JSON string
simple_commit_instance = SimpleCommit.from_json(json)
# print the JSON string representation of the object
print(SimpleCommit.to_json())

# convert the object into a dict
simple_commit_dict = simple_commit_instance.to_dict()
# create an instance of SimpleCommit from a dict
simple_commit_from_dict = SimpleCommit.from_dict(simple_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


