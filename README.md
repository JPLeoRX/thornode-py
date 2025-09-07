# thornode-py

# Introduction
Python client for THORNode API

THORChain has several APIs - Midgard, THORNode, Cosmos RPC, CometBFT RPC. This python client focuses on interactions with the basic THORNode API.

Built for API version 3.10.0.

[API Swagger Docs](https://thornode.ninerealms.com/thorchain/doc)

# Progress

Below is the implementation status of the major sections of THORNode API in this Python client:

| Section             | Implemented | Notes                        |
|---------------------|-----------|------------------------------|
| Auth                | ✅         |                              |
| Bank                | ✅         |                              |
| Health              | ✅         |                              |
| Pools               | ✅         |                              |
| Pool Slip           | ✅         |                              |
| Liquidity Providers | ✅        |                              |
| Codes               |           | Not supported in current API |
| Oracle              |           | Not supported in current API |
| TCY Stakers         | ✅        |                              |
| TCY Claimers        | ✅        |                              |
| RUNE Pool           | ✅        |                              |
| Savers              | ✅        |                              |
| Borrowers           | ✅        |                              |
| Transactions        | ✅        |                              |
| Nodes               | ✅        |                              |
| Vaults              | ✅        |                              |
| Network             |          | Partially implemented        |
| Streaming Swap      | ✅        |                              |
| Clout               |           |                              |
| Trade Unit          | ✅        |                              |
| Trade Account       |           |                              |
| Secured Assets      | ✅        |                              |
| Swap                | ✅        |                              |
| Queue               |          | Partially implemented        |
| TSS                 |           |                              |
| Thornames           | ✅         |                              |
| Mimir               |           |                              |
| Quote               | ✅         |                              |
| Invariants          | ✅         |                              |
| Block               | ✅         |                              |
| Export              |           | Not supported in current API |

If you notice any discrepancy or want a section prioritized, please open an issue or PR.

# TODOs
- Exceptions handling and keeping API response's error message
- More detailed tests
- Fill in missing endpoints in partially implemented sections

# Installation

## Normal installation

```bash
pip install thornode-py
```

## Development installation

```bash
git clone https://github.com/jpleorx/thornode-py.git
cd thornode-py
pip install --editable .
```

# Links
In case you’d like to check my other work or contact me:
* E-Mail [leo.ertuna@gmail.com](mailto:leo.ertuna@gmail.com)
* [GitHub](https://github.com/jpleorx)
* [PyPI](https://pypi.org/user/JPLeoRX/)
* [DockerHub](https://hub.docker.com/u/jpleorx)