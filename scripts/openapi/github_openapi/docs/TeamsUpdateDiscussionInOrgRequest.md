# TeamsUpdateDiscussionInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The discussion post&#39;s title. | [optional] 
**body** | **str** | The discussion post&#39;s body text. | [optional] 

## Example

```python
from github_openapi.models.teams_update_discussion_in_org_request import TeamsUpdateDiscussionInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsUpdateDiscussionInOrgRequest from a JSON string
teams_update_discussion_in_org_request_instance = TeamsUpdateDiscussionInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsUpdateDiscussionInOrgRequest.to_json())

# convert the object into a dict
teams_update_discussion_in_org_request_dict = teams_update_discussion_in_org_request_instance.to_dict()
# create an instance of TeamsUpdateDiscussionInOrgRequest from a dict
teams_update_discussion_in_org_request_from_dict = TeamsUpdateDiscussionInOrgRequest.from_dict(teams_update_discussion_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


