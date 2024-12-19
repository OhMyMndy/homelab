# ChecksCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the check. For example, \&quot;code-coverage\&quot;. | 
**head_sha** | **str** | The SHA of the commit. | 
**details_url** | **str** | The URL of the integrator&#39;s site that has the full details of the check. If the integrator does not provide this, then the homepage of the GitHub app is used. | [optional] 
**external_id** | **str** | A reference for the run on the integrator&#39;s system. | [optional] 
**status** | **str** | The current status of the check run. Only GitHub Actions can set a status of &#x60;waiting&#x60;, &#x60;pending&#x60;, or &#x60;requested&#x60;. | [optional] [default to 'queued']
**started_at** | **datetime** | The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**conclusion** | **str** | **Required if you provide &#x60;completed_at&#x60; or a &#x60;status&#x60; of &#x60;completed&#x60;**. The final conclusion of the check.  **Note:** Providing &#x60;conclusion&#x60; will automatically set the &#x60;status&#x60; parameter to &#x60;completed&#x60;. You cannot change a check run conclusion to &#x60;stale&#x60;, only GitHub can set this. | [optional] 
**completed_at** | **datetime** | The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**output** | [**ChecksCreateRequestOutput**](ChecksCreateRequestOutput.md) |  | [optional] 
**actions** | [**List[ChecksCreateRequestActionsInner]**](ChecksCreateRequestActionsInner.md) | Displays a button on GitHub that can be clicked to alert your app to do additional tasks. For example, a code linting app can display a button that automatically fixes detected errors. The button created in this object is displayed after the check run completes. When a user clicks the button, GitHub sends the [&#x60;check_run.requested_action&#x60; webhook](https://docs.github.com/webhooks/event-payloads/#check_run) to your app. Each action includes a &#x60;label&#x60;, &#x60;identifier&#x60; and &#x60;description&#x60;. A maximum of three actions are accepted. To learn more about check runs and requested actions, see \&quot;[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions).\&quot; | [optional] 

## Example

```python
from github_openapi.models.checks_create_request import ChecksCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateRequest from a JSON string
checks_create_request_instance = ChecksCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateRequest.to_json())

# convert the object into a dict
checks_create_request_dict = checks_create_request_instance.to_dict()
# create an instance of ChecksCreateRequest from a dict
checks_create_request_from_dict = ChecksCreateRequest.from_dict(checks_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


