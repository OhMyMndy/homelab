# SecretScanningLocationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The file path of the wiki page | 
**start_line** | **float** | Line number at which the secret starts in the file | 
**end_line** | **float** | Line number at which the secret ends in the file | 
**start_column** | **float** | The column at which the secret starts within the start line when the file is interpreted as 8-bit ASCII. | 
**end_column** | **float** | The column at which the secret ends within the end line when the file is interpreted as 8-bit ASCII. | 
**blob_sha** | **str** | SHA-1 hash ID of the associated blob | 
**blob_url** | **str** | The API URL to get the associated blob resource | 
**commit_sha** | **str** | SHA-1 hash ID of the associated commit | 
**commit_url** | **str** | The GitHub URL to get the associated wiki commit | 
**page_url** | **str** | The GitHub URL to get the associated wiki page | 
**issue_title_url** | **str** | The API URL to get the issue where the secret was detected. | 
**issue_body_url** | **str** | The API URL to get the issue where the secret was detected. | 
**issue_comment_url** | **str** | The API URL to get the issue comment where the secret was detected. | 
**discussion_title_url** | **str** | The URL to the discussion where the secret was detected. | 
**discussion_body_url** | **str** | The URL to the discussion where the secret was detected. | 
**discussion_comment_url** | **str** | The API URL to get the discussion comment where the secret was detected. | 
**pull_request_title_url** | **str** | The API URL to get the pull request where the secret was detected. | 
**pull_request_body_url** | **str** | The API URL to get the pull request where the secret was detected. | 
**pull_request_comment_url** | **str** | The API URL to get the pull request comment where the secret was detected. | 
**pull_request_review_url** | **str** | The API URL to get the pull request review where the secret was detected. | 
**pull_request_review_comment_url** | **str** | The API URL to get the pull request review comment where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_details import SecretScanningLocationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationDetails from a JSON string
secret_scanning_location_details_instance = SecretScanningLocationDetails.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationDetails.to_json())

# convert the object into a dict
secret_scanning_location_details_dict = secret_scanning_location_details_instance.to_dict()
# create an instance of SecretScanningLocationDetails from a dict
secret_scanning_location_details_from_dict = SecretScanningLocationDetails.from_dict(secret_scanning_location_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


