# SecretScanningLocationCommit

Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The file path in the repository | 
**start_line** | **float** | Line number at which the secret starts in the file | 
**end_line** | **float** | Line number at which the secret ends in the file | 
**start_column** | **float** | The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII | 
**end_column** | **float** | The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII | 
**blob_sha** | **str** | SHA-1 hash ID of the associated blob | 
**blob_url** | **str** | The API URL to get the associated blob resource | 
**commit_sha** | **str** | SHA-1 hash ID of the associated commit | 
**commit_url** | **str** | The API URL to get the associated commit resource | 

## Example

```python
from github_openapi.models.secret_scanning_location_commit import SecretScanningLocationCommit

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationCommit from a JSON string
secret_scanning_location_commit_instance = SecretScanningLocationCommit.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationCommit.to_json())

# convert the object into a dict
secret_scanning_location_commit_dict = secret_scanning_location_commit_instance.to_dict()
# create an instance of SecretScanningLocationCommit from a dict
secret_scanning_location_commit_from_dict = SecretScanningLocationCommit.from_dict(secret_scanning_location_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


