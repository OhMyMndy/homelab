# ReleaseNotesContent

Generated name and body describing a release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The generated name of the release | 
**body** | **str** | The generated body describing the contents of the release supporting markdown formatting | 

## Example

```python
from github_openapi.models.release_notes_content import ReleaseNotesContent

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseNotesContent from a JSON string
release_notes_content_instance = ReleaseNotesContent.from_json(json)
# print the JSON string representation of the object
print(ReleaseNotesContent.to_json())

# convert the object into a dict
release_notes_content_dict = release_notes_content_instance.to_dict()
# create an instance of ReleaseNotesContent from a dict
release_notes_content_from_dict = ReleaseNotesContent.from_dict(release_notes_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


