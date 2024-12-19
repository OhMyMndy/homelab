# GitCreateCommitRequestCommitter

Information about the person who is making the commit. By default, `committer` will use the information set in `author`. See the `author` and `committer` object below for details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author (or committer) of the commit | [optional] 
**email** | **str** | The email of the author (or committer) of the commit | [optional] 
**var_date** | **datetime** | Indicates when this commit was authored (or committed). This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

## Example

```python
from github_openapi.models.git_create_commit_request_committer import GitCreateCommitRequestCommitter

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateCommitRequestCommitter from a JSON string
git_create_commit_request_committer_instance = GitCreateCommitRequestCommitter.from_json(json)
# print the JSON string representation of the object
print(GitCreateCommitRequestCommitter.to_json())

# convert the object into a dict
git_create_commit_request_committer_dict = git_create_commit_request_committer_instance.to_dict()
# create an instance of GitCreateCommitRequestCommitter from a dict
git_create_commit_request_committer_from_dict = GitCreateCommitRequestCommitter.from_dict(git_create_commit_request_committer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


