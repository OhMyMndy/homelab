# ReposSetTeamAccessRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | **List[str]** | The slug values for teams | 

## Example

```python
from github_openapi.models.repos_set_team_access_restrictions_request import ReposSetTeamAccessRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetTeamAccessRestrictionsRequest from a JSON string
repos_set_team_access_restrictions_request_instance = ReposSetTeamAccessRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposSetTeamAccessRestrictionsRequest.to_json())

# convert the object into a dict
repos_set_team_access_restrictions_request_dict = repos_set_team_access_restrictions_request_instance.to_dict()
# create an instance of ReposSetTeamAccessRestrictionsRequest from a dict
repos_set_team_access_restrictions_request_from_dict = ReposSetTeamAccessRestrictionsRequest.from_dict(repos_set_team_access_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


