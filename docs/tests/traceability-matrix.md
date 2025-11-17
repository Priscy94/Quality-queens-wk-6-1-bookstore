# Requirements Traceability Matrix
## E-commerce Bookstore Application, v1.0.0
**Document ID:** RTM-BOOK-2025-001
**Date:** November 18, 2025

## Team Information

| Role          | Name                | Responsibilities                                         |
| ------------- | ------------------- | -------------------------------------------------------- |
| Test Manager  | Prisca Wamboka      | Planning, scheduling, coordination, metric tracking      |
| Risk Analyst  | Ivy Nagide          | Risk identification, prioritization, test design linkage |
| Test Executor | Thembisile Nkambule | Execution, evidence capture, defect logging| 

### Purpose
- This document provides a mapping between the high-level Functional Requirements (FRs), the Test Cases designed to verify them and the Defects logged against them. This ensures all requirements have been tested and provides visibility into the quality of each feature.

### Traceability Matrix

| Requirement ID | Requirement Description / Area | Test Case IDs | Defect IDs | Verification Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-Catalog** | **Catalog Search, Filter & Sort** | | | **PASSED** | Core search functionality is robust. |
| | View All Books | TC-BOOK-01 | | PASSED | |
| | View Book Details | TC-BOOK-02 | | PASSED | |
| | Search by Full/Partial Title & Author | TC-BOOK-03, TC-BOOK-04, TC-BOOK-05, TC-BOOK-06 | | PASSED | |
| | Clear Search Filters | TC-BOOK-07 | | PASSED | |
| | Sort Results (Price, Title) | TC-BOOK-08, TC-BOOK-09 | | **FAILED** | Sorting logic is not implemented. |
| | Handle No Search Results | TC-BOOK-10 | | PASSED | |
| **FR-O01** | **Shopping Cart Operations** | | | **FAILED** | **Critical defects present.** |
| | Add Item to Cart | TC-CART-01 | | PASSED | |
| | View Cart Items | TC-CART-02 | | PASSED | |
| | Remove Item from Cart | TC-CART-03 | BUG-CART-01 | **FAILED** | **Critical:** No user confirmation. |
| | Update Item Quantity | TC-CART-04 | | PASSED | |
| | Validate Stock Limit | TC-CART-05 | BUG-CART-04 | **FAILED** | **Critical:** Stock is unlimited. |
| | Persist Cart Data | TC-CART-06 | | PASSED | |
| | Calculate Totals (Subtotal, Tax, Total) | TC-CART-07, TC-CART-08, TC-CART-09 | | PASSED | |
| | Apply Coupon Code | TC-CART-10 | | **FAILED** | UI for coupon application not found. |
| | Checkout Form Validation | TC-CART-11, TC-CART-12 | BUG-CHECKOUT-01 | **FAILED** | **Minor:** Lacks alphanumeric validation. |
| | Review Order Summary | TC-CART-13 | | PASSED | |
| | Prevent Checkout with Empty Cart | TC-CART-14 | | PASSED | |
| **FR-O02** | **Checkout Wizard** | TC-PAY-01 | | PASSED | Checkout flow navigation works correctly. |
| **FR-O03** | **Payment Processing** | | | **PASSED** | Paystack integration is functional. |
| | Initialize Payment Gateway | TC-PAY-02 | | PASSED | |
| | Handle Supported Currencies | TC-PAY-03 | | PASSED | |
| | Handle Unsupported Currencies | TC-PAY-04 | | PASSED | |
| | Correct Amount Conversion | TC-PAY-05 | | PASSED | |
| | Handle Payment Cancellation | TC-PAY-06 | | PASSED | |
| | Handle Payment Failure | TC-PAY-07 | | PASSED | |
| | Handle Payment Success | TC-PAY-08, TC-PAY-09 | | PASSED | |
| **FR-M01** | **Admin Catalog CRUD** | | | **FAILED** | **Critical defects present.** |
| | Admin Login & Access Control | TC-ADMIN-01, TC-ADMIN-02 | | PASSED | (Via browser console method) |
| | Create New Book (Add) | TC-ADMIN-03 | BUG-ADMIN-01 | **FAILED** | **Critical:** CRUD operations not functional. |
| | Update Existing Book (Edit) | TC-ADMIN-04 | BUG-ADMIN-01 | **FAILED** | **Critical:** CRUD operations not functional. |
| | Delete Book | TC-ADMIN-05 | BUG-ADMIN-01 | **FAILED** | **Critical:** CRUD operations not functional. |
| **FR-M02** | **Inventory Management** | | | **FAILED** | **Critical defect present.** |
| | Low Stock Warnings | (Implicit in Admin features) | BUG-ADMIN-02 | **FAILED** | **Critical:** No low-stock alerts. |
| **FR-X01** | **Compatibility & Responsiveness** | TC-NFR-01 | | PASSED | Layout is responsive across devices. |
| **FR-X02** | **Accessibility** | TC-NFR-03 | BUG-CART-03 | **PARTIAL** | Keyboard nav works, but hover states are missing. |
| **FR-X03** | **Performance** | TC-NFR-04 | | **FAILED** | Lazy loading not implemented. |
| **FR-X04** | **Security & Validation** | TC-NFR-02 | BUG-CHECKOUT-01 | **PARTIAL** | Basic validation exists; lacks input type checks. |

### Summary & Analysis

- **Requirements Covered:** 100% of the in-scope functional areas have corresponding test cases.
- **Overall Test Status:** **AT RISK.** 4 out of 9 requirement areas have a FAILED status due to critical and major defects.
- **Key Quality Gaps:**
    1.  **Admin Module (FR-M01, FR-M02):** Complete failure of CRUD operations and inventory alerts.
    2.  **Cart Operations (FR-O01):** Critical flaws in stock validation and user experience (no delete confirmation).
    3.  **Core Features (FR-Catalog, FR-O02, FR-O03):** These areas are generally stable and passed testing, with minor exceptions.

- This matrix clearly shows that the application cannot be released until the requirements with a **FAILED** status, particularly those linked to Critical defects, are resolved and re-tested.