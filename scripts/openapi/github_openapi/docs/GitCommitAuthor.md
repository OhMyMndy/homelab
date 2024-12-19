# GitCommitAuthor

Identifying information for the git-user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Timestamp of the commit | 
**email** | **str** | Git email address of the user | 
**name** | **str** | Name of the git user | 

## Example

```python
from github_openapi.models.git_commit_author import GitCommitAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommitAuthor from a JSON string
git_commit_author_instance = GitCommitAuthor.from_json(json)
# print the JSON string representation of the object
print(GitCommitAuthor.to_json())

# convert the object into a dict
git_commit_author_dict = git_commit_author_instance.to_dict()
# create an instance of GitCommitAuthor from a dict
git_commit_author_from_dict = GitCommitAuthor.from_dict(git_commit_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


