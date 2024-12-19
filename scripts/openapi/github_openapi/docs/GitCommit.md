# GitCommit

Low-level Git commit operations within a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | SHA for the commit | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**author** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**committer** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**message** | **str** | Message describing the purpose of the commit | 
**tree** | [**GitCommitTree**](GitCommitTree.md) |  | 
**parents** | [**List[GitCommitParentsInner]**](GitCommitParentsInner.md) |  | 
**verification** | [**GitCommitVerification**](GitCommitVerification.md) |  | 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.git_commit import GitCommit

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommit from a JSON string
git_commit_instance = GitCommit.from_json(json)
# print the JSON string representation of the object
print(GitCommit.to_json())

# convert the object into a dict
git_commit_dict = git_commit_instance.to_dict()
# create an instance of GitCommit from a dict
git_commit_from_dict = GitCommit.from_dict(git_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


