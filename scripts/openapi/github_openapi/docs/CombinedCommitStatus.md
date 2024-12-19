# CombinedCommitStatus

Combined Commit Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**statuses** | [**List[SimpleCommitStatus]**](SimpleCommitStatus.md) |  | 
**sha** | **str** |  | 
**total_count** | **int** |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**commit_url** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.combined_commit_status import CombinedCommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedCommitStatus from a JSON string
combined_commit_status_instance = CombinedCommitStatus.from_json(json)
# print the JSON string representation of the object
print(CombinedCommitStatus.to_json())

# convert the object into a dict
combined_commit_status_dict = combined_commit_status_instance.to_dict()
# create an instance of CombinedCommitStatus from a dict
combined_commit_status_from_dict = CombinedCommitStatus.from_dict(combined_commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


