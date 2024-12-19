# ReposGenerateReleaseNotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** | The tag name for the release. This can be an existing tag or a new one. | 
**target_commitish** | **str** | Specifies the commitish value that will be the target for the release&#39;s tag. Required if the supplied tag_name does not reference an existing tag. Ignored if the tag_name already exists. | [optional] 
**previous_tag_name** | **str** | The name of the previous tag to use as the starting point for the release notes. Use to manually specify the range for the set of changes considered as part this release. | [optional] 
**configuration_file_path** | **str** | Specifies a path to a file in the repository containing configuration settings used for generating the release notes. If unspecified, the configuration file located in the repository at &#39;.github/release.yml&#39; or &#39;.github/release.yaml&#39; will be used. If that is not present, the default configuration will be used. | [optional] 

## Example

```python
from github_openapi.models.repos_generate_release_notes_request import ReposGenerateReleaseNotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposGenerateReleaseNotesRequest from a JSON string
repos_generate_release_notes_request_instance = ReposGenerateReleaseNotesRequest.from_json(json)
# print the JSON string representation of the object
print(ReposGenerateReleaseNotesRequest.to_json())

# convert the object into a dict
repos_generate_release_notes_request_dict = repos_generate_release_notes_request_instance.to_dict()
# create an instance of ReposGenerateReleaseNotesRequest from a dict
repos_generate_release_notes_request_from_dict = ReposGenerateReleaseNotesRequest.from_dict(repos_generate_release_notes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


