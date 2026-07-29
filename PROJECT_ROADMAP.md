# Smart Subscription Manager

## Project Roadmap

---

# Project Progress


| Sprint                                | Status        |
| ------------------------------------- | ------------- |
| Sprint 1 – Project Setup              | ✅ Complete    |
| Sprint 2 – Dashboard UI               | ✅ Complete    |
| Sprint 3 – Database Integration       | ✅ Complete    |
| Sprint 4 – Add Subscription           | ✅ Complete    |
| Sprint 5 – Edit & Delete Subscription | ✅ Complete    |
| Sprint 6 – Dashboard Statistics       | ✅ Complete    |
| Sprint 7 – UI / UX Improvements       | ✅ Complete    |
| Sprint 8 – Dashboard Analytics        | ✅ Complete    |
| Sprint 9 – Charts & Reports           | ✅ Complete    |
| Sprint 10 – Renewal Management        | ⬜ In Progress |
| Sprint 11 – User Authentication       | ⬜ Not Started |
| Sprint 12 – Deployment & Portfolio    | ⬜ Not Started |




## Project Overview

Smart Subscription Manager is a Flask-based web application that helps users manage recurring subscriptions, monitor spending, visualize analytics, track renewals, and receive renewal reminders through an intuitive dashboard.

---



# Sprint 8 – Dashboard Analytics



## Analytics Cards

- [x] Total Yearly Spending
- [x] Most Expensive Subscription
- [x] Cheapest Subscription
- [x] Spending by Category
- [x] Upcoming Renewals Summary



## Dashboard Improvements

- [x] Better empty state
- [x] Responsive analytics cards
- [x] Better dashboard layout
- [x] Hide duplicate Add Subscription button in empty state
- [x] Different empty states for no data vs no search results



## Testing

- [x] Test yearly calculations
- [x] Test category totals
- [x] Test edge cases
- [x] Test responsive layout
- [x] Test on real mobile device
- [x] Test empty search results



## UI Polish

- [x] Improve Spending by Category presentation
- [x] Consistent analytics card heights



## Git

- [x] Commit Sprint 8
- [x] Push to GitHub



## Bugs Found During QA

- [x] Apply renewal date validation to Edit Subscription
- [x] Strengthen Add Subscription renewal-date validation
- [x] Improve dashboard controls on small screens

---



# Sprint 9 – Charts & Reports



## Sprint Goal

Add clear visual charts and report summaries that help users understand their subscription spending and status.

---



## Charts

- [x] Set up chart library
- [x] Prepare chart data in Flask
- [x] Estimated Monthly Cost Breakdown
- [x] Category Spending Chart
- [x] Active vs Paused vs Cancelled Chart
- [x] Add empty states for charts
- [x] Make charts responsive
- [x] Assign fixed colors for categories and statuses

---



## Reports

- [x] Create Reports page
- [x] Add navigation between Dashboard and Reports
- [x] Monthly Spending Summary
- [x] Yearly Spending Summary
- [x] Subscription Status Summary
- [x] Upcoming Renewal Summary



### Reports Page Layout

- [x] Create report cards
- [x] Add summary sections
- [x] Make responsive
- [x] Style upcoming renewal items

---



## Testing

- [x] Test charts with multiple subscriptions
- [x] Test charts with one subscription
- [x] Test charts with no subscriptions
- [x] Test charts with no active subscriptions
- [x] Test different billing frequencies
- [x] Test active, paused, and cancelled subscriptions
- [x] Test responsive chart layout
- [x] Test Reports page on desktop
- [x] Test Reports page on mobile
- [x] Test fixed category colors remain consistent
- [x] Test dashboard with mixed subscription statuses and categories

---



## UI Polish

- [x] Use consistent chart card styling
- [x] Add chart titles and descriptions
- [x] Add clear empty-state messages
- [x] Ensure chart labels are readable
- [x] Improve currency formatting (฿)
- [x] Ensure report sections have consistent spacing
- [x] Highlight the active navigation link
- [x] Use comma-separated currency formatting across Dashboard and Reports

---



## Technical Debt

- [x] Organize JavaScript
- [x] Add comments where necessary
- [x] Verify monthly cost calculation uses shared helper functions

---



## Git

- [x] Commit Sprint 9
- [x] Push Sprint 9 to GitHub

---



## Bug Fix List

- [x] Preserve entered values and highlight invalid fields on both Add and Edit Subscription forms

---



## Sprint Outcome

Completed:

