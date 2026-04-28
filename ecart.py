import tkinter as tk

# ---------- Product Data ----------
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Headphones", "price": 2000},
    {"name": "Keyboard", "price": 1500},
    {"name": "Mouse", "price": 800}
]

cart = {}

# ---------- Functions ----------
def add_to_cart(product):
    name = product["name"]
    price = product["price"]

    if name in cart:
        cart[name]["qty"] += 1
    else:
        cart[name] = {"price": price, "qty": 1}

    update_cart()

def update_cart():
    cart_text.delete(1.0, tk.END)

    total = 0

    for item, details in cart.items():
        qty = details["qty"]
        price = details["price"]
        subtotal = qty * price
        total += subtotal

        cart_text.insert(tk.END, f"{item}  x{qty}   = ₹{subtotal}\n")

    offer = total * 0.05
    final_total = total - offer

    cart_text.insert(tk.END, "\n----------------------\n")
    cart_text.insert(tk.END, f"Total : ₹{total}\n")
    cart_text.insert(tk.END, f"Discount : -₹{offer:.2f}\n")
    cart_text.insert(tk.END, f"Final : ₹{final_total:.2f}\n")

def clear_cart():
    cart.clear()
    update_cart()

# ---------- GUI ----------
root = tk.Tk()
root.title("E-Cart System")
root.geometry("520x580")   # reduced window size
root.config(bg="#f5f6fa")

# ---------- Fonts ----------
title_font = ("Segoe UI", 18, "bold")
heading_font = ("Segoe UI", 13, "bold")
text_font = ("Segoe UI", 11)

# Title
tk.Label(root, text="🛒 E-Cart System", font=title_font, bg="#f5f6fa").pack(pady=10)

# Offer
tk.Label(
    root,
    text="🔥 5% OFF on all purchases!",
    fg="white",
    bg="#e84118",
    font=("Segoe UI", 11, "bold"),
    padx=8, pady=4
).pack(pady=5)

# Product Frame
frame = tk.Frame(root, bg="#f5f6fa")
frame.pack(pady=10)

# Products UI
for product in products:
    item_frame = tk.Frame(frame, bg="white", bd=1, relief="solid")
    item_frame.pack(fill="x", padx=15, pady=5)

    tk.Label(item_frame, text=product["name"], font=heading_font, bg="white").pack(side="left", padx=10)

    tk.Label(item_frame, text=f"₹{product['price']}", font=text_font, bg="white").pack(side="left", padx=20)

    tk.Button(
        item_frame,
        text="Add",
        bg="#4cd137",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        command=lambda p=product: add_to_cart(p)
    ).pack(side="right", padx=10)

# Cart Label
tk.Label(root, text="🧾 Cart Summary", font=heading_font, bg="#f5f6fa").pack()

# ✅ Reduced Cart Box Size
cart_text = tk.Text(root, height=10, width=45, font=("Consolas", 10))
cart_text.pack(pady=8)

# ✅ Buttons clearly visible at bottom
btn_frame = tk.Frame(root, bg="#f5f6fa")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="Clear Cart",
    bg="#e84118",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12,
    command=clear_cart
).pack(side="left", padx=20)

tk.Button(
    btn_frame,
    text="Exit",
    bg="#273c75",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12,
    command=root.destroy
).pack(side="right", padx=20)

root.mainloop()