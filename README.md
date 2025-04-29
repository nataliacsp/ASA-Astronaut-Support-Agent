# ASTRA Pro — AI Semantic Journal Agent 🌌

## Overview

ASTRA (Advanced Semantic Task and Reflection Assistant) is an AI agent designed for voice-controlled journaling, mood analysis, and personal record keeping.  
Built using the **Semantic Kernel** framework, ASTRA Pro offers modular, extendable skills focused on human-AI emotional support.

Developed by **Natalia Solorzano** for the Microsoft AI Agents Hackathon 2025 and ITAI 2277 Capstone Project.

---

## Features

- 🔊 Natural voice interface (speech recognition)
- ✍️ Save daily journal logs with automatic folder organization
- 📈 Sentiment analysis (positive / negative / neutral)
- 📝 Summarization of journal entries using transformers
- 📁 Organized by user, year, month, day, mood
- 💬 Modular skills using Microsoft Semantic Kernel

---

## Technologies Used

- Python 3.10+
- Semantic Kernel (Microsoft)
- TextBlob (sentiment analysis)
- Transformers (distilbart-cnn-12-6)
- SpeechRecognition
- Pyttsx3 (text-to-speech)
- PIL (image loading)

---

## Installation

```bash
git clone https://github.com/nataliacsp/ASTRAAgent-Pro.git
cd ASTRAAgent-Pro
python3 -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python -m textblob.download_corpora
