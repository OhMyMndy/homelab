# ReposAddTeamAccessRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | **List[str]** | The slug values for teams | 

## Example

```python
from github_openapi.models.repos_add_team_access_restrictions_request import ReposAddTeamAccessRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposAddTeamAccessRestrictionsRequest from a JSON string
repos_add_team_access_restrictions_request_instance = ReposAddTeamAccessRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposAddTeamAccessRestrictionsRequest.to_json())

# convert the object into a dict
repos_add_team_access_restrictions_request_dict = repos_add_team_access_restrictions_request_instance.to_dict()
# create an instance of ReposAddTeamAccessRestrictionsRequest from a dict
repos_add_team_access_restrictions_request_from_dict = ReposAddTeamAccessRestrictionsRequest.from_dict(repos_add_team_access_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


