# 🌍 Humanity Score Spider Collection

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.2-43B02A?style=flat-square&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Code Style](https://img.shields.io/badge/Code_Style-Black-000000?style=flat-square&logo=python&logoColor=white)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-MIT-00ADD8?style=flat-square&logo=github&logoColor=white)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square&logo=github&logoColor=white)](#contributing)
[![Ethical Data](https://img.shields.io/badge/Ethical-Data_Collection-success?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAbwAAAG8B8aLcQwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAB5SURBVDiNY/z//z8DMvj14wfD7evXGH79/MkgIirGICgkxCAkLMzAyMjIwIQs+P//fwYmJiYGBgYGBmY2dgZBQUEGYVExBnFJSQZ2DnaG////MzDi0szIyMjwh+EvAyMjI8P/f/8Y/v37y/Dn7x8GJiYmBhYWVgYA8Kcl9D/hYSAAAAAASUVORK5CYII=)](#ethical-guidelines)

<div align="center">
<h3>
  <em>"Forwarding justice everywhere through data and AI" - PhantHive</em>
  <br/>
  <small>Making international justice more transparent and accessible, one data point at a time</small>
</h3>

<sup>Because transparency in justice serves humanity</sup>
</div>

> Transparently collecting public data to understand humanitarian actions through international standards 🌟

## 💡 What is This?

This project collects publicly available information from official sources to help understand how actions align with established humanitarian principles. We focus on positive recognition and objective international standards.

## 🎯 Core Focus Areas

Based on internationally recognized humanitarian principles:

### 🤝 Human Dignity
*Grounded in Universal Human Rights*
- Universal Declaration of Human Rights (1948)
- International Human Rights Conventions
- Humanitarian Law Principles

### ☮️ Non-Violence
*Based on Peace-Building Standards*
- UN Peace-Building Framework
- Nobel Peace Prize Criteria
- International Conflict Resolution Standards

### 🔍 Truth & Transparency
*Following International Standards*
- Freedom of Information Principles
- Transparency International Guidelines
- UNESCO Communication Standards

### ⚖️ Justice & Fairness
*Aligned with International Law*
- International Court Decisions
- UN Social Justice Frameworks
- Equal Rights Declarations

### 🌱 Common Good
*Supporting Global Development*
- UN Sustainable Development Goals
- Environmental Protection Treaties
- Public Health Standards

## 🛠️ Technical Setup

### Prerequisites
```bash
# Required tools
Python 3.8+ (everything is tested on 3.12 though)
Microsoft Edge
EdgeDriver (matching your Edge version) in spiders/ folder
```

# Installation
```
pip install -r requirements.txt
```

### Project Structure
```
📁 humanity-spider/
├── 📄 main.py           # Main runner
├── 📁 data/            # Collected data
└── 📁 spiders/         # Data collectors
    └── 📄 icc_spider.py  # ICC public records
```

### Quick Start
```bash
# Clone & Run
git clone https://github.com/yourusername/humanity-spider
cd humanity-spider
python main.py
```

## 📊 Data Format

```json
{
  "metadata": {
    "version": "1.0",
    "source": "SOURCE_NAME",
    "date_collected": "ISO_TIMESTAMP"
  },
  "records": [
    {
      "source_info": {
        "name": "Record Name",
        "type": "public_record",
        "url": "Source URL"
      },
      "recognition": {
        "positive_actions": [],
        "official_acknowledgments": []
      }
    }
  ]
}
```

## 🤝 Contributing

We welcome contributions that:
- Focus on official, public sources
- Maintain transparent methodologies
- Respect privacy and data protection
- Add positive recognition metrics
- Improve data collection accuracy

## ⚖️ Ethical Guidelines

We are committed to:
- Using only public, official sources
- Focusing on positive recognition
- Maintaining full transparency
- Respecting privacy rights
- Following data protection laws
- Supporting humanitarian principles

## 🌟 Future Plans

- [ ] Add more international recognition sources
- [ ] Implement peace prize databases
- [ ] Include humanitarian award records
- [ ] Develop transparency metrics

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 💝 Acknowledgments

Special thanks to:
- International humanitarian organizations
- Open-source community
- Data transparency advocates
- Peace research institutions

---

<p align="center">
Made with ❤️ for a more transparent and peaceful world
</p>