- Dashboard analytics with Chart.js
- Three interactive charts
- Reports page
- Report summaries
- UI polish and navigation improvements
- Add and Edit form value preservation
- Inline validation messages and invalid-field highlighting

Status:
✅ Sprint 9 Complete

# Sprint 10 – Renewal Management



## Phase 1 – Planning & Database Design



### 10.1 Database Design

- [x] Review current Subscription model
- [x] Compare one-table vs two-table design
- [x] Decide to use a separate RenewalHistory table
- [x] Finalize database schema
- [x] Update ERD documentation



### 10.2 Renewal Logic

- [x] Define "Days Remaining"
- [x] Define "Due Today"
- [x] Define "Overdue"
- [x] Define automatic next renewal calculation
- [x] Define renewal workflow



### 10.3 Navigation & Page Planning

- [x] Keep Upcoming Renewals on Dashboard
- [x] Create dedicated Renewals page
- [x] Add Renewals navigation item
- [ ] Add notification badge to Renewals navigation
- [ ] Add "View All" link from Dashboard



### 10.4 UI Mockup

No coding.

Just sketch:

- Dashboard navigation
- Renewals page
- Calendar
- Renewal History
- Renewal Button
- Reminder badge



## Phase 2 – Database & Core Renewal Logic

- [x] Add `last_renewal_date` to Subscription
- [x] Create RenewalHistory model
- [x] Create SQLAlchemy relationship
- [x] Verify relationship queries
- [x] Update existing database safely
- [x] Test database changes
- [x] Calculate Days Remaining
- [ ] Unit test Days Remaining



## Phase 3 – Renewals UI & Features

- [x] Create Renewals page
- [x] Group subscriptions by renewal status
- [x] Calculate Renewal Status
- [x] Overdue subscriptions
- [ ] Calendar page
- [ ] Monthly calendar view
- [x] Display renewal dates
- [ ] Highlight overdue renewals on Dashboard
- [ ] Highlight today's renewals on Dashboard



### Subscription Editing Lifecycle



#### Before First Renewal

- [x] Allow editing all subscription details
- [x] Allow changing Start Date
- [x] Allow changing Billing Frequency
- [x] Allow changing Amount
- [x] Validate Next Renewal Date



#### After First Renewal

- [ ] Preserve Original Start Date
- [ ] Lock Original Start Date
- [ ] Disable billing-related editing from Edit Subscription
- [ ] Allow only Status changes
- [ ] Allow Delete Subscription



### Testing

- [x] Test overdue subscriptions
- [x] Test future renewals
- [ ] Test leap years
- [x] Test monthly/yearly subscriptions
- [ ] Test duplicate renewal prevention
- [ ] Test renewal history creation


### Renewals Page UI Redesign

- [ ] Design page layout
- [ ] Create tab navigation
- [ ] Overdue tab
- [ ] Due Today tab
- [ ] Upcoming tab
- [ ] Display counts on each tab
- [ ] Default to Overdue tab
- [ ] Design compact renewal cards
- [ ] Style active tab
- [ ] Style Renew Subscription button
- [ ] Responsive design


## Phase 4 – Renewal Confirmation Workflow



### Renewal Confirmation Page

- [ ] Create Renewal Confirmation page
- [ ] Display Original Start Date
- [ ] Display Current Subscription Details
- [ ] Display Current Billing Frequency
- [ ] Display Current Amount
- [ ] Allow editing Subscription Name
- [ ] Allow editing Amount
- [ ] Allow editing Billing Frequency
- [ ] Allow editing Renewal Date
- [ ] Auto-calculate Next Renewal Date
- [ ] Show confirmation summary



### Renewal Validation

- [ ] Prevent renewal dates before the previous renewal
- [ ] Prevent future renewal dates beyond today (optional)
- [ ] Validate billing frequency changes
- [ ] Auto-recalculate next renewal after edits



### Dashboard / Renewals Page

- [x] Show "Renew Subscription" button only for Due Today or Overdue subscriptions



### Backend

- [ ] Load Renewal Confirmation
- [ ] Validate renewal information
- [ ] Save RenewalHistory
- [ ] Update Subscription
- [ ] Update Subscription Name (if changed)
- [ ] Update Billing Frequency (if changed)
- [ ] Update Amount (if changed)
- [ ] Update Last Renewal Date
- [ ] Update Next Renewal Date



### Business Rules

