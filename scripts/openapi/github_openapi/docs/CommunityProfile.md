# CommunityProfile

Community Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_percentage** | **int** |  | 
**description** | **str** |  | 
**documentation** | **str** |  | 
**files** | [**CommunityProfileFiles**](CommunityProfileFiles.md) |  | 
**updated_at** | **datetime** |  | 
**content_reports_enabled** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.community_profile import CommunityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityProfile from a JSON string
community_profile_instance = CommunityProfile.from_json(json)
# print the JSON string representation of the object
print(CommunityProfile.to_json())

# convert the object into a dict
community_profile_dict = community_profile_instance.to_dict()
# create an instance of CommunityProfile from a dict
community_profile_from_dict = CommunityProfile.from_dict(community_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


