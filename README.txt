 P2P File Sharing

A lightweight and decentralized peer-to-peer (P2P) file sharing system written in Python. Inspired by BitTorrent-style chunked transfer, this project enables users to share files directly with each other — **no central server required**.

---

## 🚀 Features

- **Decentralized transfers** using a chunked protocol (announcer → discovery → uploader/downloader).
- Works across Windows, macOS, and Linux.
- Simple and intuitive command-line interface.
- Easily supports large files via chunked transfers.
- Peer discovery mechanism without central coordination.

---

## 🧩 Components

The project contains four main modules:

1. `Chunk_Announcer.py` – Announces availability of files.
2. `Chunk_Discovery.py` – Finds peers sharing a given file/chunk.
3. `Chunk_Uploader.py` – Uploads requested chunks to peers.
4. `Chunk_Downloader.py` – Downloads chunks from peers and reconstructs the file.

Together, they form a functional P2P sharing pipeline.

---

## ⚙️ Requirements

- Python **3.7+**
