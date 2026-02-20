# GA_2 - Question 5  
## Static JSON API hosted on GitHub Pages

This project hosts a static JSON API using GitHub Pages.

### 🔗 Live API URL

https://amanvx.github.io/iitm-tds-26t1/GA_2/q5/products.json

---

## 📦 API Structure

The JSON file contains:

### 1️⃣ metadata
- **email**: 24f2008471@ds.study.iitm.ac.in  
- **version**: f9310ce3  

### 2️⃣ products
- Exactly 24 products
- Each product includes:
  - id
  - name
  - category
  - price
  - stock
  - rating

### 3️⃣ aggregations
Pre-computed statistics per category:
- clothing
- home
- books
- sports
- electronics

Each category contains:
- count (number of products)
- inventoryValue (sum of price × stock)

---

## 🚀 Deployment

This JSON file is hosted using **GitHub Pages**:

Repository → Settings → Pages  
Source: Deploy from branch  
Branch: main  
Folder: / (root)

---

## 📝 Notes

- This API is fully static (no backend server).
- CDN cache can be bypassed using:
  
  `?v=1`

Example:

