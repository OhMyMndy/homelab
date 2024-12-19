# BillingUsageReportUsageItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date of the usage line item. | 
**product** | **str** | Product name. | 
**sku** | **str** | SKU name. | 
**quantity** | **int** | Quantity of the usage line item. | 
**unit_type** | **str** | Unit type of the usage line item. | 
**price_per_unit** | **float** | Price per unit of the usage line item. | 
**gross_amount** | **float** | Gross amount of the usage line item. | 
**discount_amount** | **float** | Discount amount of the usage line item. | 
**net_amount** | **float** | Net amount of the usage line item. | 
**organization_name** | **str** | Name of the organization. | 
**repository_name** | **str** | Name of the repository. | [optional] 

## Example

```python
from github_openapi.models.billing_usage_report_usage_items_inner import BillingUsageReportUsageItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillingUsageReportUsageItemsInner from a JSON string
billing_usage_report_usage_items_inner_instance = BillingUsageReportUsageItemsInner.from_json(json)
# print the JSON string representation of the object
print(BillingUsageReportUsageItemsInner.to_json())

# convert the object into a dict
billing_usage_report_usage_items_inner_dict = billing_usage_report_usage_items_inner_instance.to_dict()
# create an instance of BillingUsageReportUsageItemsInner from a dict
billing_usage_report_usage_items_inner_from_dict = BillingUsageReportUsageItemsInner.from_dict(billing_usage_report_usage_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


