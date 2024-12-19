# GitCreateTagRequestTagger

An object with information about the individual creating the tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author of the tag | 
**email** | **str** | The email of the author of the tag | 
**var_date** | **datetime** | When this object was tagged. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

## Example

```python
from github_openapi.models.git_create_tag_request_tagger import GitCreateTagRequestTagger

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateTagRequestTagger from a JSON string
git_create_tag_request_tagger_instance = GitCreateTagRequestTagger.from_json(json)
# print the JSON string representation of the object
print(GitCreateTagRequestTagger.to_json())

# convert the object into a dict
git_create_tag_request_tagger_dict = git_create_tag_request_tagger_instance.to_dict()
# create an instance of GitCreateTagRequestTagger from a dict
git_create_tag_request_tagger_from_dict = GitCreateTagRequestTagger.from_dict(git_create_tag_request_tagger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


