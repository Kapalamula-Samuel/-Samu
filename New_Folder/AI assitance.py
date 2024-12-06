# program for customer service

def customer_service_bot():
    """Simulates a simple customer service bot."""

    print("Welcome to our customer support!")
    print("How can I assist you today?")

    while True:
        user_input = input("Enter your issue or type 'exit' to quit: ").lower()

        if user_input == "exit":
            print("Thank you for contacting us. Goodbye!")
            break
        elif "order" in user_input or "shipping" in user_input:
            print("Please provide your order number.")
            order_number = input("Order number: ")
            print(f"Checking the status of order {order_number}...")
            # In a real application, you would query a database here
            print("Your order is currently being processed.")
        elif "return" in user_input or "refund" in user_input:
            print("Please provide your order number and reason for return/refund.")
            # ... Handle return/refund process ...
            print("We'll get back to you regarding your request shortly")
        elif "billing" in user_input:
            print("Please provide your account details.")
            # ... handle billing inquiry ...
            print("Your billing information was updated")
        else:
            print("I'm sorry, I didn't understand your request. Please rephrase or contact a human representative.")

customer_service_bot()
