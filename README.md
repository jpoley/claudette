# claudette

a smarter version of claude ;)


# Claude via Amazon Bedrock in DevContainer

This project lets you invoke Claude 3 Sonnet using Amazon Bedrock inside a Docker DevContainer.

## ✅ Prerequisites

- AWS credentials in `~/.aws/credentials`
- Access to Claude in Amazon Bedrock (enabled in console)
- VSCode with **Remote Containers** extension
- Docker installed

## 🚀 Usage

1. Open this folder in VSCode.
2. Reopen in DevContainer (you'll be prompted).
3. Claude can now be invoked with:

```bash
python invoke_claude.py

```
---


### 🧪 How to Run

1. Install Docker + VSCode + Remote Containers extension  
2. Run:
   ```bash
   git clone https://github.com/jpoley/claudette.git
   cd claudette
   code .
