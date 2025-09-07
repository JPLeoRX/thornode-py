# thornode-py

## Introduction
Python client for THORNode API

THORChain has several APIs - Midgard, THORNode, Cosmos RPC, CometBFT RPC. This python client focuses on interactions with the basic THORNode API.

[API Swagger Docs](https://thornode.ninerealms.com/thorchain/doc)

## Progress

Below is the implementation status of the major sections of THORNode API in this Python client:

| Section             | Implemented | Notes                        |
|---------------------|-------------|------------------------------|
| Auth                | ✅           |                              |
| Bank                | ✅           |                              |
| Health              | ✅           |                              |
| Pools               | ✅           |                              |
| Pool Slip           | ✅           |                              |
| Liquidity Providers | ✅          |                              |
| Codes               |             | Not supported in current API |
| Oracle              |             | Not supported in current API |
| TCY Stakers         | ✅          |                              |
| TCY Claimers        | ✅          |                              |
| RUNE Pool           | ✅          |                              |
| Savers              | ✅          |                              |
| Borrowers           | ✅          |                              |
| Transactions        | ✅          |                              |
| Nodes               | ✅          |                              |
| Vaults              | ✅          |                              |
| Network             | ✅          | Partially implemented        |
| Streaming Swap      | ✅          |                              |
| Clout               |             |                              |
| Trade Unit          | ✅          |                              |
| Trade Account       |             |                              |
| Secured Assets      | ✅          |                              |
| Swap                | ✅          | Partially implemented        |
| Queue               |             |                              |
| TSS                 |             |                              |
| Thornames           | ✅           |                              |
| Mimir               |             |                              |
| Quote               |             |                              |
| Invariants          |             |                              |
| Block               |             |                              |
| Export              |             | Not supported in current API |

If you notice any discrepancy or want a section prioritized, please open an issue or PR.

## Usage