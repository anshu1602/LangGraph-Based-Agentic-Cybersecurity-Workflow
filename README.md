# Agentic Cybersecurity Pipeline

## Overview
An autonomous cybersecurity pipeline built with **LangGraph** and **LangChain** to simplify penetration testing. It breaks down tasks (e.g., "Scan google.com for ports"), enforces scope constraints, runs tools like `nmap`, and generates reports. Ideal for security audits with dynamic task management and failure handling.

## Features
- Converts instructions into executable tasks.
- Restricts scans to defined domains/IPs (e.g., `google.com`, `142.250.0.0/16`).
- Executes `nmap` and processes outputs.
- Retries failed tasks and logs errors.
- Outputs a JSON report with results.

## Tech Stack
- Python 3.11
- LangGraph & LangChain
- Pydantic
- Subprocess

## Structure
