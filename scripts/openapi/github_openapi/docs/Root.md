# Root


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_user_url** | **str** |  | 
**current_user_authorizations_html_url** | **str** |  | 
**authorizations_url** | **str** |  | 
**code_search_url** | **str** |  | 
**commit_search_url** | **str** |  | 
**emails_url** | **str** |  | 
**emojis_url** | **str** |  | 
**events_url** | **str** |  | 
**feeds_url** | **str** |  | 
**followers_url** | **str** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**hub_url** | **str** |  | [optional] 
**issue_search_url** | **str** |  | 
**issues_url** | **str** |  | 
**keys_url** | **str** |  | 
**label_search_url** | **str** |  | 
**notifications_url** | **str** |  | 
**organization_url** | **str** |  | 
**organization_repositories_url** | **str** |  | 
**organization_teams_url** | **str** |  | 
**public_gists_url** | **str** |  | 
**rate_limit_url** | **str** |  | 
**repository_url** | **str** |  | 
**repository_search_url** | **str** |  | 
**current_user_repositories_url** | **str** |  | 
**starred_url** | **str** |  | 
**starred_gists_url** | **str** |  | 
**topic_search_url** | **str** |  | [optional] 
**user_url** | **str** |  | 
**user_organizations_url** | **str** |  | 
**user_repositories_url** | **str** |  | 
**user_search_url** | **str** |  | 

## Example

```python
from github_openapi.models.root import Root

# TODO update the JSON string below
json = "{}"
# create an instance of Root from a JSON string
root_instance = Root.from_json(json)
# print the JSON string representation of the object
print(Root.to_json())

# convert the object into a dict
root_dict = root_instance.to_dict()
# create an instance of Root from a dict
root_from_dict = Root.from_dict(root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


