# 🐞 Defect Log — Online Bookstore System

| Bug ID        | Summary                                                          | Severity | Priority | Environment                 | Affected FR(s)                                         | Status      | Date Reported |
| ------------- | ---------------------------------------------------------------- | -------- | -------- | --------------------------- | ------------------------------------------------------ | ----------- | ------------- |
| BUG-CART-01   | Cart item deletion occurs without user confirmation              | Critical | High     | Chrome v119 / Windows 10    | FR-O01 (Cart Operations)                               | Open        | 05/11/2025    |
| BUG-CART-02   | “Buy Now” updates cart count but does not redirect to cart       | Major    | High     | Firefox v118 / Ubuntu 22.04 | FR-O01 (Cart Operations), FR-O02 (Checkout Wizard)     | In Progress | 05/11/2025    |
| BUG-SEARCH-03 | Search bar does not return results for available catalog items   | Major    | Medium   | Edge v119 / Windows 11      | FR-M01 (Catalog CRUD), FR-Catalog (Search/Filter/Sort) | Open        | 05/11/2025    |
| BUG-PRICE-04  | Product prices do not update after currency configuration change | Major    | High     | Chrome v119 / Windows 10    | FR-O01 (Price Display Logic), FR-X01 (Compatibility)   | Open        | 06/11/2025    |

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

### BUG-SEARCH-03 — Search Bar Returns No Matching Results

**Affected FR(s):** FR-M01 (Catalog CRUD), FR-Catalog (Search/Filter/Sort)  
**Severity:** Major  
**Priority:** Medium  
**Environment:** Edge v119, Windows 11

**Steps to Reproduce:**

1. Navigate to catalog.
2. Search for a known existing book title or author.

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
