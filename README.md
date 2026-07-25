# Kite Data Engine 🛸

![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

A lightweight, high-performance declarative configuration and asset storage format designed as a faster, more human-readable alternative to JSON, YAML, and TOML.

Kite allows developers to define configurations, environment variables, and key-value assets using clean dot notation (`kite.KEY`) or dictionary lookup brackets (`kite["KEY WITH SPACES"]`) for identifiers containing spaces or special characters.

---

## 🚀 What's Coming Next? (Roadmap)

> 📅 **September Update Announcement**: In September 2026, Kite will introduce native parser implementations for **10 additional programming languages**! 
>
> Planned language support includes: **JavaScript / TypeScript, Go, Rust, C++, C#, Java, PHP, Ruby, Swift, and Kotlin**. Stay tuned!

---

## 📊 Feature Comparison Matrix

| Feature | **Kite** (`.kite`) | **JSON** (`.json`) | **YAML** (`.yaml`) | **TOML** (`.toml`) |
| :--- | :---: | :---: | :---: | :---: |
| **Native Comments** (`//`, `#`) | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Space-based Keys** | ✅ Native (`kite["KEY"]`) | ⚠️ Requires quotes | ⚠️ Complex | ⚠️ Requires quotes |
| **Dot Notation Access** | ✅ Native (`kite.KEY`) | ❌ Requires JS/Python wrap | ❌ Requires JS/Python wrap | ❌ Requires parser wrap |
| **Human Readability** | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐ Low/Medium | ⭐⭐⭐⭐ Medium | ⭐⭐⭐⭐ Medium |
| **Parsing Overhead** | 🚀 $O(1)$ Hash Map | ⚡ Fast | 🐢 Slow | ⚡ Moderate |
| **Boilerplate Noise** | 🟢 Minimal | 🔴 High (`{}`, `,`) | 🟡 Indentation sensitive | 🟡 Bracket heavy |

---

## 🛠️ Syntax Specifications & Rules

### 1. General Property Rules
- Standard variables use **dot notation**: `kite.KEY_NAME = VALUE`
- Multi-word variables or keys with spaces use **bracket notation**: `kite["KEY WITH SPACES"] = VALUE`
- Supports all fundamental data types out of the box.
- Supports single-line comments starting with `//` or `#`.

### 2. Supported Data Types Summary

| Data Type | Syntax Example in `.kite` | Python Equivalent |
| :--- | :--- | :--- |
| **String** | `kite.NAME = "Kite Engine"` | `str` |
| **Integer** | `kite.PORT = 8080` | `int` |
| **Float** | `kite.TIMEOUT = 12.5` | `float` |
| **Boolean** | `kite.DEBUG = true` | `bool` |
| **Array / List** | `kite.TAGS = ["fast", "clean", "light"]` | `list` |
| **Dictionary / Map** | `kite.DB = {"host": "localhost", "port": 5432}` | `dict` |

---

## 📄 File Example (`base.kite`)

```text
// ==========================================
// GENERAL SYSTEM CONFIGURATION
// ==========================================
kite.VERSION = "1.0.0"
kite.PORT = 8080
kite.DEBUG_MODE = true
kite.TIMEOUT = 15.5

// ==========================================
// ASSETS AND IDENTIFIERS WITH SPACES
// ==========================================
kite["MAIN ASSET ID"] = "998877665544"
kite["HERO BANNER URL"] = "[https://cdn.site.com/banner.png](https://cdn.site.com/banner.png)"
kite["PRIMARY COLOR"] = "#0071E3"
kite["WELCOME MESSAGE"] = "Welcome to the Kite Data Engine!"

// ==========================================
// COMPLEX DATA STRUCTURES
// ==========================================
kite.SERVERS = ["us-east", "sa-east", "eu-central"]
kite.DATABASE = {
    "host": "127.0.0.1",
    "port": 5432,
    "user": "admin"
}
