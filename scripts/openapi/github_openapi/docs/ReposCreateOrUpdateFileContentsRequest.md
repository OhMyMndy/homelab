# ReposCreateOrUpdateFileContentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The commit message. | 
**content** | **str** | The new file content, using Base64 encoding. | 
**sha** | **str** | **Required if you are updating a file**. The blob SHA of the file being replaced. | [optional] 
**branch** | **str** | The branch name. Default: the repository’s default branch. | [optional] 
**committer** | [**ReposCreateOrUpdateFileContentsRequestCommitter**](ReposCreateOrUpdateFileContentsRequestCommitter.md) |  | [optional] 
**author** | [**ReposCreateOrUpdateFileContentsRequestAuthor**](ReposCreateOrUpdateFileContentsRequestAuthor.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_or_update_file_contents_request import ReposCreateOrUpdateFileContentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateFileContentsRequest from a JSON string
repos_create_or_update_file_contents_request_instance = ReposCreateOrUpdateFileContentsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateFileContentsRequest.to_json())

# convert the object into a dict
repos_create_or_update_file_contents_request_dict = repos_create_or_update_file_contents_request_instance.to_dict()
# create an instance of ReposCreateOrUpdateFileContentsRequest from a dict
repos_create_or_update_file_contents_request_from_dict = ReposCreateOrUpdateFileContentsRequest.from_dict(repos_create_or_update_file_contents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


