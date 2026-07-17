# Smart Subscription Manager

## Project Roadmap

---

# Project Progress


| Sprint                                | Status         |
| ------------------------------------- | -------------- |
| Sprint 1 – Project Setup              | ✅ Complete     |
| Sprint 2 – Dashboard UI               | ✅ Complete     |
| Sprint 3 – Database Integration       | ✅ Complete     |
| Sprint 4 – Add Subscription           | ✅ Complete     |
| Sprint 5 – Edit & Delete Subscription | ✅ Complete     |
| Sprint 6 – Dashboard Statistics       | ✅ Complete     |
| Sprint 7 – UI / UX Improvements       | ✅ Complete     |
| Sprint 8 – Dashboard Analytics        | ✅ Complete     |
| Sprint 9 – Charts & Reports           | 🟡 In Progress |
| Sprint 10 – Calendar & Reminders      | ⬜ Not Started  |
| Sprint 11 – User Authentication       | ⬜ Not Started  |
| Sprint 12 – Deployment & Portfolio    | ⬜ Not Started  |


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
- [ ] Add empty states for charts
- [x] Make charts responsive
- [ ] Assign fixed colors for categories *(new)*
  > Since we've decided on the fixed color mapping, I'd keep it here until it's implemented.

---



## Reports

- [ ] Create Reports page
- [ ] Monthly Spending Summary
- [ ] Yearly Spending Summary
- [ ] Subscription Status Summary
- [ ] Upcoming Renewal Summary
- [ ] Add navigation between Dashboard and Reports
- [ ] Export PDF — optional stretch goal

---



## Testing

- [ ] Test charts with multiple subscriptions
- [ ] Test charts with one subscription
- [ ] Test charts with no subscriptions
- [ ] Test different billing frequencies
- [ ] Test active, paused, and cancelled subscriptions
- [ ] Test responsive chart layout
- [ ] Test Reports page on desktop
- [ ] Test Reports page on mobile

---



## UI Polish

- [x] Use consistent chart card styling
- [x] Add chart titles and descriptions
- [ ] Add clear empty-state messages
- [x] Ensure chart labels are readable
- [x] Improve currency formatting (฿) *(new)*
- [ ] Ensure report sections have consistent spacing

---



## Technical Debt

- [ ] Refactor style.css
- [ ] Refactor dashboard.html
- [ ] Remove duplicate CSS
- [ ] Organize JavaScript
- [ ] Add comments where necessary

---



## Git

- [ ] Commit Sprint 9
- [ ] Push Sprint 9 to GitHub

---



## Bug Fix List

- [ ] Edit form should preserve user-entered values after validation failure.
- [ ] Refactor monthly cost calculation to avoid duplicate logic *(new)*

---



# Sprint 10 – Calendar & Reminders



## Features

- [ ] Renewal Calendar
- [ ] Upcoming Renewals
- [ ] Renewal Notifications
- [ ] Days Remaining

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

- [ ] Mark subscription as renewed
- [ ] Store last renewal date
- [x] Auto-calculate next renewal date
- [ ] Show overdue subscriptions
- [ ] Renewal history



## Dashboard

- [ ] Expand category cards
- [x] Pie / doughnut charts
- [ ] Monthly spending trend



## Notifications

- [ ] Renewal reminders
- [ ] Email reminders
- [ ] Desktop notifications

---



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

---



# Ideas for Future Versions

- Dark Mode
- Multiple Currencies
- Email Reminders
- Historical Spending Trends
- Payment History Analytics
- Export CSV
- Export PDF
- Mobile App
- AI Spending Insights
- Family Accounts
- Subscription Sharing
- Cloud Sync
- Scheduled subscription status

---



# Notes

Use this section to keep track of ideas, bugs, and future improvements while developing the project.