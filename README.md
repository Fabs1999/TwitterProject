# 🤖 Twitter Sentiment Analysis with Tweepy & TextBlob

Welcome to **Twitter Sentiment Analysis**! 🚀 This project scrapes tweets using **Tweepy**, analyzes their sentiment with **TextBlob**, and tells you if the internet is smiling 😊 or frowning 😡 about a topic.

---

## 🔥 Features
✅ Fetch **real-time tweets** from Twitter (X).  
✅ Analyze tweets for **positive, negative, or neutral sentiment**.  
✅ Avoid API rate limits (well, mostly 😅).  
✅ Python-powered awesomeness. 🐍

---

## 📦 Setup Instructions

### 1️⃣ Clone this repo
```sh
 git clone https://github.com/YourUsername/TwitterSentimentAnalysis.git
 cd TwitterSentimentAnalysis
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set up Twitter API Credentials 🛠️
1. Get API keys from [Twitter Developer Portal](https://developer.x.com/en/portal/product).
2. Create a `.env` file and add:
   ```ini
   BEARER_TOKEN=your_bearer_token_here
   ```

### 4️⃣ Run the Sentiment Analyzer
```sh
python TwiSentiment.py
```

---

## 🧠 How It Works
1. **Tweepy** grabs recent tweets (no retweets, English only!).
2. **TextBlob** performs sentiment analysis.
3. The script prints whether people are happy 😍, sad 😭, or neutral 😐.

---

## 🎯 Example Output
```
Tweet: "I love Python!"
Sentiment: Sentiment(polarity=0.5, subjectivity=0.6) → 😊 Positive

Tweet: "This API is so frustrating!"
Sentiment: Sentiment(polarity=-0.7, subjectivity=0.8) → 😡 Negative
```

---

## ⚠️ Rate Limits & Fixes
- If you get `429 Too Many Requests`, you hit the API limit. 🛑
- The script will **automatically wait 15 mins** before retrying.
- You can upgrade your API plan for more requests.

---

## 👨‍💻 Contributing
Got cool ideas? Fixes? **Fork this repo and submit a PR!** 🤝

---

## 💖 Support
If you found this useful, **drop a ⭐ on GitHub** and make my day! 🌟

---

## 📜 License
MIT License – Do whatever you want, just give credit where it’s due. 😉

