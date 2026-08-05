# MT Dashboard

Web-based Management Team Dashboard showing useful business insights from stored datasets. Built with Vue.js and Vuetify, it provides a unified interface for monitoring and managing operations across multiple departments of SP Brewery in Lae.

## Features

- **Multi‑Module Navigation** – Switch between Safety, Packaging, Brewing, Quality, Logistics, and Utilities sections via a persistent navigation drawer.
- **Data Import / Export** – Built‑in dialogs to import and export datasets for each module.
- **Real‑Time Notifications** – Toggleable notification panel to view system alerts.
- **Loading Spinner** – Visual feedback while API data is loading.
- **Snackbar Alerts** – Contextual messages with a dismiss button.
- **Responsive App Bar** – Quick access to notifications, user account, and back navigation.
- **Vuex State Management** – Centralised store for HTTP requests, alerts, and global loading state.
- **Dynamic API Integration** – Fetches API schemas and endpoints on initialisation.

## Tech Stack

- **Vue 2** with Vue Router
- **Vuetify** (Material Design component framework)
- **Vuex** for state management
- **Axios** (assumed for HTTP requests in store actions)
- **Vue CLI** for project scaffolding and build

## Prerequisites

- [Node.js](https://nodejs.org/) (v14 or later)
- npm or yarn

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mt_dashboard
