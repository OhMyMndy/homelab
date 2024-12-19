# CheckRun

A check performed on the code of a given code change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the check. | 
**head_sha** | **str** | The SHA of the commit that is being checked. | 
**node_id** | **str** |  | 
**external_id** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**details_url** | **str** |  | 
**status** | **str** | The phase of the lifecycle that the check is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check runs. | 
**conclusion** | **str** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**output** | [**CheckRunOutput**](CheckRunOutput.md) |  | 
**name** | **str** | The name of the check. | 
**check_suite** | [**CheckRunCheckSuite**](CheckRunCheckSuite.md) |  | 
**app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**pull_requests** | [**List[PullRequestMinimal]**](PullRequestMinimal.md) | Pull requests that are open with a &#x60;head_sha&#x60; or &#x60;head_branch&#x60; that matches the check. The returned pull requests do not necessarily indicate pull requests that triggered the check. | 
**deployment** | [**DeploymentSimple**](DeploymentSimple.md) |  | [optional] 

## Example

```python
from github_openapi.models.check_run import CheckRun

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRun from a JSON string
check_run_instance = CheckRun.from_json(json)
# print the JSON string representation of the object
print(CheckRun.to_json())

# convert the object into a dict
check_run_dict = check_run_instance.to_dict()
# create an instance of CheckRun from a dict
check_run_from_dict = CheckRun.from_dict(check_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


