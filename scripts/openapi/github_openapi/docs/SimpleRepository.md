# SimpleRepository

A GitHub repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier of the repository. | 
**node_id** | **str** | The GraphQL identifier of the repository. | 
**name** | **str** | The name of the repository. | 
**full_name** | **str** | The full, globally unique, name of the repository. | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**private** | **bool** | Whether the repository is private. | 
**html_url** | **str** | The URL to view the repository on GitHub.com. | 
**description** | **str** | The repository description. | 
**fork** | **bool** | Whether the repository is a fork. | 
**url** | **str** | The URL to get more information about the repository from the GitHub API. | 
**archive_url** | **str** | A template for the API URL to download the repository as an archive. | 
**assignees_url** | **str** | A template for the API URL to list the available assignees for issues in the repository. | 
**blobs_url** | **str** | A template for the API URL to create or retrieve a raw Git blob in the repository. | 
**branches_url** | **str** | A template for the API URL to get information about branches in the repository. | 
**collaborators_url** | **str** | A template for the API URL to get information about collaborators of the repository. | 
**comments_url** | **str** | A template for the API URL to get information about comments on the repository. | 
**commits_url** | **str** | A template for the API URL to get information about commits on the repository. | 
**compare_url** | **str** | A template for the API URL to compare two commits or refs. | 
**contents_url** | **str** | A template for the API URL to get the contents of the repository. | 
**contributors_url** | **str** | A template for the API URL to list the contributors to the repository. | 
**deployments_url** | **str** | The API URL to list the deployments of the repository. | 
**downloads_url** | **str** | The API URL to list the downloads on the repository. | 
**events_url** | **str** | The API URL to list the events of the repository. | 
**forks_url** | **str** | The API URL to list the forks of the repository. | 
**git_commits_url** | **str** | A template for the API URL to get information about Git commits of the repository. | 
**git_refs_url** | **str** | A template for the API URL to get information about Git refs of the repository. | 
**git_tags_url** | **str** | A template for the API URL to get information about Git tags of the repository. | 
**issue_comment_url** | **str** | A template for the API URL to get information about issue comments on the repository. | 
**issue_events_url** | **str** | A template for the API URL to get information about issue events on the repository. | 
**issues_url** | **str** | A template for the API URL to get information about issues on the repository. | 
**keys_url** | **str** | A template for the API URL to get information about deploy keys on the repository. | 
**labels_url** | **str** | A template for the API URL to get information about labels of the repository. | 
**languages_url** | **str** | The API URL to get information about the languages of the repository. | 
**merges_url** | **str** | The API URL to merge branches in the repository. | 
**milestones_url** | **str** | A template for the API URL to get information about milestones of the repository. | 
**notifications_url** | **str** | A template for the API URL to get information about notifications on the repository. | 
**pulls_url** | **str** | A template for the API URL to get information about pull requests on the repository. | 
**releases_url** | **str** | A template for the API URL to get information about releases on the repository. | 
**stargazers_url** | **str** | The API URL to list the stargazers on the repository. | 
**statuses_url** | **str** | A template for the API URL to get information about statuses of a commit. | 
**subscribers_url** | **str** | The API URL to list the subscribers on the repository. | 
**subscription_url** | **str** | The API URL to subscribe to notifications for this repository. | 
**tags_url** | **str** | The API URL to get information about tags on the repository. | 
**teams_url** | **str** | The API URL to list the teams on the repository. | 
**trees_url** | **str** | A template for the API URL to create or retrieve a raw Git tree of the repository. | 
**hooks_url** | **str** | The API URL to list the hooks on the repository. | 

## Example

```python
from github_openapi.models.simple_repository import SimpleRepository

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleRepository from a JSON string
simple_repository_instance = SimpleRepository.from_json(json)
# print the JSON string representation of the object
print(SimpleRepository.to_json())

# convert the object into a dict
simple_repository_dict = simple_repository_instance.to_dict()
# create an instance of SimpleRepository from a dict
simple_repository_from_dict = SimpleRepository.from_dict(simple_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


