# OrgsReviewPatGrantRequestsInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pat_request_ids** | **List[int]** | Unique identifiers of the requests for access via fine-grained personal access token. Must be formed of between 1 and 100 &#x60;pat_request_id&#x60; values. | [optional] 
**action** | **str** | Action to apply to the requests. | 
**reason** | **str** | Reason for approving or denying the requests. Max 1024 characters. | [optional] 

## Example

```python
from github_openapi.models.orgs_review_pat_grant_requests_in_bulk_request import OrgsReviewPatGrantRequestsInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsReviewPatGrantRequestsInBulkRequest from a JSON string
orgs_review_pat_grant_requests_in_bulk_request_instance = OrgsReviewPatGrantRequestsInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsReviewPatGrantRequestsInBulkRequest.to_json())

# convert the object into a dict
orgs_review_pat_grant_requests_in_bulk_request_dict = orgs_review_pat_grant_requests_in_bulk_request_instance.to_dict()
# create an instance of OrgsReviewPatGrantRequestsInBulkRequest from a dict
orgs_review_pat_grant_requests_in_bulk_request_from_dict = OrgsReviewPatGrantRequestsInBulkRequest.from_dict(orgs_review_pat_grant_requests_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


