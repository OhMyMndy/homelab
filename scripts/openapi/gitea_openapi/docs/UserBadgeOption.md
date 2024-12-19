# UserBadgeOption

UserBadgeOption options for link between users and badges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_slugs** | **List[str]** |  | [optional] 

## Example

```python
from gitea_openapi.models.user_badge_option import UserBadgeOption

# TODO update the JSON string below
json = "{}"
# create an instance of UserBadgeOption from a JSON string
user_badge_option_instance = UserBadgeOption.from_json(json)
# print the JSON string representation of the object
print(UserBadgeOption.to_json())

# convert the object into a dict
user_badge_option_dict = user_badge_option_instance.to_dict()
# create an instance of UserBadgeOption from a dict
user_badge_option_from_dict = UserBadgeOption.from_dict(user_badge_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


