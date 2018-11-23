## HILU proxy API

HILU proxy API can be used to make transactions to the HILU payments accounting system. The proxy API is a convenience wrapper on top of the actual HILU API, which requires a more complex authentication method.

The API is available at two urls: [https://gnyxeovy1m.execute-api.eu-west-1.amazonaws.com/junction-test/api/pos/v1/transaction](https://gnyxeovy1m.execute-api.eu-west-1.amazonaws.com/junction-test/api/pos/v1/transaction), which can be used to make purchases in the API, and the same URL but `/load` appended to the end can be used to add funds to the account. NOTE! The API is quite slow to respond due to the nature of the intermediate proxy component.

Below is a model json body of the POST request that can be sent to the API:

```javascript
{
    "tokenUid":"UIDString",
    "deviceId":"1",
    "amount": 0
}
```

