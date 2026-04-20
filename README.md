# pyunifi

A Python implementation of the [UniFi API](https://developer.ui.com).

> [!CAUTION]
> This project is currently in early development and may not be stable. Use at your own risk.

## Features Coverage

|Application|Endpoints|GET|POST|PUT|DELETE|
|-|-|:-:|:-:|:-:|:-:|
|Network|`Application` Info|✅|N/A|N/A|N/A|
|Network|`Sites`|✅|N/A|N/A|N/A|
|Network|UniFi `Devices`|✅|❌|❌|❌|
|Network|`Clients`|✅|❌|N/A|N/A|
|Network|`Networks`|✅|❌|❌|❌|
|Network|`WiFi` Broadcasts|✅|❌|❌|❌|
|Network|`Hotspot`|✅|❌|N/A|❌|
|Network|`Firewall`|✅|❌|❌|❌|
|Network|Access Controll (`ACL`)|✅|❌|❌|❌|
|Network|`DNS` Policies|✅|❌|❌|❌|
|Network|`Traffic` Matching List|✅|❌|❌|❌|
|Network|`Support`ing Resources|✅|N/A|N/A|N/A|

## Development

```sh
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -e .
```