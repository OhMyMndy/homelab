# PaginatedNotificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Notification]**](Notification.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_notification_list import PaginatedNotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationList from a JSON string
paginated_notification_list_instance = PaginatedNotificationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationList.to_json())

# convert the object into a dict
paginated_notification_list_dict = paginated_notification_list_instance.to_dict()
# create an instance of PaginatedNotificationList from a dict
paginated_notification_list_from_dict = PaginatedNotificationList.from_dict(paginated_notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


