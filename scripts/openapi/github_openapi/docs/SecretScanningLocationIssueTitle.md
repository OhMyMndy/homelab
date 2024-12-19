# SecretScanningLocationIssueTitle

Represents an 'issue_title' secret scanning location type. This location type shows that a secret was detected in the title of an issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_title_url** | **str** | The API URL to get the issue where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_issue_title import SecretScanningLocationIssueTitle

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationIssueTitle from a JSON string
secret_scanning_location_issue_title_instance = SecretScanningLocationIssueTitle.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationIssueTitle.to_json())

# convert the object into a dict
secret_scanning_location_issue_title_dict = secret_scanning_location_issue_title_instance.to_dict()
# create an instance of SecretScanningLocationIssueTitle from a dict
secret_scanning_location_issue_title_from_dict = SecretScanningLocationIssueTitle.from_dict(secret_scanning_location_issue_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


