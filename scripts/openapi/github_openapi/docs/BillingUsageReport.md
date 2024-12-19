# BillingUsageReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_items** | [**List[BillingUsageReportUsageItemsInner]**](BillingUsageReportUsageItemsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.billing_usage_report import BillingUsageReport

# TODO update the JSON string below
json = "{}"
# create an instance of BillingUsageReport from a JSON string
billing_usage_report_instance = BillingUsageReport.from_json(json)
# print the JSON string representation of the object
print(BillingUsageReport.to_json())

# convert the object into a dict
billing_usage_report_dict = billing_usage_report_instance.to_dict()
# create an instance of BillingUsageReport from a dict
billing_usage_report_from_dict = BillingUsageReport.from_dict(billing_usage_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


