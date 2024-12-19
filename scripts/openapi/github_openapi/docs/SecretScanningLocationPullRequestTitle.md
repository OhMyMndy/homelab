# SecretScanningLocationPullRequestTitle

Represents a 'pull_request_title' secret scanning location type. This location type shows that a secret was detected in the title of a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request_title_url** | **str** | The API URL to get the pull request where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_pull_request_title import SecretScanningLocationPullRequestTitle

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationPullRequestTitle from a JSON string
secret_scanning_location_pull_request_title_instance = SecretScanningLocationPullRequestTitle.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationPullRequestTitle.to_json())

# convert the object into a dict
secret_scanning_location_pull_request_title_dict = secret_scanning_location_pull_request_title_instance.to_dict()
# create an instance of SecretScanningLocationPullRequestTitle from a dict
secret_scanning_location_pull_request_title_from_dict = SecretScanningLocationPullRequestTitle.from_dict(secret_scanning_location_pull_request_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


