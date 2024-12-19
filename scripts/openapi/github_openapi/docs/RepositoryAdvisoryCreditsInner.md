# RepositoryAdvisoryCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | The username of the user credited. | [optional] 
**type** | [**SecurityAdvisoryCreditTypes**](SecurityAdvisoryCreditTypes.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_advisory_credits_inner import RepositoryAdvisoryCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCreditsInner from a JSON string
repository_advisory_credits_inner_instance = RepositoryAdvisoryCreditsInner.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCreditsInner.to_json())

# convert the object into a dict
repository_advisory_credits_inner_dict = repository_advisory_credits_inner_instance.to_dict()
# create an instance of RepositoryAdvisoryCreditsInner from a dict
repository_advisory_credits_inner_from_dict = RepositoryAdvisoryCreditsInner.from_dict(repository_advisory_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


