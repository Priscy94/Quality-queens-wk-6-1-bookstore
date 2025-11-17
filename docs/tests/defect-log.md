
\# 🐞 Defect Log — Online Bookstore System

| Bug ID        | Summary     | Severity | Priority | Environment    | Affected FR(s)       | Status      | Date Reported |
| --------------| ----------- | -------- | -------- | -------------- | ---------------------| ----------- | ------------- |
| BUG-CART-01   | Cart item deletion occurs without user confirmation | Critical | High| Chrome v119 / Windows 10 | FR-O01 (Cart Operations)  | Open | 05/11/2025|
| BUG-CART-02   | “Buy Now” updates cart count but does not redirect to cart| Major| High | Firefox v118 / Ubuntu 22.04 | FR-O01 (Cart Operations), FR-O02 (Checkout Wizard)| In Progress | 05/11/2025    |
| BUG-SEARCH-03 | Navbar search does not return results for available catalog items   | Major| Medium | Edge v119 / Windows 11 | FR-M01 (Catalog CRUD), FR-Catalog (Search/Filter/Sort) | Open | 05/11/2025    |
| BUG-PRICE-04  | Product prices do not update after currency configuration change | Major| High| Chrome v119 / Windows 10 | FR-O01 (Price Display Logic), FR-X01 (Compatibility) | Open | 06/11/2025 |
| BUG-CART-03   | Buttons hover not active(Proceed checkout,Next, Payment)| Low | Low | Chrome v119 / Windows 10 |FR-X0 (Accessibility)| Open|13/11/2025|
|BUG-CHECKOUT-01|Form does not validate that the input texts are alphabets or numbers when according to whats required| Low |Low|Chrome v119 / Windows 10|FR-O02 (Checkout wizard )| Open| 13/11/2025|
| BUG-CART-04   |Stock is unlimited(Can add any quantity of an item)| Critical|High|Chrome v119 / Windows 10 |FR-O01 (Cart operations)| Open|13/11/2025|
|BUG-ADMIN-01   |Admin not able to do the CRUD operations| Critical| High | Chrome v119 / Windows 10 |FR-M01 (Catalog CRUD)| Open | 13/11/2025|
|BUG-ADMIN-02   |Admin does not receive low‑stock warnings| Critical | High |Chrome v119 / Windows 10 |FR-M02 (Inventory) | Open |13/11/2025|



---

## Detailed Bug Reports

### BUG-CART-01 — Cart Item Deletion Occurs Without User Confirmation

**Affected FR(s):** FR-O01 (Cart Operations)  
**Severity:** Critical  
**Priority:** High  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

1. Navigate to the Cart page.
2. Click **Remove** on any cart item.

**Expected Result:**  
System should display a confirmation prompt before deleting the item.

**Actual Result:**  
Item is removed immediately without confirmation.

**Notes:**  
High risk of accidental cart data loss.

---

### BUG-CART-02 — “Buy Now” Updates Cart Count but Does Not Redirect to Cart

**Affected FR(s):** FR-O01 (Cart Operations), FR-O02 (Checkout Wizard)  
**Severity:** Major  
**Priority:** High  
**Environment:** Firefox v118, Ubuntu 22.04

**Steps to Reproduce:**

1. Open the product catalog.
2. Click **Buy Now** on any product.

**Expected Result:**  
User should be auto-redirected to **Cart** or shown a confirmation modal.

**Actual Result:**  
Cart count updates, but user remains on the same page with no feedback.

**Notes:**  
User flow interruption; navigation handler not triggered.

---

### BUG-SEARCH-03 — Navbar Search Returns No Matching Results

**Affected FR(s):** FR-M01 (Catalog CRUD), FR-Catalog (Search/Filter/Sort)  
**Severity:** Major  
**Priority:** Medium  
**Environment:** Edge v119, Windows 11

**Steps to Reproduce:**

1. Navigate to catalog.
2. Click on "Search Books..." on the navbar

