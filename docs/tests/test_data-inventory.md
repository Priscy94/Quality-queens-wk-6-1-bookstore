
#  Test Data Inventory Document**
## Bookstore E-Commerce Bookstore Application, v1.0.0
 **Document ID:** TDI-BOOK-2025-001
 **Date:** November 18, 2025

 ## Team Information

| Role          | Name                | Responsibilities                                         |
| ------------- | ------------------- | -------------------------------------------------------- |
| Test Manager  | Prisca Wamboka      | Planning, scheduling, coordination, metric tracking      |
| Risk Analyst  | Ivy Nagide          | Risk identification, prioritization, test design linkage |
| Test Executor | Thembisile Nkambule | Execution, evidence capture, defect logging    
|

### Purpose
This document catalogs the test data used during the testing cycle for the Bookworm's Corner application. It serves as a reference for test setup, replication of defects, and future regression testing.

### 1. User Accounts

| Role | Username / Method | Password / Setup | Purpose |
| :--- | :--- | :--- | :--- |
| **Standard User** | N/A (No formal login UI) | N/A | Used for all standard user journeys like browsing, cart, and checkout. Session is anonymous. |
| **Administrator** | N/A (No formal login UI) | Execute in Browser Console: `localStorage.setItem('app.user', JSON.stringify({ role: 'admin' }))` | Used to access the Admin Dashboard at `/admin` for testing inventory management features. |

### 2. Book Catalog Data

The application was seeded with a static list of books. The following are examples of key data points used for testing:

| Book Title | Author | Price (USD) | ISBN/ID | Use Case in Testing |
| :--- | :--- | :--- | :--- | :--- |
| To Kill a Mockingbird | Harper Lee | $12.99 | (System Generated) | Primary book for search tests (TC-BOOK-03, TC-BOOK-04, TC-BOOK-05, TC-BOOK-06). |
| The Great Gatsby | F. Scott Fitzgerald | $10.50 | (System Generated) | Used for case-insensitive search tests (TC-BOOK-05). |
| 1984 | George Orwell | $9.99 | (System Generated) | General book for cart and checkout flow tests. |
| Pride and Prejudice | Jane Austen | $11.25 | (System Generated) | General book for cart and checkout flow tests. |


### 3. Shopping Cart & Checkout Data

| Data Field | Sample Test Data 1 | Sample Test Data 2 | Purpose / Notes |
| :--- | :--- | :--- | :--- |
| **Full Name** | `Thembisile Nkambule` | `John Doe` | Tests alphabetic input validation (BUG-CHECKOUT-01). |
| **Email Address** | `thembisile@gmail.com` | `invalid-email.com` | Tests email format validation (TC-CART-12). |
| **Address** | `7 Poplar Ave` | `123 Main Street` | Standard address field. |
| **City** | `Nelspruit` | `Cape Town` | Standard city field. |
| **Country** | `South Africa` | `Kenya` | Standard country field. |
| **Postal Code** | `0458` | `abc123` | Tests numeric input validation (BUG-CHECKOUT-01). |
| **Item Quantity** | `1`, `4` | `1000000` | Tests quantity update (TC-CART-04) and stock validation (TC-CART-05, BUG-CART-04). |

### 4. Payment Gateway Test Data (Paystack Sandbox)

| Data Type | Test Value / Method | Purpose |
| :--- | :--- | :--- |
| **Supported Currencies** | NGN, GHS, USD, ZAR | Configured in `currency.js`/environment to test currency support (TC-PAY-03). |
| **Test Card (Success)** | Select "Success" option in Paystack test modal. | To simulate a successful payment (TC-PAY-08, TC-PAY-09). |
| **Test Card (Failure)** | Select "Decline" option in Paystack test modal. | To simulate a failed payment and test error handling (TC-PAY-07). |
| **Test Card (Authentication)** | Select "Authentication" option in Paystack test modal. | To simulate a payment requiring 3DSecure. |
| **Cancel Payment** | Click "Back" button in Paystack modal. | To test user cancellation flow (TC-PAY-06). |

### 5. Environment & Configuration Data

| Component | Configuration / Value | Purpose |
| :--- | :--- | :--- |
| **Application URL** | `http://localhost:3000` | Base URL for all test execution. |
| **Tax Rate** | 8% (Fixed) | Used for calculating tax in the shopping cart (TC-CART-08). |
| **Shipping Cost** | Logic not explicitly defined in tests. Assumed to be $0 or factored into a fixed total. | --- |
| **Coupon Codes** | N/A | A UI or backend service for applying coupons was not found during testing (TC-CART-10). |

### 6. Data for Negative & Boundary Testing

| Test Case | Data Used | Expected Outcome |
| :--- | :--- | :--- |
| **Empty Form Submission** | Leave all checkout fields blank. | Validation errors for required fields (TC-CART-11). |
| **Invalid Email Format** | `user.name.com`, `user@name` | Validation error for incorrect email format (TC-CART-12). |
| **Excessive Quantity** | `1000000` | Error message for exceeding stock (TC-CART-05). **Actual: Failed (BUG-CART-04).** |
| **Search Non-Existent Book** | `Zulu myths` | "No books found" message (TC-BOOK-10). |
| **Non-Admin Access** | Access `/admin` without setting admin role. | "Unauthorized user" error (TC-ADMIN-02). |

### Summary
This inventory documents the core datasets that were utilized to verify the functionality, validation and error handling of the E-commerce Bookstore application. The data covers positive, negative and boundary scenarios for all in-scope features.