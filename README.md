# Guide – Layer-Based Privacy & Security Hardening Tool

Guide is an **offline-first, layer-based privacy and security hardening tool** for Windows and Linux.  
It is designed to help users prepare **clean, controlled environments** for privacy-sensitive work and cybersecurity testing — without relying on internet connectivity or external services.

Guide does **not collect data**, does **not communicate externally**, and performs only **user-approved, reversible system changes**.

---

## 🎯 Project Goals

- Improve user privacy through **clear, layered controls**
- Provide **offline-safe environments** for cybersecurity testing
- Disable invasive OS features (e.g. telemetry, recall, background tracking)
- Reduce accidental data leakage caused by user behavior
- Make privacy actions **transparent, reversible, and auditable**

---

## 🧱 Layer-Based Architecture

Guide operates using independent, selectable layers.  
Each layer targets a specific attack or leak surface.


Users may enable layers individually or combine them.

---

## 🪟 Windows Features

When enabled, Guide can:

- Disable Windows telemetry and background diagnostics
- Disable Windows Recall and related background components
- Disable activity history and clipboard history
- Reduce background services that generate user traces
- Apply changes in a **reversible** and **non-destructive** way

> No files are deleted. All changes can be restored.

---

## 🐧 Linux Features

On supported Linux systems, Guide can:

- Limit or disable shell history
- Restrict system logging verbosity
- Disable unnecessary background services
- Reduce metadata generation during testing
- Prepare clean environments for offline analysis

---

## 🌐 Network Layer (Offline-First)

Guide can fully operate **without internet access**.

Optional network actions include:

- Disabling network interfaces
- Flushing DNS and ARP caches
- Disabling IPv6
- Randomizing MAC address (offline only)
- Restoring all settings after use

This allows users to safely perform **offline analysis** without ISP or network exposure.

---

## 🧪 Scenario-Based Profiles

Guide includes predefined **behavior profiles** designed for common cybersecurity and privacy use cases.

Examples:

### Offline File Analysis
- Network disabled
- USB auto-mount disabled
- Clipboard cleared
- Logging limited

### CTF / Training Environment
- Local network only
- Screen capture disabled
- Minimal system noise

### Forensics / Analysis Mode
- Disk writes minimized
- Time synchronization disabled
- Logs set to read-only where possible

Profiles are **transparent** and customizable.

---

## 🔐 Privacy & Ethics

Guide is designed for **defensive, educational, and privacy-preserving use**.

It does **not**:
- Hide malicious activity
- Bypass security controls
- Install persistence mechanisms
- Communicate with external servers
- Perform actions without user consent

All actions are local, visible, and reversible.

---

## 🔄 Restore & Safety

At any time, users can restore the system to its previous state:

