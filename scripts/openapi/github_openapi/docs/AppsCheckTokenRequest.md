# AppsCheckTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access_token of the OAuth or GitHub application. | 

## Example

```python
from github_openapi.models.apps_check_token_request import AppsCheckTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppsCheckTokenRequest from a JSON string
apps_check_token_request_instance = AppsCheckTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AppsCheckTokenRequest.to_json())

# convert the object into a dict
apps_check_token_request_dict = apps_check_token_request_instance.to_dict()
# create an instance of AppsCheckTokenRequest from a dict
apps_check_token_request_from_dict = AppsCheckTokenRequest.from_dict(apps_check_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


