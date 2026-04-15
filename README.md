# TrendBot

TrendBot fetches **recent startup and technology information** from online sources in a simple dashboard.

---

## 🚀 Features

* Fetches the latest **startup and tech headlines**
* Runs entirely in Python
* Hosted by Anvil

---

## 🧠 How It Works

1. The app requests feed from a tech news source.
2. The information parsed to extract recent articles.
3. Article titles are collected.

---

## 🛠 Tech Stack

* Python
* Anvil (UI + hosting)
* XML parsing (`xml.etree.ElementTree`)

---

## 📊 Example Output

```
AI startup launches new developer platform
Investors pour funding into robotics company
Open source AI tool gains traction
Startup building automation tools raises seed round
```

---

## 📦 Project Structure

```
trendbot/
│
├── server_module.py    # Fetches and parses RSS feed
├── form1.py            # UI logic
└── README.md
```

---

## 💡 Use Cases

TrendBot can be useful for:

* startup and tech news
* spotting emerging ideas
* quickly checking industry trends
* inspiration for product ideas

---

## 🔮 Future Improvements

Possible upgrades:

* extract keywords instead of titles
* combine multiple sources (Product Hunt, GitHub, etc.)
* summarize articles with AI
* trends with charts

---

## 📄 License

MIT License



AI has drafted the entire README. It's not laziness, it's optimization. And honestly *emdash* that's brave.
