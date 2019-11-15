# NSE IPO(Initial public offering) Python SDk

Python wrapper around NSE IPO application REST API's.

API Documentation: [NSE IPO REST API Docs](https://www.nseindia.com/technology/content/nnf/WEB_CBRICS_PROTOCOL_1.1.pdf)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

```python
import NseIPO

api = NseIPO()
api.Auth.login("member_id", "login_id", "pwd")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)