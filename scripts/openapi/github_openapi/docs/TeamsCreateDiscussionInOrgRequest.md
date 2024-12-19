# TeamsCreateDiscussionInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The discussion post&#39;s title. | 
**body** | **str** | The discussion post&#39;s body text. | 
**private** | **bool** | Private posts are only visible to team members, organization owners, and team maintainers. Public posts are visible to all members of the organization. Set to &#x60;true&#x60; to create a private post. | [optional] [default to False]

## Example

```python
from github_openapi.models.teams_create_discussion_in_org_request import TeamsCreateDiscussionInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsCreateDiscussionInOrgRequest from a JSON string
teams_create_discussion_in_org_request_instance = TeamsCreateDiscussionInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsCreateDiscussionInOrgRequest.to_json())

# convert the object into a dict
teams_create_discussion_in_org_request_dict = teams_create_discussion_in_org_request_instance.to_dict()
# create an instance of TeamsCreateDiscussionInOrgRequest from a dict
teams_create_discussion_in_org_request_from_dict = TeamsCreateDiscussionInOrgRequest.from_dict(teams_create_discussion_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


