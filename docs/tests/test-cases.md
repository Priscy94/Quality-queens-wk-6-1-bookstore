# ✅ Test Cases — Online Bookstore System

## Legend

- **Role:** U (User), A (Admin)
- **FR Code:** Maps to functional requirements traced from SRS

---

# ✅ Test Cases — Online Bookstore System

## Legend

- **Role:** U (User), A (Admin)
- **FR Code:** Maps to functional requirements traced from SRS

---

### 1. Book Browsing & Search

| ID         | Title                         | Pre-Conditions          | Steps                                                 | Expected Result                                   | FR Code | Evidence                | Status     |
| ---------- | ----------------------------- | ----------------------- | ----------------------------------------------------- | ------------------------------------------------- | ------- | ----------------------- | ---------- |
| TC-BOOK-01 | View All Books from Home Page | User logged in or guest | 1. Visit home page 2. Scroll book listings            | All available books displayed in grid/card format | FR-B01  | screenshots/book-01.png | PASS       |
| TC-BOOK-02 | View Book Details Page        | Book data exists        | 1. Click any book card 2. View details                | Title, author, price & description displayed      | FR-B02  |                         | PASS       |
| TC-BOOK-03 | Search book by full title     | Books seeded            | 1. Use search bar 2. Enter exact book title 3. Search | Matching book(s) displayed                        | FR-B03  |                         | Not Tested |
| TC-BOOK-04 | Search using partial keyword  | Books seeded            | 1. Type partial term e.g., “pot” for “Harry Potter”   | Suggested / filtered results displayed            | FR-B03  |                         | PASS       |

---

### 2. Shopping Cart

| ID         | Title                 | Pre-Conditions      | Steps                                       | Expected Result                                 | FR Code | Evidence | Status |
| ---------- | --------------------- | ------------------- | ------------------------------------------- | ----------------------------------------------- | ------- | -------- | ------ |
| TC-CART-01 | Add a book to cart    | Logged in           | 1. Open book details 2. Click “Add to Cart” | Cart count increments and item appears in cart  | FR-C01  |          | PASS   |
| TC-CART-02 | View cart items       | Items in cart       | 1. Click cart icon                          | All added books displayed with price & quantity | FR-C02  |          | PASS   |
| TC-CART-03 | Remove item from cart | Item exists in cart | 1. Click “Remove” beside any item           | Item removed and totals updated                 | FR-C02  |          | PASS   |

---

### 3. Checkout & Payment

| ID        | Title                          | Pre-Conditions     | Steps                                                     | Expected Result                                 | FR Code | Evidence               | Status     |
| --------- | ------------------------------ | ------------------ | --------------------------------------------------------- | ----------------------------------------------- | ------- | ---------------------- | ---------- |
| TC-PAY-01 | Proceed to Checkout            | Cart has ≥1 item   | 1. Open cart 2. Click “Checkout”                          | Redirected to checkout page                     | FR-P01  | screenshots/pay-01.png | Not Tested |
| TC-PAY-02 | Complete Payment               | Checkout page open | 1. Select M-Pesa 2. Enter phone number 3. Confirm payment | Payment success message & receipt generated     | FR-P02  |                        | Not Tested |
| TC-PAY-03 | Payment Cancellation / Failure | Payment initiated  | 1. Cancel transaction from modal                          | Error message displayed, cart remains unchanged | FR-P02  |                        | PASS       |

---

### 4. Admin Inventory Management

| ID          | Title             | Pre-Conditions       | Steps                                                | Expected Result                                 | FR Code | Evidence                 | Status     |
| ----------- | ----------------- | -------------------- | ---------------------------------------------------- | ----------------------------------------------- | ------- | ------------------------ | ---------- |
| TC-ADMIN-01 | Admin Login       | Admin account exists | 1. Login with admin credentials                      | Redirect to Admin Dashboard                     | FR-AD01 | screenshots/admin-01.png | PASS       |
| TC-ADMIN-02 | Add New Book      | Logged in as Admin   | 1. Navigate to Inventory 2. Add book details 3. Save | New book appears in product list                | FR-AD02 |                          | Not Tested |
| TC-ADMIN-03 | Edit Book Details | Book exists          | 1. Select book 2. Edit fields 3. Save                | Updated information reflects in product listing | FR-AD03 |                          | Not Tested |

---