- [x] Renewal is available only for Due Today or Overdue subscriptions.
- [x] Renewals are created through the Renew action, not by editing the subscription.
- [ ] Prevent duplicate renewals
- [x] Before first renewal all fields are editable
- [x] After first renewal billing changes only occur during Renewal Confirmation
- [x] Original Start Date is immutable after first renewal
- [x] Renewal History must preserve previous billing events



### Phase 4 Outcome

- [ ] Complete end-to-end renewal workflow



## Phase 5 – Renewal History



### Backend

- [ ] Retrieve renewal history
- [ ] Sort history by most recent renewal
- [ ] Handle subscriptions with no renewal history



### UI

- [ ] History page
- [ ] Timeline/List view
- [ ] Search renewal history


## Phase 6 – Notifications

- [ ] In-app reminder badges
- [ ] In-app renewal notifications
- [ ] Notification badge on navigation



## Sprint 10 Fixes



### Business Logic

- [ ] Prevent duplicate renewals
- [ ] Protect future renewal dates from accidental updates
- [ ] Support billing cycle validation during Renewal Confirmation



## Git

- [x] Commit Sprint 10 Phase 1 & 2
- [ ] Push Sprint 10 to GitHub



## Sprint Outcome

Goal:

- Renewal management
- Renewal history
- Renewal status calculation
- Renewal calendar
- Reminder badges
- Automatic renewal workflow

Current Status:

🟡 Phase 3 – Renewals UI & Features (In Progress)

---



# Sprint 11 – User Authentication



## Authentication

- [ ] User Registration
- [ ] Login
- [ ] Logout
- [ ] Password Hashing



## User Features

- [ ] Personal Dashboard
- [ ] User-specific subscriptions

---



# Sprint 12 – Deployment & Portfolio



## Deployment

- [ ] Production Configuration
- [ ] Deploy to Render
- [ ] Deploy Database
- [ ] Environment Variables



## Documentation

- [ ] README.md
- [ ] Installation Guide
- [ ] Screenshots
- [ ] Demo Video



## Portfolio

- [ ] Update Resume
- [ ] Update GitHub
- [ ] Portfolio Website
- [ ] LinkedIn Project

---



# Product Backlog



## Renewal Management

- [x] Auto-calculate next renewal date



## Renewals

- [ ] Search Renewal History
- [ ] Filter Renewal History
- [ ] Export Renewal History



## Dashboard

- [ ] Expand category cards
- [x] Pie / doughnut charts
- [ ] Monthly spending trend



## Reports Page

- [ ] Export CSV
- [ ] Export PDF



## Notifications

- [ ] Renewal reminders
- [ ] Email reminders
- [ ] Desktop notifications
- [ ] Renewal Notifications



## MAintenance/Refactoring

- [ ] Refactor style.css
- [ ] Refactor dashboard.html
- [ ] Move repeated currency formatting into a reusable helper



## Future Enhancement

- Support multiple Billing Cycle Policies
  - [ ] Fixed Billing Cycle
  - [ ] Reset Billing Cycle on Renewal

---



# Development Infrastructure



## Environment

- [x] Create virtual environment
- [x] Create requirements.txt



## Database

- [ ] Configure Flask-Migrate
- [ ] Initialize Alembic migrations
- [ ] Create initial database migration
- [ ] Verify migration workflow



# Completed Features

- [x] Add Subscription
- [x] Edit Subscription
- [x] Delete Subscription
- [x] Dashboard Statistics
- [x] Estimated Monthly Cost
- [x] Active Subscription Count
- [x] Renewing Soon Counter
- [x] Search
- [x] Filter
- [x] Sort
- [x] Flash Notifications
- [x] Unsaved Changes Warning
- [x] Basic responsive UI
- [x] Bootstrap Icons
- [x] Status Badges
- [x] Dashboard Analytics
- [x] Yearly Spending Calculator
- [x] Spending by Category
- [x] Upcoming Renewals
- [x] Responsive Dashboard Controls
- [x] Empty State UI
- [x] Renewal Date Validation
- [x] Reports Page
- [x] Dashboard Charts
- [x] Reports & Dashboard Navigation

---



# Ideas for Future Versions

- Dark Mode
- Multiple Currencies
- Email Reminders
- Historical Spending Trends
- Payment History Analytics
- Mobile App
- AI Spending Insights
- Family Accounts
- Subscription Sharing
- Cloud Sync
- Scheduled subscription status

---



# Notes

Use this section to keep track of ideas, bugs, and future improvements while developing the project.