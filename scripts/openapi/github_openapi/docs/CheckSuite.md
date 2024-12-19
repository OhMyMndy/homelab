# CheckSuite

A suite of checks performed on the code of a given code change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**head_branch** | **str** |  | 
**head_sha** | **str** | The SHA of the head commit that is being checked. | 
**status** | **str** | The phase of the lifecycle that the check suite is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check suites. | 
**conclusion** | **str** |  | 
**url** | **str** |  | 
**before** | **str** |  | 
**after** | **str** |  | 
**pull_requests** | [**List[PullRequestMinimal]**](PullRequestMinimal.md) |  | 
**app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**head_commit** | [**SimpleCommit**](SimpleCommit.md) |  | 
**latest_check_runs_count** | **int** |  | 
**check_runs_url** | **str** |  | 
**rerequestable** | **bool** |  | [optional] 
**runs_rerequestable** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.check_suite import CheckSuite

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuite from a JSON string
check_suite_instance = CheckSuite.from_json(json)
# print the JSON string representation of the object
print(CheckSuite.to_json())

# convert the object into a dict
check_suite_dict = check_suite_instance.to_dict()
# create an instance of CheckSuite from a dict
check_suite_from_dict = CheckSuite.from_dict(check_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


