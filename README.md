<img width="2714" height="948" alt="Screenshot(1)" src="https://github.com/user-attachments/assets/8a8b5c2b-f6cd-4b15-9632-262a7928ca38" />

# LocalBridge

LocalBridge was born out of a very simple frustration: transferring just one or two files between my phone and laptop, or vice versa, was always more trouble than it should be. USB drives are inconvenient and often incompatible with phones. Cloud storage is slow, login-heavy, and overkill for a couple of files. Bluetooth? Don’t even get me started.

Before LocalBridge, I would use `python3 -m http.server` and manually connect via IP and port. It worked, but had limitations: no password protection, tiny text on mobile browsers, inconvenient port changes, and the worst part, digging up your local IP and typing it carefully on your phone.

LocalBridge fixes all that in a single, lightweight Python script. It shows your local IP and even generates a QR code for instant mobile access. It works across Windows, macOS, Linux, and Android via Termux, provides an intuitive, mobile-friendly interface, and includes optional password protection for basic security.

Users are warned that the password feature uses HTTP Basic Auth and does not encrypt data over the network, but it is sufficient for casual use. The focus remains on usability and speed.

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
