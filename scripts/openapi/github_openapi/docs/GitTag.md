# GitTag

Metadata for a Git tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 
**tag** | **str** | Name of the tag | 
**sha** | **str** |  | 
**url** | **str** | URL for the tag | 
**message** | **str** | Message describing the purpose of the tag | 
**tagger** | [**GitTagTagger**](GitTagTagger.md) |  | 
**object** | [**GitTagObject**](GitTagObject.md) |  | 
**verification** | [**Verification**](Verification.md) |  | [optional] 

## Example

```python
from github_openapi.models.git_tag import GitTag

# TODO update the JSON string below
json = "{}"
# create an instance of GitTag from a JSON string
git_tag_instance = GitTag.from_json(json)
# print the JSON string representation of the object
print(GitTag.to_json())

# convert the object into a dict
git_tag_dict = git_tag_instance.to_dict()
# create an instance of GitTag from a dict
git_tag_from_dict = GitTag.from_dict(git_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


