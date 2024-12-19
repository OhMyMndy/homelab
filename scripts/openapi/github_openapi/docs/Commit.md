# Commit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **List[str]** | An array of files added in the commit. A maximum of 3000 changed files will be reported per commit. | [optional] 
**author** | [**Committer**](Committer.md) |  | 
**committer** | [**Committer**](Committer.md) |  | 
**distinct** | **bool** | Whether this commit is distinct from any that have been pushed before. | 
**id** | **str** |  | 
**message** | **str** | The commit message. | 
**modified** | **List[str]** | An array of files modified by the commit. A maximum of 3000 changed files will be reported per commit. | [optional] 
**removed** | **List[str]** | An array of files removed in the commit. A maximum of 3000 changed files will be reported per commit. | [optional] 
**timestamp** | **datetime** | The ISO 8601 timestamp of the commit. | 
**tree_id** | **str** |  | 
**url** | **str** | URL that points to the commit API resource. | 

## Example

```python
from github_openapi.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print(Commit.to_json())

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_from_dict = Commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


