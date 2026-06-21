# 📁 utils/

## 📖 Dictionary
Folder ini berisi kumpulan utility tools (helper functions) yang digunakan untuk mendukung sistem quant trading.

Isi folder ini bukan strategi utama, melainkan fungsi pendukung seperti risk management, position sizing, indikator, signal filter, validasi, dan tools analisis statistik.

Tujuan utama folder ini adalah membuat sistem lebih modular, rapi, reusable, dan mudah dikembangkan.

---

## 🧰 Tools

### 🧠 math_helper_v1.py
Lightweight Python command-line tool untuk basic statistical and financial data analysis.

Tool ini memproses input angka (space-separated) dan menghasilkan metrik statistik utama untuk analisis data cepat.

**Fungsi utama:**
- Mean calculation
- Median calculation
- Variance calculation
- Standard deviation
- Log return calculation
- Z-score normalization

**Tech Stack:**
- Python (Standard Library)

**Purpose:**
Digunakan untuk eksplorasi data, pemahaman statistik dasar, dan konsep awal dalam quantitative finance.

---

### 🧠 risk_management_v1.py
Basic risk management utility untuk menghitung manajemen risiko dalam trading system.

**Fungsi utama:**
- Fixed risk percentage
- Risk amount calculation
- Stop loss distance calculation
- Position sizing
- Reward distance calculation
- Take profit calculation
- BUY / SELL support

---

### 📊 position_size_trade_spot_v1.py
Position size calculator untuk spot trading (tanpa leverage).

Tool ini membantu menentukan ukuran posisi berdasarkan account balance, risk per trade, entry price, dan stop loss sehingga risiko tetap terkontrol sesuai batas yang ditentukan.

**Fungsi utama:**
- Account balance input
- Fixed risk percentage
- Entry price & stop loss input
- Risk amount calculation
- Risk per unit calculation
- Position size calculation
- Capital required calculation
- BUY / SELL support
- Input validation
- Insufficient balance warning
- Spot trading focus (no leverage)

---

## 🎯 Tujuan
- Memisahkan strategy dan helper tools  
- Membuat sistem lebih modular  
- Mudah dikembangkan dan di-maintain  
- Reusable untuk berbagai strategi trading  
- Mempermudah scaling project quant trading
