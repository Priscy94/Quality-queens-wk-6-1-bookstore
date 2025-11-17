# Test Plan document for a Bookstore E-commerce Platform

**Level:** Intermediate QA
**Course:** Software Testing & Quality Assurance  
**Project Type:** Final Project 
**Submission Date:** 05/11/2025

## Team Information

| Role          | Name                | Responsibilities                                         |
| ------------- | ------------------- | -------------------------------------------------------- |
| Test Manager  | Prisca Wamboka      | Planning, scheduling, coordination, metric tracking      |
| Risk Analyst  | Ivy Nagide          | Risk identification, prioritization, test design linkage |
| Test Executor | Thembisile Nkambule | Execution, evidence capture, defect logging    
|
 ## Project Overview

System Under Test: Bookstore app (e-commerce platform)  
Technology Stack: React, Tailwind CSS, JavaScript  
Environment:Latest 2 of Chrome/Firefox/Safari/Microoft Edge; responsive breakpoints 

### Features Under Test

- Book catalog & earch functionality
- User accounts & authentication
- Shopping cart & checkout process
- Inventory management
- Order tracking system

  ## Test Plan

### Objectives & Scope

This test plan defines the strategy for validating the Bookstore App’s core features, ensuring they meet functional, accessibility, performance and compatibility standards. It focuses on catalog discovery, shopping cart and checkout process, payments, order tracking and admin workflows.

- Functional Testing – Verify that book cards display correct data, cart and checkout workflows behave as expected and payment status updates are accurate.
- User Interface Testing – Ensure book cards, buttons, and layout are visually aligned, responsive and readable across devices.
- Accessibility Testing – Confirm keyboard navigation, screen reader labels, and ARIA roles are correctly implemented.
- Business Logic Testing – Validate price formatting, cart limits, coupon rules and order status transitions.
- User Experience Testing – Ensure intuitive browsing, fast feedback and smooth purchase flow.
- Security Testing – Confirm input validation and safe rendering of user-generated content.


## Scope
### In-Scope 
| In-Scope Objective                                               | Mapped FR Code(s)                                      |
|------------------------------------------------------------------|--------------------------------------------------------|
| Catalog browse titles, search, filter and sort                   | FR-M01 (Catalog CRUD), FR-Catalog (search/filter/sort) |
| Cart operations, coupon applications and checkout steps          | FR-O01 (Cart ops), FR-O02 (Checkout wizard), FR-M05 (Promotions) |
| Paystack payment flow and order status updates                   | FR-O03 (Payment), FR-O05 (Order lifecycle)             |
| Tracking order history, CSV export, returns/refunds              | FR-O04 (Order history/export), FR-R01–R03 (Returns/Refunds) |
| Reviews, Q&A and moderation workflows                            | FR-U01 (Reviews), FR-U02 (Moderation), FR-U03 (Q&A sanitation) |
| Admin console actions (CRUD, inventory, order management)        | FR-M01–M04 (Catalog, Inventory, Orders, Moderation)    |
| Notifications and badge behavior                                 | FR-N01 (Notifications), FR-N02 (Mark all read)         |
| Accessibility, performance and compatibility checks              | FR-X01–X04 (A11y, Performance, Compatibility, Security) |


### Out-of-Scope
- Backend services or payment capture
- Storage of personal data
- Taxes beyond 8% fixed rate
- Shipping carriers or logistics integrations


## Test Types
|      Types        | Tests | 
|-------------------|------------|
|Functional Testing |Unit, Integration, System, UAT|
|Non-functional Testing|Performance, Accessibility, Usability, Compatibility, Security Hygiene|
|Negative Testing      |Boundary cases, validation errors|
|Retesting & Regression Testing |Testing code after new changes|


## Test Strategy
- Manual Testing - Jest testing framework for unit testing
- Automation Testing - Selenium IDE


## Resources
- Resources (Required personnel): Test manager, Risk analyst & Test executor
- Browsers - Latest 2 of Chrome/Firefox/Safari/Microoft Edge; responsive breakpoints
- Devices - Standard PC/Laptop, Tablet and Mobile 
- Tools - Node.js, Jest testing framework, Local Git repo, VS Code, Github projects (github issues and Kanban Board for project tracking), Snipping tool for screenshots
- Throttling: Simulated 3G for performance testing; offline mode for error handling



# Test Schedule
|            Activity           | Start Date | End Date |
|-------------------------------|------------|----------|
|Planning and setup             | 31/10/2025 | 05/11/2025|
|Test Design and Early Execution|06/11/2025|11/11/2025|
|Final Execution and Reporting  |10/112025/|18/11/2025|

# Roles and Responsibility 
| Name              | Role        |Responsibility|
|-------------------|-------------|-----------------|  
|Prisca Wamboka|Test Manager|Planning, scheduling, coordination, metric tracking|
|Ivy Nagide|Risk analyst|Risk identification, prioritization, test design linkage|     
|Thembisile Nkambule|Test executor|Execution, evidence capture, defect logging|

# Risks and Mitigations

| Risk |Impact | Mitigation |
|------|------------|----------------|
|Tool installation failure     |Testing delays      |Have backup environment|
|Time restrictions             |Incomplete testing  |Prioritize high-risk tests|
|Unclear/Ambiguous requirements|Incorrect test cases|Request clarification|
|Variation in browsers/devices |Issues with rendering|Cross-browser testing|

# Criteria

## Entry Criteria

- Functional requirements have been recorded, assessed and authorized.
- The test plan, test cases and test data have been finalized and assessed.
- The team has access to admin credentials and seed data.
- All necessary resources and tools are accessable (Browser, Node.js, Jest testing framework, Local Git repo, VS Code).
- Team roles and responsibilities assigned.

## Exit Criteria
- All planned test cases have been executed (P1, P2, P3).
- No Critical or High severity bugs remain open.
- All Regression testing is passed.
- Every identified defect is recorded and understood.
- Product Owner / Stakeholder has reviewed results and signed off for release.

## Acceptance / Exit Criteria

- All P1 and P2 test cases executed
- No Critical/High severity defects open
- Payment, checkout, admin guards validated
- CSV export verified
- A11y and security hygiene checks complete

### Exit not allowed if:
- Payments, checkout or admin guards are failing.
- Any security/A11y compliance defects are Critical.

### If exit criteria pass:
- testing is complete and product may proceed to release.