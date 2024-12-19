# GitCreateCommitRequestAuthor

Information about the author of the commit. By default, the `author` will be the authenticated user and the current date. See the `author` and `committer` object below for details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author (or committer) of the commit | 
**email** | **str** | The email of the author (or committer) of the commit | 
**var_date** | **datetime** | Indicates when this commit was authored (or committed). This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

## Example

```python
from github_openapi.models.git_create_commit_request_author import GitCreateCommitRequestAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateCommitRequestAuthor from a JSON string
git_create_commit_request_author_instance = GitCreateCommitRequestAuthor.from_json(json)
# print the JSON string representation of the object
print(GitCreateCommitRequestAuthor.to_json())

# convert the object into a dict
git_create_commit_request_author_dict = git_create_commit_request_author_instance.to_dict()
# create an instance of GitCreateCommitRequestAuthor from a dict
git_create_commit_request_author_from_dict = GitCreateCommitRequestAuthor.from_dict(git_create_commit_request_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


