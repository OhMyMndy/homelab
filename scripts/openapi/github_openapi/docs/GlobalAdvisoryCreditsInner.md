# GlobalAdvisoryCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**type** | [**SecurityAdvisoryCreditTypes**](SecurityAdvisoryCreditTypes.md) |  | 

## Example

```python
from github_openapi.models.global_advisory_credits_inner import GlobalAdvisoryCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAdvisoryCreditsInner from a JSON string
global_advisory_credits_inner_instance = GlobalAdvisoryCreditsInner.from_json(json)
# print the JSON string representation of the object
print(GlobalAdvisoryCreditsInner.to_json())

# convert the object into a dict
global_advisory_credits_inner_dict = global_advisory_credits_inner_instance.to_dict()
# create an instance of GlobalAdvisoryCreditsInner from a dict
global_advisory_credits_inner_from_dict = GlobalAdvisoryCreditsInner.from_dict(global_advisory_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


