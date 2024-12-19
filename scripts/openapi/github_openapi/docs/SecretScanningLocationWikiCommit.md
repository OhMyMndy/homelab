# SecretScanningLocationWikiCommit

Represents a 'wiki_commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository wiki.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The file path of the wiki page | 
**start_line** | **float** | Line number at which the secret starts in the file | 
**end_line** | **float** | Line number at which the secret ends in the file | 
**start_column** | **float** | The column at which the secret starts within the start line when the file is interpreted as 8-bit ASCII. | 
**end_column** | **float** | The column at which the secret ends within the end line when the file is interpreted as 8-bit ASCII. | 
**blob_sha** | **str** | SHA-1 hash ID of the associated blob | 
**page_url** | **str** | The GitHub URL to get the associated wiki page | 
**commit_sha** | **str** | SHA-1 hash ID of the associated commit | 
**commit_url** | **str** | The GitHub URL to get the associated wiki commit | 

## Example

```python
from github_openapi.models.secret_scanning_location_wiki_commit import SecretScanningLocationWikiCommit

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationWikiCommit from a JSON string
secret_scanning_location_wiki_commit_instance = SecretScanningLocationWikiCommit.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationWikiCommit.to_json())

# convert the object into a dict
secret_scanning_location_wiki_commit_dict = secret_scanning_location_wiki_commit_instance.to_dict()
# create an instance of SecretScanningLocationWikiCommit from a dict
secret_scanning_location_wiki_commit_from_dict = SecretScanningLocationWikiCommit.from_dict(secret_scanning_location_wiki_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


