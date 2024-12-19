# ReposDeleteFileRequestAuthor

object containing information about the author.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author (or committer) of the commit | [optional] 
**email** | **str** | The email of the author (or committer) of the commit | [optional] 

## Example

```python
from github_openapi.models.repos_delete_file_request_author import ReposDeleteFileRequestAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of ReposDeleteFileRequestAuthor from a JSON string
repos_delete_file_request_author_instance = ReposDeleteFileRequestAuthor.from_json(json)
# print the JSON string representation of the object
print(ReposDeleteFileRequestAuthor.to_json())

# convert the object into a dict
repos_delete_file_request_author_dict = repos_delete_file_request_author_instance.to_dict()
# create an instance of ReposDeleteFileRequestAuthor from a dict
repos_delete_file_request_author_from_dict = ReposDeleteFileRequestAuthor.from_dict(repos_delete_file_request_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


