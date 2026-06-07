📁 utils/

## 📖 Dictionary
Folder ini berisi kumpulan utility tools (helper functions) yang digunakan untuk mendukung sistem quant trading.

Isi dari folder ini bukan strategi utama, melainkan fungsi-fungsi pendukung seperti risk management, indikator, signal filter, validasi, dan tools analisis lainnya.

Tujuan utama folder ini adalah membuat sistem lebih modular, rapi, reusable, dan mudah dikembangkan.

---

## 🧰 Tools

### 🧠 risk_management_v1.py
Basic risk management utility untuk menghitung manajemen risiko dasar dalam trading system.

Features:
- Fixed risk percentage
- Risk amount calculation
- Stop loss distance calculation
- Position sizing
- Reward distance calculation
- Take profit calculation
- BUY / SELL support

---

### 📊 position_size_trade_spot_v1.py
Position Size Calculator untuk spot trading (tanpa leverage).

Tool ini membantu menentukan ukuran posisi yang sesuai berdasarkan account balance, risk per trade, entry price, dan stop loss sehingga risiko tetap terkontrol sesuai batas yang ditentukan.

Features:
- Account balance input
- Fixed risk percentage
- Risk amount calculation
- Entry price and stop loss input
- Risk per unit calculation
- Position size calculation
- Capital required calculation
- BUY / SELL support
- Input validation
- Insufficient balance warning
- Spot trading focused (no leverage)

---

## 🎯 Tujuan
- Memisahkan strategy dan helper tools
- Membuat sistem lebih modular
- Mudah dikembangkan dan di-maintain
- Reusable untuk berbagai strategi trading
- Mempermudah scaling project quant trading
