# OrderCloud.UserGroupApi

All URIs are relative to *https://api.ordercloud.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserGroupApi.md#create) | **POST** /buyers/{buyerID}/usergroups | 
[**delete**](UserGroupApi.md#delete) | **DELETE** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**delete_user_assignment**](UserGroupApi.md#delete_user_assignment) | **DELETE** /buyers/{buyerID}/usergroups/{userGroupID}/assignments/{userID} | 
[**get**](UserGroupApi.md#get) | **GET** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**list**](UserGroupApi.md#list) | **GET** /buyers/{buyerID}/usergroups | 
[**list_user_assignments**](UserGroupApi.md#list_user_assignments) | **GET** /buyers/{buyerID}/usergroups/assignments | 
[**patch**](UserGroupApi.md#patch) | **PATCH** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**save**](UserGroupApi.md#save) | **PUT** /buyers/{buyerID}/usergroups/{userGroupID} | 
[**save_user_assignment**](UserGroupApi.md#save_user_assignment) | **POST** /buyers/{buyerID}/usergroups/assignments | 


# **create**
> UserGroup create(buyer_id, user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.create(buyer_id, user_group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(buyer_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    UserGroupApi.delete(buyer_id, user_group_id)
except ApiException as e:
    print("Exception when calling UserGroupApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_assignment**
> delete_user_assignment(buyer_id, user_group_id, user_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_id = 'user_id_example' # str | ID of the user.

try: 
    UserGroupApi.delete_user_assignment(buyer_id, user_group_id, user_id)
except ApiException as e:
    print("Exception when calling UserGroupApi->delete_user_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 
 **user_id** | **str**| ID of the user. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> UserGroup get(buyer_id, user_group_id)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.

try: 
    response = UserGroupApi.get(buyer_id, user_group_id)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListUserGroup list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
search = 'search_example' # str | Word or phrase to search for. (optional)
search_on = 'search_on_example' # str | Comma-delimited list of fields to search on. (optional)
sort_by = 'sort_by_example' # str | Comma-delimited list of fields to sort by. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)
filters = {'key': 'filters_example'} # dict(str, str) | Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???' (optional)

try: 
    response = UserGroupApi.list(buyer_id, search=search, search_on=search_on, sort_by=sort_by, page=page, page_size=page_size, filters=filters)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **search** | **str**| Word or phrase to search for. | [optional] 
 **search_on** | **str**| Comma-delimited list of fields to search on. | [optional] 
 **sort_by** | **str**| Comma-delimited list of fields to sort by. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 
 **filters** | [**dict(str, str)**](str.md)| Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or &#39;xp.???&#39; | [optional] 

### Return type

[**ListUserGroup**](ListUserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_assignments**
> ListUserGroupAssignment list_user_assignments(buyer_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group. (optional)
user_id = 'user_id_example' # str | ID of the user. (optional)
page = 56 # int | Page of results to return. Default: 1 (optional)
page_size = 56 # int | Number of results to return per page. Default: 20, max: 100. (optional)

try: 
    response = UserGroupApi.list_user_assignments(buyer_id, user_group_id=user_group_id, user_id=user_id, page=page, page_size=page_size)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->list_user_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | [optional] 
 **user_id** | **str**| ID of the user. | [optional] 
 **page** | **int**| Page of results to return. Default: 1 | [optional] 
 **page_size** | **int**| Number of results to return per page. Default: 20, max: 100. | [optional] 

### Return type

[**ListUserGroupAssignment**](ListUserGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> UserGroup patch(buyer_id, user_group_id, partial_user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
partial_user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.patch(buyer_id, user_group_id, partial_user_group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 
 **partial_user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save**
> UserGroup save(buyer_id, user_group_id, user_group)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_id = 'user_group_id_example' # str | ID of the user group.
user_group = OrderCloud.UserGroup() # UserGroup | 

try: 
    response = UserGroupApi.save(buyer_id, user_group_id, user_group)
    print(response)
except ApiException as e:
    print("Exception when calling UserGroupApi->save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_id** | **str**| ID of the user group. | 
 **user_group** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_assignment**
> save_user_assignment(buyer_id, user_group_assignment)



### Example 
```python
import OrderCloud
from OrderCloud.rest import ApiException
# Assuming you've already acquired and set an access_token (see the Getting Started guide)

# create an instance of the API class
UserGroupApi = OrderCloud.UserGroupApi
buyer_id = 'buyer_id_example' # str | ID of the buyer.
user_group_assignment = OrderCloud.UserGroupAssignment() # UserGroupAssignment | 

try: 
    UserGroupApi.save_user_assignment(buyer_id, user_group_assignment)
except ApiException as e:
    print("Exception when calling UserGroupApi->save_user_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| ID of the buyer. | 
 **user_group_assignment** | [**UserGroupAssignment**](UserGroupAssignment.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/plain; charset=utf-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

