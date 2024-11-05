class OrderNode:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # List of ordered items
        self.next = None

class MenuOrderSystem:
    def __init__(self):
        self.head = None  # Points to the front of the list
        self.tail = None  # Points to the end of the list
        self.average_prep_time = 5  # Average time in minutes for each item

    def add_order(self, order_id, customer_name, items):
        new_order = OrderNode(order_id, customer_name, items)
        
        if self.tail is None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order
        print(f"Order {order_id} added for {customer_name}.")

    def serve_order(self):
        if self.head is None:
            print("No orders to serve.")
            return
        served_order = self.head
        print(f"Serving order {served_order.order_id} for {served_order.customer_name}.")
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def display_orders(self):
        if self.head is None:
            print("No current orders.")
            return
        print("Current orders in queue:")
        current = self.head
        while current:
            print(f"Order ID: {current.order_id}, Customer: {current.customer_name}, Items: {current.items}")
            current = current.next

    def estimated_waiting_time(self, order_id):
        current = self.head
        waiting_time = 0
        found = False
        
        while current:
            waiting_time += len(current.items) * self.average_prep_time
            if current.order_id == order_id:
                found = True
                break
            current = current.next
        
        if found:
            print(f"Estimated waiting time for order {order_id} is approximately {waiting_time} minutes.")
        else:
            print("Order not found.")

def main_menu(menu_system):
    while True:
        print("\n--- Menu Order System ---")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. Display Orders")
        print("4. Estimated Waiting Time")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            order_id = int(input("Enter order ID: "))
            customer_name = input("Enter customer name: ")
            items = input("Enter items (comma-separated): ").split(',')
            items = [item.strip() for item in items]
            menu_system.add_order(order_id, customer_name, items)
        
        elif choice == '2':
            menu_system.serve_order()
        
        elif choice == '3':
            menu_system.display_orders()
        
        elif choice == '4':
            order_id = int(input("Enter order ID to check waiting time: "))
            menu_system.estimated_waiting_time(order_id)
        
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    menu_system = MenuOrderSystem()
    main_menu(menu_system)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()