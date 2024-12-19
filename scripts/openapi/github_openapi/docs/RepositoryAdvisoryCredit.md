# RepositoryAdvisoryCredit

A credit given to a user for a repository security advisory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**type** | [**SecurityAdvisoryCreditTypes**](SecurityAdvisoryCreditTypes.md) |  | 
**state** | **str** | The state of the user&#39;s acceptance of the credit. | 

## Example

```python
from github_openapi.models.repository_advisory_credit import RepositoryAdvisoryCredit

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisoryCredit from a JSON string
repository_advisory_credit_instance = RepositoryAdvisoryCredit.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisoryCredit.to_json())

# convert the object into a dict
repository_advisory_credit_dict = repository_advisory_credit_instance.to_dict()
# create an instance of RepositoryAdvisoryCredit from a dict
repository_advisory_credit_from_dict = RepositoryAdvisoryCredit.from_dict(repository_advisory_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


