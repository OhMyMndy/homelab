# WebhookCheckSuiteRequestedCheckSuite

The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** |  | 
**app** | [**App3**](App3.md) |  | 
**before** | **str** |  | 
**check_runs_url** | **str** |  | 
**conclusion** | **str** | The summary conclusion for all check runs that are part of the check suite. This value will be &#x60;null&#x60; until the check run has completed. | 
**created_at** | **datetime** |  | 
**head_branch** | **str** | The head branch name the changes are on. | 
**head_commit** | [**SimpleCommit**](SimpleCommit.md) |  | 
**head_sha** | **str** | The SHA of the head commit that is being checked. | 
**id** | **int** |  | 
**latest_check_runs_count** | **int** |  | 
**node_id** | **str** |  | 
**pull_requests** | [**List[CheckRunPullRequest]**](CheckRunPullRequest.md) | An array of pull requests that match this check suite. A pull request matches a check suite if they have the same &#x60;head_sha&#x60; and &#x60;head_branch&#x60;. When the check suite&#39;s &#x60;head_branch&#x60; is in a forked repository it will be &#x60;null&#x60; and the &#x60;pull_requests&#x60; array will be empty. | 
**rerequestable** | **bool** |  | [optional] 
**runs_rerequestable** | **bool** |  | [optional] 
**status** | **str** | The summary status for all check runs that are part of the check suite. Can be &#x60;requested&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;. | 
**updated_at** | **datetime** |  | 
**url** | **str** | URL that points to the check suite API resource. | 

## Example

```python
from github_openapi.models.webhook_check_suite_requested_check_suite import WebhookCheckSuiteRequestedCheckSuite

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckSuiteRequestedCheckSuite from a JSON string
webhook_check_suite_requested_check_suite_instance = WebhookCheckSuiteRequestedCheckSuite.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckSuiteRequestedCheckSuite.to_json())

# convert the object into a dict
webhook_check_suite_requested_check_suite_dict = webhook_check_suite_requested_check_suite_instance.to_dict()
# create an instance of WebhookCheckSuiteRequestedCheckSuite from a dict
webhook_check_suite_requested_check_suite_from_dict = WebhookCheckSuiteRequestedCheckSuite.from_dict(webhook_check_suite_requested_check_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


