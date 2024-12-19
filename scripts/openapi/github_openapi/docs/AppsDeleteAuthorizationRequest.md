# AppsDeleteAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The OAuth access token used to authenticate to the GitHub API. | 

## Example

```python
from github_openapi.models.apps_delete_authorization_request import AppsDeleteAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppsDeleteAuthorizationRequest from a JSON string
apps_delete_authorization_request_instance = AppsDeleteAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(AppsDeleteAuthorizationRequest.to_json())

# convert the object into a dict
apps_delete_authorization_request_dict = apps_delete_authorization_request_instance.to_dict()
# create an instance of AppsDeleteAuthorizationRequest from a dict
apps_delete_authorization_request_from_dict = AppsDeleteAuthorizationRequest.from_dict(apps_delete_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


