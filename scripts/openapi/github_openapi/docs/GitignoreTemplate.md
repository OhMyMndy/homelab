# GitignoreTemplate

Gitignore Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from github_openapi.models.gitignore_template import GitignoreTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GitignoreTemplate from a JSON string
gitignore_template_instance = GitignoreTemplate.from_json(json)
# print the JSON string representation of the object
print(GitignoreTemplate.to_json())

# convert the object into a dict
gitignore_template_dict = gitignore_template_instance.to_dict()
# create an instance of GitignoreTemplate from a dict
gitignore_template_from_dict = GitignoreTemplate.from_dict(gitignore_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


