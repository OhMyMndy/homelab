# GitTagTagger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from github_openapi.models.git_tag_tagger import GitTagTagger

# TODO update the JSON string below
json = "{}"
# create an instance of GitTagTagger from a JSON string
git_tag_tagger_instance = GitTagTagger.from_json(json)
# print the JSON string representation of the object
print(GitTagTagger.to_json())

# convert the object into a dict
git_tag_tagger_dict = git_tag_tagger_instance.to_dict()
# create an instance of GitTagTagger from a dict
git_tag_tagger_from_dict = GitTagTagger.from_dict(git_tag_tagger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


