# SecretScanningLocationIssueBody

Represents an 'issue_body' secret scanning location type. This location type shows that a secret was detected in the body of an issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_body_url** | **str** | The API URL to get the issue where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_issue_body import SecretScanningLocationIssueBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationIssueBody from a JSON string
secret_scanning_location_issue_body_instance = SecretScanningLocationIssueBody.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationIssueBody.to_json())

# convert the object into a dict
secret_scanning_location_issue_body_dict = secret_scanning_location_issue_body_instance.to_dict()
# create an instance of SecretScanningLocationIssueBody from a dict
secret_scanning_location_issue_body_from_dict = SecretScanningLocationIssueBody.from_dict(secret_scanning_location_issue_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


