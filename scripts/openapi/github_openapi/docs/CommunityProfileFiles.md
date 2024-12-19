# CommunityProfileFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_of_conduct** | [**NullableCodeOfConductSimple**](NullableCodeOfConductSimple.md) |  | 
**code_of_conduct_file** | [**NullableCommunityHealthFile**](NullableCommunityHealthFile.md) |  | 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 
**contributing** | [**NullableCommunityHealthFile**](NullableCommunityHealthFile.md) |  | 
**readme** | [**NullableCommunityHealthFile**](NullableCommunityHealthFile.md) |  | 
**issue_template** | [**NullableCommunityHealthFile**](NullableCommunityHealthFile.md) |  | 
**pull_request_template** | [**NullableCommunityHealthFile**](NullableCommunityHealthFile.md) |  | 

## Example

```python
from github_openapi.models.community_profile_files import CommunityProfileFiles

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityProfileFiles from a JSON string
community_profile_files_instance = CommunityProfileFiles.from_json(json)
# print the JSON string representation of the object
print(CommunityProfileFiles.to_json())

# convert the object into a dict
community_profile_files_dict = community_profile_files_instance.to_dict()
# create an instance of CommunityProfileFiles from a dict
community_profile_files_from_dict = CommunityProfileFiles.from_dict(community_profile_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