## ✅ Detailed Test Cases — Online Bookstore System

---

## 1) Catalog & Search

### TC-CAT-01

- **ID:** TC-CAT-01
- **Title:** Load Book Catalog
- **Pre-conditions:** Application running; user is on `/catalog`
- **Steps:**
  1. Navigate to `/catalog`
- **Expected Result:** Books displayed in list/grid with title, author, price, and action button.
- **Post-conditions:** None
- **Evidence:**

### TC-SRCH-02

- **ID:** TC-SRCH-02
- **Title:** Search Books with Matching Keyword
- **Pre-conditions:** Catalog contains searchable book titles
- **Steps:**
  1. Navigate to `/catalog`
  2. Enter a known book title in the search bar
- **Expected Result:** Matching books only are displayed.
- **Post-conditions:** None
- **Evidence:**

### TC-SRCH-03

- **ID:** TC-SRCH-03
- **Title:** Search Produces No Results
- **Pre-conditions:** Catalog loaded
- **Steps:**
  1. Enter a random string (e.g., `xzqplm`) into search bar
- **Expected Result:** “No results found” or empty-state UI displayed.
- **Post-conditions:** None
- **Evidence:**

---

## 2) Shopping Cart

### TC-CART-01

- **ID:** TC-CART-01
- **Title:** Add Single Book to Cart
- **Pre-conditions:** Catalog page open
- **Steps:**
  1. Click **Buy Now** on any book
- **Expected Result:** Cart count increases; book appears in cart summary.
- **Post-conditions:** Cart stored in localStorage.
- **Evidence:**

### TC-CART-02

- **ID:** TC-CART-02
- **Title:** Update Book Quantity in Cart
- **Pre-conditions:** Cart contains ≥ 1 item
- **Steps:**
  1. Navigate to `/cart`
  2. Click `+` to increase item quantity
- **Expected Result:** Quantity increases and subtotal recalculates correctly.
- **Post-conditions:** Updated cart stored in localStorage.
- **Evidence:**

### TC-CART-03

- **ID:** TC-CART-03
- **Title:** Remove Book from Cart
- **Pre-conditions:** Cart contains ≥ 1 item
- **Steps:**
  1. Navigate to `/cart`
  2. Click **Remove** beside item
- **Expected Result:** Item removed from cart; totals update.
- **Post-conditions:** Cart state updated.
- **Evidence:**

---

## 3) Checkout & Payment

### TC-CHK-01

- **ID:** TC-CHK-01
- **Title:** Proceed to Checkout
- **Pre-conditions:** Cart contains ≥ 1 item
- **Steps:**
  1. Navigate to `/cart`
  2. Click **Proceed to Checkout**
- **Expected Result:** Redirect to `/checkout` with order summary.
- **Post-conditions:** Checkout session initialized.
- **Evidence:**

### TC-PAY-02

- **ID:** TC-PAY-02
- **Title:** Attempt Payment with Missing Paystack Key
- **Pre-conditions:** Invalid / missing Paystack key in `.env`
- **Steps:**
  1. On `/checkout`, click **Pay Now**
- **Expected Result:** System blocks transaction and shows warning.
- **Post-conditions:** No order created.
- **Evidence:**

---

## 4) Currency Configuration

### TC-CURR-01

- **ID:** TC-CURR-01
- **Title:** Currency Change Reflects in Pricing
- **Pre-conditions:** `.env` currency configured; application restarted
- **Steps:**
  1. Change currency in `.env`
  2. Restart server
  3. Reload `/catalog`
- **Expected Result:** Price symbol and conversion update across system.
- **Post-conditions:** None
- **Evidence:**

---

## 5) Admin Access Control

### TC-ADMIN-01

- **ID:** TC-ADMIN-01
- **Title:** Non-Admin Access Restriction
- **Pre-conditions:** User role ≠ admin
- **Steps:**
  1. Navigate to `/admin`
- **Expected Result:** “Unauthorized” access message; no admin UI access.
- **Post-conditions:** None
- **Evidence:**

### TC-ADMIN-02

- **ID:** TC-ADMIN-02
- **Title:** Admin Access to Dashboard
- **Pre-conditions:** User session role = admin
- **Steps:**
  1. Navigate to `/admin`
- **Expected Result:** Admin dashboard loads fully.
- **Post-conditions:** None
- **Evidence:**
