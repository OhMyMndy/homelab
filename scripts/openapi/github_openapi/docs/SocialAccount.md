# SocialAccount

Social media account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.social_account import SocialAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccount from a JSON string
social_account_instance = SocialAccount.from_json(json)
# print the JSON string representation of the object
print(SocialAccount.to_json())

# convert the object into a dict
social_account_dict = social_account_instance.to_dict()
# create an instance of SocialAccount from a dict
social_account_from_dict = SocialAccount.from_dict(social_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


