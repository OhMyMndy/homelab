# RepositoryAdvisorySubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Whether a private vulnerability report was accepted by the repository&#39;s administrators. | [readonly] 

## Example

```python
from github_openapi.models.repository_advisory_submission import RepositoryAdvisorySubmission

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAdvisorySubmission from a JSON string
repository_advisory_submission_instance = RepositoryAdvisorySubmission.from_json(json)
# print the JSON string representation of the object
print(RepositoryAdvisorySubmission.to_json())

# convert the object into a dict
repository_advisory_submission_dict = repository_advisory_submission_instance.to_dict()
# create an instance of RepositoryAdvisorySubmission from a dict
repository_advisory_submission_from_dict = RepositoryAdvisorySubmission.from_dict(repository_advisory_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


