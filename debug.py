def main():
    # Import required classes
    from customer import Customer
    from coffee import Coffee
    from order import Order

    # Clear existing data
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()

    # Create test customers
    customers = {
        "leo": Customer("Leonardo"),
        "tina": Customer("Tina")
    }

    # Create test coffee items
    coffees = {
        "latte": Coffee("Galaxy Latte"),
        "espresso": Coffee("Phoenix Espresso")
    }

    # Create test orders
    orders = [
        Order(customers["leo"], coffees["latte"], 5.0),
        Order(customers["leo"], coffees["espresso"], 4.5),
        Order(customers["tina"], coffees["latte"], 6.0),
        Order(customers["tina"], coffees["espresso"], 3.5)
    ]

    def test_customer_properties():
        """Test customer-related functionality"""
        print("\nCustomer Tests:")
        leo = customers["leo"]
        print(f"{leo.name}'s orders: {len(leo.orders())} (expected: 2)")
        print(f"{leo.name}'s coffee types: {len(leo.coffees())} (expected: 2)")
        
        new_order = leo.create_order(coffees["espresso"], 3.5)
        print(f"New order price: {new_order.price} (expected: 3.5)")

    def test_coffee_properties():
        """Test coffee-related functionality"""
        print("\nCoffee Tests:")
        latte = coffees["latte"]
        print(f"{latte.name} orders: {latte.num_orders()} (expected: 2)")
        print(f"Average price: {latte.average_price():.1f} (expected: 5.5)")
        
        espresso = coffees["espresso"]
        print(f"{espresso.name} average price: {espresso.average_price():.1f} (expected: 4.0)")

    def test_top_customers():
        """Test customer spending analysis"""
        print("\nTop Customer Tests:")
        latte_lover = Customer.most_aficionado(coffees["latte"])
        espresso_lover = Customer.most_aficionado(coffees["espresso"])
        
        print(f"Latte top customer: {latte_lover.name} (expected: Tina)")
        print(f"Espresso top customer: {espresso_lover.name} (expected: Leonardo)")

    def test_validations():
        """Test input validation"""
        print("\nValidation Tests:")
        def set_invalid_price():
            orders[0].price = 0.5
            
        tests = [
            ("Empty customer name", lambda: Customer("")),
            ("Short coffee name", lambda: Coffee("X")),
            ("Invalid price", set_invalid_price)
        ]
        
        for description, test in tests:
            try:
                test()
            except ValueError as e:
                print(f"Validation caught: {description} - {e}")

    # Execute all tests
    test_customer_properties()
    test_coffee_properties()
    test_top_customers()
    test_validations()

    print("\nAll tests completed successfully.")

if __name__ == "__main__":
    main()