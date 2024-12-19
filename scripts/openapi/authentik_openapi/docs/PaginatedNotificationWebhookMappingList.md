# PaginatedNotificationWebhookMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[NotificationWebhookMapping]**](NotificationWebhookMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationWebhookMappingList from a JSON string
paginated_notification_webhook_mapping_list_instance = PaginatedNotificationWebhookMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationWebhookMappingList.to_json())

# convert the object into a dict
paginated_notification_webhook_mapping_list_dict = paginated_notification_webhook_mapping_list_instance.to_dict()
# create an instance of PaginatedNotificationWebhookMappingList from a dict
paginated_notification_webhook_mapping_list_from_dict = PaginatedNotificationWebhookMappingList.from_dict(paginated_notification_webhook_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


