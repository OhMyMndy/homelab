# ReposSetTeamAccessRestrictionsRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | **List[str]** | The slug values for teams | 

## Example

```python
from github_openapi.models.repos_set_team_access_restrictions_request_one_of import ReposSetTeamAccessRestrictionsRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetTeamAccessRestrictionsRequestOneOf from a JSON string
repos_set_team_access_restrictions_request_one_of_instance = ReposSetTeamAccessRestrictionsRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ReposSetTeamAccessRestrictionsRequestOneOf.to_json())

# convert the object into a dict
repos_set_team_access_restrictions_request_one_of_dict = repos_set_team_access_restrictions_request_one_of_instance.to_dict()
# create an instance of ReposSetTeamAccessRestrictionsRequestOneOf from a dict
repos_set_team_access_restrictions_request_one_of_from_dict = ReposSetTeamAccessRestrictionsRequestOneOf.from_dict(repos_set_team_access_restrictions_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


