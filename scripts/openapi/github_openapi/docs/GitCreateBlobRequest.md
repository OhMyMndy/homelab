# GitCreateBlobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The new blob&#39;s content. | 
**encoding** | **str** | The encoding used for &#x60;content&#x60;. Currently, &#x60;\&quot;utf-8\&quot;&#x60; and &#x60;\&quot;base64\&quot;&#x60; are supported. | [optional] [default to 'utf-8']

## Example

```python
from github_openapi.models.git_create_blob_request import GitCreateBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateBlobRequest from a JSON string
git_create_blob_request_instance = GitCreateBlobRequest.from_json(json)
# print the JSON string representation of the object
print(GitCreateBlobRequest.to_json())

# convert the object into a dict
git_create_blob_request_dict = git_create_blob_request_instance.to_dict()
# create an instance of GitCreateBlobRequest from a dict
git_create_blob_request_from_dict = GitCreateBlobRequest.from_dict(git_create_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


