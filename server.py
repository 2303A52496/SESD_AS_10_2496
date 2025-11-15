from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 80000, "stock": 15},
    {"id": 2, "name": "Wireless Mouse", "price": 1200, "stock": 50},
    {"id": 3, "name": "Mechanical Keyboard", "price": 4500, "stock": 30},
    {"id": 4, "name": "USB-C Hub", "price": 2500, "stock": 25},
    {"id": 5, "name": "Headphones", "price": 3000, "stock": 40},
]

# Orders storage
orders = {}
order_count = 0

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all available products"""
    return jsonify({"success": True, "products": products}), 200

@app.route('/api/order', methods=['POST'])
def place_order():
    """Place a new order"""
    global order_count
    
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    customer_name = data.get('customer_name')
    
    # Validate input
    if not product_id or not customer_name:
        return jsonify({"success": False, "message": "Missing required fields"}), 400
    
    # Find product
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"success": False, "message": "Product not found"}), 404
    
    # Check stock
    if product['stock'] < quantity:
        return jsonify({"success": False, "message": "Insufficient stock"}), 400
    
    # Process order
    order_count += 1
    order_id = f"ORD{order_count:05d}"
    
    orders[order_id] = {
        "order_id": order_id,
        "product_name": product['name'],
        "product_id": product_id,
        "quantity": quantity,
        "customer_name": customer_name,
        "total_amount": product['price'] * quantity,
        "status": "Order Placed",
        "payment_status": "Pending"
    }
    
    # Update stock
    product['stock'] -= quantity
    
    return jsonify({
        "success": True, 
        "message": "Order placed successfully",
        "order": orders[order_id]
    }), 201

@app.route('/api/track/<order_id>', methods=['GET'])
def track_order(order_id):
    """Track order status"""
    order = orders.get(order_id)
    
    if order:
        return jsonify({"success": True, "order": order}), 200
    else:
        return jsonify({"success": False, "message": "Order not found"}), 404

@app.route('/api/payment/<order_id>', methods=['POST'])
def process_payment(order_id):
    """Process payment for an order"""
    order = orders.get(order_id)
    
    if not order:
        return jsonify({"success": False, "message": "Order not found"}), 404
    
    data = request.json
    payment_method = data.get('payment_method', 'Credit Card')
    
    # Simulate payment processing
    order['payment_status'] = 'Completed'
    order['payment_method'] = payment_method
    order['status'] = 'Payment Confirmed - Preparing for Shipment'
    
    return jsonify({
        "success": True,
        "message": "Payment processed successfully",
        "order": order
    }), 200

@app.route('/api/orders', methods=['GET'])
def get_all_orders():
    """Get all orders (admin endpoint)"""
    return jsonify({"success": True, "orders": list(orders.values())}), 200

@app.route('/', methods=['GET'])
def home():
    """API home endpoint"""
    return jsonify({
        "message": "E-commerce Product Ordering System API",
        "version": "1.0",
        "endpoints": {
            "/api/products": "GET - List all products",
            "/api/order": "POST - Place new order",
            "/api/track/<order_id>": "GET - Track order",
            "/api/payment/<order_id>": "POST - Process payment",
            "/api/orders": "GET - Get all orders"
        }
    }), 200

if __name__ == '__main__':
    print("Starting E-commerce Server...")
    print("Server running on http://localhost:5000")
    app.run(debug=True, port=5000)
