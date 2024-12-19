# ReposAddTeamAccessRestrictionsRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | **List[str]** | The slug values for teams | 

## Example

```python
from github_openapi.models.repos_add_team_access_restrictions_request_one_of import ReposAddTeamAccessRestrictionsRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReposAddTeamAccessRestrictionsRequestOneOf from a JSON string
repos_add_team_access_restrictions_request_one_of_instance = ReposAddTeamAccessRestrictionsRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ReposAddTeamAccessRestrictionsRequestOneOf.to_json())

# convert the object into a dict
repos_add_team_access_restrictions_request_one_of_dict = repos_add_team_access_restrictions_request_one_of_instance.to_dict()
# create an instance of ReposAddTeamAccessRestrictionsRequestOneOf from a dict
repos_add_team_access_restrictions_request_one_of_from_dict = ReposAddTeamAccessRestrictionsRequestOneOf.from_dict(repos_add_team_access_restrictions_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