**Expected Result:**  
Matching books should be displayed in real time.

**Actual Result:**  
Search returns **no results** regardless of input.

**Notes:**  
Likely issue with UI state binding or incomplete filter logic.

---

### BUG-PRICE-04 — Product Prices Do Not Update When Currency is Changed

**Affected FR(s):** FR-O01 (Price Display Logic), FR-X01 (Compatibility & Config Behavior)  
**Severity:** Major  
**Priority:** High  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

1. Modify currency setting in `.env` (e.g., NGN → USD).
2. Restart development server.
3. Refresh product listings.

**Expected Result:**  
Prices should update to reflect the new currency selection.

**Actual Result:**  
Displayed prices remain unchanged.

**Notes:**  
Conversion logic not being executed or cached values blocking update.

### BUG-CART-03 — Buttons Hover Not Active(Proceed checkout,Next, Payment)

**Affected FR(s):** FR-X0 (Accessibility)  
**Severity:**   
**Priority:** Low  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

  1. Navigate to `/catalog`
  2. Click "Buy Now" on a book
  3. Click "Buy Now" on another book
  4. Click checkout icon
  5. Click on "Proceed to checkout"
  6. Fill in the form
  7. Click "Next"
  8. Click "Proceed to Payment"

**Expected Result:**  
When hovering on the button it must show buy change the buttons color

**Actual Result:**  
When hovering on a button the color remains the same

**Notes:**  
CSS button hover not active


### BUG-CHECKOUT-01 — Form does not validate that the input texts are alphabets or numbers  according to whats required

**Affected FR(s):** FR-O02 (Checkout wizard )
**Severity:**   
**Priority:** Low  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

  1. Navigate to `/catalog`
  2. Click "Buy Now" on a book
  3. Click "Buy Now" on another book
  4. Click checkout icon
  5. Click on "Proceed to checkout"
  6. Fill in the form
  7. Input number where alphabets are required and alphabets where numbers are required

**Expected Result:**  
Error message "Only alphabets are required",  Error message "Only numbers are required"

**Actual Result:**  
Allows you to input any characters

**Notes:**  
Form input validation

### BUG-CART-04 — Stock is unlimited (Can add any quantity of an item)

**Affected FR(s):** FR-O02 (Checkout wizard )
**Severity:**   Critical
**Priority:** High  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

  1. Navigate to `/catalog`
  2. Click "Buy Now" on a book
  3. Crick the cart icon
  4. Increase the quantity to 1000000 (1 million)

**Expected Result:**  
Error message "The amount of items added is not available. Only 10 items are in stock."

**Actual Result:**  
Allows you to input any quantity

**Notes:**  
quantities with stock not enforcement 



### BUG-ADMIN-01 — Admin not able to do the CRUD operations

**Affected FR(s):** FR-M01 (Catalog CRUD)
**Severity:**   Critical
**Priority:** High  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

  1. Open the launch web browser terminal
  2. Type `localStorage.setItem('app.user', JSON.stringify({ role: 'admin' }))`
  3. http://localhost:3000/admin
  4. Click "Catalog CRUD"

**Expected Result:**  
Admin can create/update/delete titles and metadata... message "Successfully  create/update/delete"

**Actual Result:**  
Admin cannot create/update/delete titles and metadata

**Notes:**  




### BUG-ADMIN-02 - Admin does not receive low‑stock warnings
**Affected FR(s):** FR-M02 (Inventory)
**Severity:**   Critical
**Priority:** High  
**Environment:** Chrome v119, Windows 10

**Steps to Reproduce:**

  1. Open the launch web browser terminal
  2. Type `localStorage.setItem('app.user', JSON.stringify({ role: 'admin' }))`
  3. http://localhost:3000/admin
  4. Click "Inventory"

**Expected Result:**  
Warning message "The stock is low-- only 10 books left"

**Actual Result:**  
Admin does not receive low‑stock warnings

**Notes:**  


