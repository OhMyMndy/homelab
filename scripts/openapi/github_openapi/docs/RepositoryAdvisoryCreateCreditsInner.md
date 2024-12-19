# RepositoryAdvisoryCreateCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | The username of the user credited. | 
**type** | [**SecurityAdvisoryCreditTypes**](SecurityAdvisoryCreditTypes.md) |  | 

## Example

```python
from github_openapi.models.repository_advisory_create_credits_inner import RepositoryAdvisoryCreateCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCreateCreditsInner from a JSON string
repository_advisory_create_credits_inner_instance = RepositoryAdvisoryCreateCreditsInner.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCreateCreditsInner.to_json())

# convert the object into a dict
repository_advisory_create_credits_inner_dict = repository_advisory_create_credits_inner_instance.to_dict()
# create an instance of RepositoryAdvisoryCreateCreditsInner from a dict
repository_advisory_create_credits_inner_from_dict = RepositoryAdvisoryCreateCreditsInner.from_dict(repository_advisory_create_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


