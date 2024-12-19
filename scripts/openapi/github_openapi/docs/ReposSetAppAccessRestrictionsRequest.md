# ReposSetAppAccessRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | **List[str]** | The GitHub Apps that have push access to this branch. Use the slugified version of the app name. **Note**: The list of users, apps, and teams in total is limited to 100 items. | 

## Example

```python
from github_openapi.models.repos_set_app_access_restrictions_request import ReposSetAppAccessRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposSetAppAccessRestrictionsRequest from a JSON string
repos_set_app_access_restrictions_request_instance = ReposSetAppAccessRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposSetAppAccessRestrictionsRequest.to_json())

# convert the object into a dict
repos_set_app_access_restrictions_request_dict = repos_set_app_access_restrictions_request_instance.to_dict()
# create an instance of ReposSetAppAccessRestrictionsRequest from a dict
repos_set_app_access_restrictions_request_from_dict = ReposSetAppAccessRestrictionsRequest.from_dict(repos_set_app_access_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


