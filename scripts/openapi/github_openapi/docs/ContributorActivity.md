# ContributorActivity

Contributor Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**total** | **int** |  | 
**weeks** | [**List[ContributorActivityWeeksInner]**](ContributorActivityWeeksInner.md) |  | 

## Example

```python
from github_openapi.models.contributor_activity import ContributorActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ContributorActivity from a JSON string
contributor_activity_instance = ContributorActivity.from_json(json)
# print the JSON string representation of the object
print(ContributorActivity.to_json())

# convert the object into a dict
contributor_activity_dict = contributor_activity_instance.to_dict()
# create an instance of ContributorActivity from a dict
contributor_activity_from_dict = ContributorActivity.from_dict(contributor_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


