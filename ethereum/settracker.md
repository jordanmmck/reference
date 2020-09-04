# SetTracker

unitShares: The quantity of the currentSet tokens that corresponds to one Rebalancing Set token.
The unitShares parameter is initiated in the constructor and updated after each rebalance.

naturalUnit: The natural unit is an integer value that represents the least divisible issuance value of
the Rebalancing Set.

To solve this issue, Set introduces the concept of natural unit, which is the atomic, least divisible unit of a
Set that can be issued or redeemed. Set creation enforces that the natural unit is larger than the transferable
unit of the token with the smallest decimals place.

```json
{
    "id": "ethrsiapy",
    "price_usd": "227.13",
    "market_cap": "2985600.23",
    "natural_unit": "1000000",
    "unit_shares":   "557211",
    "components": [
    {
        "symbol": "cUSDC",
        "quantity": "0",
        "units": "0"
    },
    {
        "symbol": "WETH",
        "quantity": "1.168556",
        "units": "2097152"
    }
    ]
},
{
    "id": "ethmacoapy",
    "price_usd": "431.75",
    "market_cap": "2898122.91",
    "natural_unit": "1000000",
    "unit_shares":  "1059201",
    "components": [
    {
        "symbol": "cUSDC",
        "quantity": "0",
        "units": "0"
    },
    {
        "symbol": "WETH",
        "quantity": "2.221305",
        "units": "2097152"
    }
    ]
},
{
    "id": "btceth7525",
    "price_usd": "139.25",
    "market_cap": "71710.32",
    "natural_unit": "1000000",
    "unit_shares":     "4368",
    "components": [
    {
        "symbol": "WETH",
        "quantity": "0.207324",
        "units": "474643755238"
    },
    {
        "symbol": "WBTC",
        "quantity": "0.013104",
        "units": "3"
    }
    ]
},
```

quantity _asset + quantity_ asset = tokenset unit
