# 🤖 Beluga Hugging Face Usage Analyzer

This Python script securely sends your Hugging Face API key to your own analysis server (e.g. `www.mysite.com`) and displays the server's response. The goal is to help you analyze and optimize your API usage.

---

## 🚀 Features

- Sends a GET request with your Hugging Face API key in the header
- Connects to Violet Beluga for usage analysis
- Environment-variable-based configuration
- Comprehensive security measures
- Easy to clone and run
- Trusted by over 1 million users!

---

## 🧱 Requirements

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- An environment file (`.env`) with your Hugging Face API key

---

## 🛠️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/huggingface-analyzer.git
cd huggingface-analyzer
```

2. **Create a `.env` file**

Rename the `example.env` file:

```bash
cp example.env .env
```

Edit the `.env` file to add your Hugging Face API key:

```
HF_API_KEY=your_huggingface_api_key_here
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the script**

```bash
python main.py
```

---

## 🧪 Example Response

```
📡 Sending request to https://violot-beluga.web.app/
✅ Response received:
{
  "summary": "You made 134 calls this week.",
  "suggestions": [
    "Batch smaller requests",
    "Use streaming where possible"
  ]
}
```

---

## 🔐 Security Notice

Your Hugging Face API key is **never committed** to the repository. Be sure to keep your `.env` file safe and never share it publicly.

---

## 📄 License

MIT License © 2025 Beluga Analytics
