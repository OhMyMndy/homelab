# ReposSetUserAccessRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | The username for users | 

## Example

```python
from github_openapi.models.repos_set_user_access_restrictions_request import ReposSetUserAccessRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetUserAccessRestrictionsRequest from a JSON string
repos_set_user_access_restrictions_request_instance = ReposSetUserAccessRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposSetUserAccessRestrictionsRequest.to_json())

# convert the object into a dict
repos_set_user_access_restrictions_request_dict = repos_set_user_access_restrictions_request_instance.to_dict()
# create an instance of ReposSetUserAccessRestrictionsRequest from a dict
repos_set_user_access_restrictions_request_from_dict = ReposSetUserAccessRestrictionsRequest.from_dict(repos_set_user_access_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


