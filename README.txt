# P2P File Sharing System

A Python-based peer-to-peer file sharing application that enables direct file transfer between users without requiring a centralized server. The system uses a chunk-based architecture for efficient file distribution.

## Authors
- **Kadir Topal** - [@kadirTPL](https://github.com/kadirTPL)
- **Kerem Karataş**

## Features

- **Decentralized Architecture**: Direct peer-to-peer file sharing without central server dependency
- **Chunk-based Transfer**: Files are divided into chunks for efficient distribution and parallel downloading
- **Discovery Protocol**: Automatic peer and chunk discovery mechanism
- **Concurrent Operations**: Support for simultaneous upload and download operations
- **Flexible File Storage**: Configurable download locations

## System Architecture

The application consists of four main components that work together:

1. **Chunk Discovery** - Discovers available file chunks in the network
2. **Chunk Announcer** - Announces available chunks to other peers
3. **Chunk Upload** - Handles uploading file chunks to requesting peers
4. **Chunk Download** - Downloads chunks from peers and reconstructs files

## Installation

### Prerequisites
- Python 3.x
- Required Python packages (install via pip):
```bash
pip install -r requirements.txt
```

### Setup
1. Clone the repository:
```bash
git clone https://github.com/kadirTPL/P2P-FileSharing.git
cd P2P-FileSharing
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start
To test the application, run the Python files in the following order:

```bash
# Terminal 1
python chunkDiscovery.py

# Terminal 2 
python chunkAnnouncer.py

# Terminal 3
python chunkUpload.py

# Terminal 4
python chunkDownload.py
```

### Detailed Usage

#### 1. Start Chunk Discovery
```bash
python chunkDiscovery.py
```
This component discovers available chunks in the P2P network.

#### 2. Launch Chunk Announcer
```bash
python chunkAnnouncer.py
```
Announces your available file chunks to other peers in the network.

#### 3. Begin Chunk Upload Service
```bash
python chunkUpload.py
```
Starts the upload service to share your file chunks with requesting peers.

#### 4. Download Files
```bash
python chunkDownload.py
```
Downloads chunks from peers and reconstructs the complete files.

**Note**: Downloaded files will be saved to the location you specify in the chunkDownload configuration.

## File Structure

```
P2P-FileSharing/
├── chunkDiscovery.py    # Peer and chunk discovery
├── chunkAnnouncer.py    # Chunk announcement service
├── chunkUpload.py       # File chunk upload handler
├── chunkDownload.py     # File chunk download and reconstruction
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## How It Works

1. **File Chunking**: Large files are divided into smaller chunks for efficient transfer
2. **Peer Discovery**: Nodes discover other peers in the network
3. **Chunk Announcement**: Peers announce which chunks they have available
4. **Chunk Request**: Peers request specific chunks from other peers
5. **File Reconstruction**: Downloaded chunks are reassembled into the original file

## Configuration

- Modify network settings in the respective Python files
- Configure download directories in `chunkDownload.py`
- Adjust chunk size and transfer parameters as needed

## Network Requirements

- All peers should be on the same network or have network connectivity
- Ensure firewall settings allow the application to communicate
- Default ports should be available (check individual files for specific ports)

## Troubleshooting

### Common Issues

1. **Connection Issues**: Ensure all peers are on the same network
2. **File Not Found**: Check file paths and permissions
3. **Port Conflicts**: Verify no other applications are using the same ports

### Debug Mode
Run components with verbose output to troubleshoot issues:
```bash
python chunkDiscovery.py --verbose
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source. Please check the repository for license details.

## Future Enhancements

- [ ] GUI interface for easier user interaction
- [ ] Encryption for secure file transfer
- [ ] Resume capability for interrupted downloads
- [ ] Bandwidth throttling options
- [ ] Support for different file types and metadata
- [ ] Network topology optimization

## Support

For questions or issues, please:
- Open an issue on GitHub
- Contact the authors directly

---

**Note**: This is an educational/experimental project. Use responsibly and ensure compliance with your network policies.
Kadir Topal
Kerem Karataş
