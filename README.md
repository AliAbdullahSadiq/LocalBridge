<img width="3071" height="950" alt="Screenshot(1)" src="https://github.com/user-attachments/assets/40b4b5b8-28d6-407b-b07e-c297411affea" />

# LocalBridge
#### [Video Demo](youtube.com)
#### Description:

LocalBridge is a simple, lightweight, and cross-platform local file server for sharing files on your network. Designed for convenience and speed, perfect for quick file transfers between devices. Written entirely in Python and designed to be run from a single file, making it extremely portable and easy to use on a variety of systems, including Windows, macOS, Linux, and even Android via Termux.

The project consists of a single Python script, `localbridge.py`, which uses Python's built-in `http.server` module to handle network communication and file serving.

To enhance user experience, LocalBridge includes optional features such as password protection, request logging, and QR code generation for mobile access.

Unlike other HTTP local file servers, LocalBridge offers an intuitive and responsive CSS interface to ensure readability and ease of navigation on mobile devices without adding unnecessary bloat. The interface remains minimal and clean, focusing on usability without sacrificing aesthetics.

While the server is intended for local networks and convenience rather than public hosting, basic password protection was added to prevent unauthorized access. Users are warned that the password feature uses HTTP Basic Auth and does not encrypt data over the network, but it is sufficient for casual use. The focus remains on usability and speed.

This is my Final Project for CS50x 2025!

## Features

 - Serve any file over your local network
 - Works on Windows, macOS, Linux, and Android (via Termux)
 - Intuitive interface with responsive layout
 - Password protection (HTTP Basic Auth)
 - QR code for easy mobile access
 - Logging of client requests (optional)
 - Navigate directories with parent folder support
 - Lightweight: single Python file, zero dependencies (except optional QR code support)

## Requirements

Python 3.6+

Optional: qrcode[pil] for QR code generation

```
pip install qrcode[pil]
```

## Usage

```
python localbridge.py [options]
```

### Options

`-p, --port` — Port to serve on (default: 8000)

`-d, --directory` — Directory to share (default: current directory)

`--password` — Enable password protection

`--log` — Enable access logging

## Notes

Designed for quick local file sharing, not secure public hosting

Optional password is HTTP Basic Auth, **username is ignored**
