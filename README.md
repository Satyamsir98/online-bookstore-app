# 📚 Online Bookstore Application

## 📌 Overview

This project is a full-stack Online Bookstore Application that allows customers to browse and purchase books, while enabling bookstore owners to manage inventory and orders.

The system is built using a Flask-based REST API backend, Angular frontend, and SQLite database with SQLAlchemy ORM.

It follows a role-based architecture supporting Customers, Bookstore Owners, and Admin functionalities.

---

## 🧠 Features

### 👤 Customer

- Browse and search books by title, author, or genre  
- View book details, pricing, and availability  
- Add books to cart and place orders  
- Track order status (Placed, Shipped, Delivered)  
- Submit ratings and reviews  

---

### 🏪 Bookstore Owner

- Register and manage bookstore  
- Add, update, and delete books  
- Manage inventory  
- Process and track orders  
- View customer reviews  

---

### 🛠️ Admin (Optional)

- Manage users and roles  
- Manage bookstores  
- Handle disputes  

---

## 🗄️ Database Design

Entities:

- Customer  
- Bookstore Owner  
- Books  
- Orders  
- Reviews  
- Admin  

Relationships:

- Customers place Orders  
- Books belong to Bookstore Owners  
- Customers review Books  
- Orders link Customers and Books  

---

## 🏗️ Architecture

Frontend (Angular)  
→ REST APIs (Flask)  
→ Database (SQLite with SQLAlchemy)

---

## 💡 Tech Stack

- Frontend: Angular  
- Backend: Python (Flask)  
- Database: SQLite  
- ORM: SQLAlchemy  

---

## ⚙️ Functional Highlights

- RESTful API design  
- Role-based authorization  
- Input validation and error handling  
- Modular and scalable backend structure  

---

## ▶️ How to Run

### Backend

```bash
python app.py
```

### Frontend

```bash
ng serve
```

---

## 🎯 Use Cases

- E-commerce applications  
- Online retail platforms  
- Order management systems  
- Role-based web applications  

---

## 💯 Highlights

- Full-stack implementation  
- Role-based access control  
- Real-world database design  
- Clean architecture and modular code  

---

## 👤 Author

Satyam Rai  
Full Stack Developer → Data Engineer
