# ActivityMarkRepoNotificationsAsReadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_read_at** | **datetime** | Describes the last point that notifications were checked. Anything updated since this time will not be marked as read. If you omit this parameter, all notifications are marked as read. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. Default: The current timestamp. | [optional] 

## Example

```python
from github_openapi.models.activity_mark_repo_notifications_as_read_request import ActivityMarkRepoNotificationsAsReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityMarkRepoNotificationsAsReadRequest from a JSON string
activity_mark_repo_notifications_as_read_request_instance = ActivityMarkRepoNotificationsAsReadRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityMarkRepoNotificationsAsReadRequest.to_json())

# convert the object into a dict
activity_mark_repo_notifications_as_read_request_dict = activity_mark_repo_notifications_as_read_request_instance.to_dict()
# create an instance of ActivityMarkRepoNotificationsAsReadRequest from a dict
activity_mark_repo_notifications_as_read_request_from_dict = ActivityMarkRepoNotificationsAsReadRequest.from_dict(activity_mark_repo_notifications_as_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


