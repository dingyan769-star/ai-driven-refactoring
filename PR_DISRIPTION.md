## 1. Identified Code Smells

1. Long Method (calculate_shipping_fee in Order class)
   - The method handles multiple concerns, including country-based shipping calculation and VIP discount application.
   - This results in low cohesion and makes the method harder to read, test, and maintain.

2. Single Responsibility Principle (SRP) Violation (Order class)
   - The Order class is responsible for data storage (customer, country, weight), business logic (shipping fee calculation), and presentation (print_order).
   - This violates SRP, as the class has multiple reasons to change.

3. Open/Closed Principle (OCP) Violation (country-based conditional logic)
   - The use of if/elif statements for handling different countries requires modification of existing code when adding new countries.
   - This makes the system less extensible and increases the risk of introducing bugs.

4. Excessive Conditional Logic (PaymentProcessor class)
   - The process_payment method relies on if/elif statements to handle different payment types.
   - This approach does not scale well and violates OCP, as new payment methods require modifying existing logic.

5. Data Clumps / Primitive Obsession (Order class attributes)
   - The use of primitive data types (e.g., country as string, is_vip as boolean) directly in business logic indicates a lack of domain modeling.
   - This reduces expressiveness and makes the system harder to extend (e.g., adding more complex pricing rules).

6. Low Cohesion (Order class)
   - The responsibilities within the Order class are not closely related (data, calculation, and printing).
   - This decreases maintainability and increases the likelihood of unintended side effects during changes.

   ## 2. AI Collaboration Log

### Prompt 1: Code Smell Identification

Prompt:
"Analyze the following Python code and identify at least 5 code smells. 
Explain why each is problematic in terms of software design principles."

AI Response (Summarized):
- Long Method: The shipping calculation method combines multiple responsibilities.
- SRP Violation: The Order class handles multiple concerns (data, logic, and output).
- OCP Violation: The use of conditional logic prevents easy extension.
- Excessive Conditional Logic: if/elif structures reduce scalability.
- Primitive Obsession: Use of raw data types instead of domain models.

---

### Prompt 2: Refactoring Strategy Suggestions

Prompt:
"Propose 3 different refactoring strategies for this code. Include pros and cons of each."

AI Response (Summarized):

1. Extract Method
   - Pros: Improves readability and modularity
   - Cons: Does not fully solve extensibility issues

2. Strategy Pattern
   - Pros: Eliminates conditional logic and improves scalability
   - Cons: Introduces additional classes and complexity

3. Split Class (SRP-based refactoring)
   - Pros: Improves cohesion and separation of concerns
   - Cons: Requires restructuring multiple parts of the system

   ## 3. Decision & Review Process

We evaluated multiple refactoring strategies proposed by the AI, including Extract Method, Strategy Pattern, and Split Class.

After careful consideration, we selected the Strategy Pattern as the primary refactoring approach.

### Evaluation of Options:

1. Extract Method
   - Pros: Improves readability by breaking down long methods.
   - Cons: Does not address the core issue of extensibility and still relies on conditional logic.

2. Split Class (SRP-based refactoring)
   - Pros: Improves separation of concerns and class cohesion.
   - Cons: While it addresses SRP violations, it does not eliminate the conditional logic problem.

3. Strategy Pattern (Selected)
   - Pros:
     - Eliminates if/elif conditional logic by introducing polymorphism
     - Fully supports the Open/Closed Principle (OCP)
     - Makes the system easily extensible for new shipping or payment types
   - Cons:
     - Introduces additional classes, slightly increasing system complexity

### Final Decision:

We selected the Strategy Pattern because it directly addresses the most critical design issue: lack of extensibility due to conditional logic.

Although it introduces more classes, the long-term benefits in scalability, maintainability, and adherence to SOLID principles outweigh the added complexity.

## 4. Improved Design

- Replaced country-based conditional logic with Strategy Pattern
- Introduced ShippingStrategy abstraction and concrete implementations (KR, US, Default)
- Eliminated if/elif logic and improved code readability
- Improved extensibility: new shipping rules can be added without modifying existing code
- Reduced coupling between Order and shipping logic
- Maintained original functionality while improving system design