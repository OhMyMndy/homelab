# RepositoryLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_url** | **str** |  | 
**assignees_url** | **str** |  | 
**blobs_url** | **str** |  | 
**branches_url** | **str** |  | 
**collaborators_url** | **str** |  | 
**comments_url** | **str** |  | 
**commits_url** | **str** |  | 
**compare_url** | **str** |  | 
**contents_url** | **str** |  | 
**contributors_url** | **str** |  | 
**deployments_url** | **str** |  | 
**description** | **str** |  | 
**downloads_url** | **str** |  | 
**events_url** | **str** |  | 
**fork** | **bool** |  | 
**forks_url** | **str** |  | 
**full_name** | **str** |  | 
**git_commits_url** | **str** |  | 
**git_refs_url** | **str** |  | 
**git_tags_url** | **str** |  | 
**hooks_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the repository | 
**issue_comment_url** | **str** |  | 
**issue_events_url** | **str** |  | 
**issues_url** | **str** |  | 
**keys_url** | **str** |  | 
**labels_url** | **str** |  | 
**languages_url** | **str** |  | 
**merges_url** | **str** |  | 
**milestones_url** | **str** |  | 
**name** | **str** | The name of the repository. | 
**node_id** | **str** |  | 
**notifications_url** | **str** |  | 
**owner** | [**User2**](User2.md) |  | 
**private** | **bool** | Whether the repository is private or public. | 
**pulls_url** | **str** |  | 
**releases_url** | **str** |  | 
**stargazers_url** | **str** |  | 
**statuses_url** | **str** |  | 
**subscribers_url** | **str** |  | 
**subscription_url** | **str** |  | 
**tags_url** | **str** |  | 
**teams_url** | **str** |  | 
**trees_url** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.repository_lite import RepositoryLite

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryLite from a JSON string
repository_lite_instance = RepositoryLite.from_json(json)
# print the JSON string representation of the object
print(RepositoryLite.to_json())

# convert the object into a dict
repository_lite_dict = repository_lite_instance.to_dict()
# create an instance of RepositoryLite from a dict
repository_lite_from_dict = RepositoryLite.from_dict(repository_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


