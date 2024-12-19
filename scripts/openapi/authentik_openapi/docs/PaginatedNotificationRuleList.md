# PaginatedNotificationRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[NotificationRule]**](NotificationRule.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_notification_rule_list import PaginatedNotificationRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationRuleList from a JSON string
paginated_notification_rule_list_instance = PaginatedNotificationRuleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNotificationRuleList.to_json())

# convert the object into a dict
paginated_notification_rule_list_dict = paginated_notification_rule_list_instance.to_dict()
# create an instance of PaginatedNotificationRuleList from a dict
paginated_notification_rule_list_from_dict = PaginatedNotificationRuleList.from_dict(paginated_notification_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


