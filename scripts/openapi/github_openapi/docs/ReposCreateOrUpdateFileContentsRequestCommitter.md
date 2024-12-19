# ReposCreateOrUpdateFileContentsRequestCommitter

The person that committed the file. Default: the authenticated user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author or committer of the commit. You&#39;ll receive a &#x60;422&#x60; status code if &#x60;name&#x60; is omitted. | 
**email** | **str** | The email of the author or committer of the commit. You&#39;ll receive a &#x60;422&#x60; status code if &#x60;email&#x60; is omitted. | 
**var_date** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_or_update_file_contents_request_committer import ReposCreateOrUpdateFileContentsRequestCommitter

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateFileContentsRequestCommitter from a JSON string
repos_create_or_update_file_contents_request_committer_instance = ReposCreateOrUpdateFileContentsRequestCommitter.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateFileContentsRequestCommitter.to_json())

# convert the object into a dict
repos_create_or_update_file_contents_request_committer_dict = repos_create_or_update_file_contents_request_committer_instance.to_dict()
# create an instance of ReposCreateOrUpdateFileContentsRequestCommitter from a dict
repos_create_or_update_file_contents_request_committer_from_dict = ReposCreateOrUpdateFileContentsRequestCommitter.from_dict(repos_create_or_update_file_contents_request_committer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


