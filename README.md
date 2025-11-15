# SESD_AS_10_2496

## Client-Server Architecture for E-commerce Product Ordering System
**SESD Assignment 10 - Software Engineering and System Design**

**Student ID:** 2303A52496  
**Architecture Pattern:** Client-Server

---

## 📋 Table of Contents
- [Problem Statement](#problem-statement)
- [Architecture Overview](#architecture-overview)
- [System Components](#system-components)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [UML Deployment Diagram](#uml-deployment-diagram)
- [Screenshots](#screenshots)
- [Benefits & Limitations](#benefits--limitations)

---

## 🎯 Problem Statement

An e-commerce startup needs a product ordering system where:
- **Client** users can browse products, place orders, and track shipments
- **Server** handles inventory management and payment processing
- The system must be scalable, maintainable, and secure

---

## 🏗️ Architecture Overview

This project implements a **Client-Server Architecture** with clear separation of concerns:

```
┌─────────────────┐         HTTP/REST API         ┌──────────────────┐
│                 │  ◄─────────────────────────►  │                  │
│  Client (HTML)  │     JSON Data Exchange        │  Server (Flask)  │
│   JavaScript    │                                │   Python REST    │
│                 │                                │      API         │
└─────────────────┘                                └──────────────────┘
     (Browser)                                         (Backend)
                                                            │
                                                            ▼
                                                    ┌──────────────┐
                                                    │   In-Memory  │
                                                    │   Database   │
                                                    └──────────────┘
```

### Why Client-Server Architecture?

1. **Clear Separation**: UI logic (client) and business logic (server) are independent
2. **Scalability**: Multiple clients can connect to the same server
3. **Security**: Sensitive operations (inventory, payments) secured on server
4. **Maintainability**: Changes to backend don't affect client interface
5. **Flexibility**: Different client types (web, mobile) can use same server API

---

## 🔧 System Components

### Client Side (`client.html`)
- **Technology:** HTML5, CSS3, JavaScript (ES6+)
- **Features:**
  - Product browsing with real-time inventory
  - Interactive order placement form
  - Order tracking system
  - Responsive design with modern UI
- **Communication:** Fetch API for RESTful calls

### Server Side (`server.py`)
- **Technology:** Flask (Python)
- **Features:**
  - RESTful API endpoints
  - Inventory management
  - Order processing
  - Payment handling (simulated)
  - CORS enabled for cross-origin requests

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)

### Step 1: Clone Repository
```bash
git clone https://github.com/2303A52496/SESD_AS_10_2496.git
cd SESD_AS_10_2496
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
- Flask 2.3.3
- flask-cors 4.0.0
- Werkzeug 2.3.7

---

## 🚀 Running the Application

### Start the Server

```bash
python server.py
```

**Output:**
```
Starting E-commerce Server...
Server running on http://localhost:5000
 * Running on http://127.0.0.1:5000
```

### Open the Client

1. Open `client.html` in your web browser
2. Or use a local server:
   ```bash
   python -m http.server 8000
   ```
   Then navigate to: `http://localhost:8000/client.html`

---

## 🔌 API Endpoints

### 1. Get All Products
**Endpoint:** `GET /api/products`

**Response:**
```json
{
  "success": true,
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 80000,
      "stock": 15
    }
  ]
}
```

### 2. Place Order
**Endpoint:** `POST /api/order`

**Request Body:**
```json
{
  "customer_name": "John Doe",
  "product_id": 1,
  "quantity": 2
}
```

**Response:**
```json
{
  "success": true,
  "message": "Order placed successfully",
  "order": {
    "order_id": "ORD00001",
    "product_name": "Laptop",
    "total_amount": 160000,
    "status": "Order Placed"
  }
}
```

### 3. Track Order
**Endpoint:** `GET /api/track/<order_id>`

**Response:**
```json
{
  "success": true,
  "order": {
    "order_id": "ORD00001",
    "customer_name": "John Doe",
    "status": "Order Placed",
    "payment_status": "Pending"
  }
}
```

### 4. Process Payment
**Endpoint:** `POST /api/payment/<order_id>`

**Request Body:**
```json
{
  "payment_method": "Credit Card"
}
```

### 5. Get All Orders (Admin)
**Endpoint:** `GET /api/orders`

---

## 📊 UML Deployment Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Node                          │
│                      (User Browser)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              client.html                              │  │
│  │  - HTML5 Interface                                    │  │
│  │  - JavaScript Logic                                   │  │
│  │  - CSS Styling                                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ HTTP/REST
                           │ (Port 5000)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                        Server Node                          │
│                  (Flask Web Server)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              server.py                                │  │
│  │  <<REST API>>                                         │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  API Routes:                                    │  │  │
│  │  │  - /api/products (GET)                          │  │  │
│  │  │  - /api/order (POST)                            │  │  │
│  │  │  - /api/track/<id> (GET)                        │  │  │
│  │  │  - /api/payment/<id> (POST)                     │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Business Logic:                                │  │  │
│  │  │  - Inventory Management                         │  │  │
│  │  │  - Order Processing                             │  │  │
│  │  │  - Payment Handling                             │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          In-Memory Data Storage                       │  │
│  │  - Products Dictionary                                │  │
│  │  - Orders Dictionary                                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📸 Screenshots

### 1. Product Browsing
![Product List](screenshots/products.png)
*Users can view all available products with prices and stock*

### 2. Order Placement
![Order Form](screenshots/order.png)
*Interactive form for placing orders*

### 3. Order Confirmation
![Order Success](screenshots/confirmation.png)
*Order confirmation with order ID and details*

### 4. Order Tracking
![Track Order](screenshots/tracking.png)
*Track order status using order ID*

---

## ⚖️ Benefits & Limitations

### Benefits of Client-Server Architecture

✅ **Scalability**
- Easy to scale horizontally by adding more servers
- Load balancing can distribute client requests
- Multiple clients can connect simultaneously

✅ **Centralized Control**
- Business logic and data centralized on server
- Easier to implement security measures
- Consistent data management

✅ **Platform Independence**
- Clients can be on different platforms (web, mobile, desktop)
- Server technology independent of client
- RESTful API enables interoperability

✅ **Maintainability**
- Clear separation of concerns
- Updates to server don't require client changes (if API stable)
- Easier debugging and testing

✅ **Security**
- Sensitive operations protected on server
- Client has limited access
- Authentication/authorization centralized

### Limitations

❌ **Network Dependency**
- Requires constant network connectivity
- Performance depends on network quality
- Offline functionality limited

❌ **Single Point of Failure**
- Server downtime affects all clients
- Requires redundancy/backup strategies
- Load on server can become bottleneck

❌ **Initial Setup Complexity**
- Requires server infrastructure
- More complex than standalone applications
- Need for server maintenance and monitoring

❌ **Latency Issues**
- Network round-trip time adds delay
- Not suitable for real-time applications without optimization
- Bandwidth limitations can affect performance

❌ **Cost**
- Server hosting and maintenance costs
- May need dedicated DevOps resources
- Scaling can be expensive

---

## 📝 Project Structure

```
SESD_AS_10_2496/
│
├── client.html           # Frontend client interface
├── server.py             # Backend Flask server
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── UML_Diagram.png       # Deployment diagram
└── screenshots/          # Application screenshots
    ├── products.png
    ├── order.png
    ├── confirmation.png
    └── tracking.png
```

---

## 🎓 Assignment Report Summary

### 1. Problem Statement ✓
E-commerce ordering system with client-server separation

### 2. Architecture Justification ✓
Client-Server chosen for scalability, security, and maintainability

### 3. UML Deployment Diagram ✓
Shows client node, server node, and communication protocols

### 4. Working Prototype ✓
- Functional client with product browsing, ordering, tracking
- Flask server with complete REST API
- Screenshots demonstrating all features

### 5. GitHub Repository ✓
https://github.com/2303A52496/SESD_AS_10_2496

### 6. Comparative Discussion ✓
Detailed analysis of scalability, performance, benefits, and limitations

---

## 🤝 Contributing

This is an academic project for SESD Assignment 10. For improvements or suggestions:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📄 License

This project is created for educational purposes as part of SESD coursework.

---

## 👤 Author

**Student ID:** 2303A52496  
**Course:** Software Engineering and System Design  
**Assignment:** Client-Server Architecture Implementation

---

**Last Updated:** November 2025
