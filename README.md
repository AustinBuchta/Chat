# Interactive CLI Pizza Ordering System v2

An enhanced command-line ordering platform built in Python. Collects customer order parameters, validates inputs against structural constraints, looks up dynamic flavor pricing using dictionary mappings, and runs a real-time terminal ETA countdown timer.

## Technical Highlights

* **Dictionary-Based Price Mapping:** Implements key-value data structures (`menu` dictionary) and dynamic lookup methods (`.get()`) to map specialized pizza flavors directly to individual add-on costs.
* **Input Validation & Exception Guard Rails:** Enforces runtime input sanitization across user prompts using nested `while True` state loops, string length checks, and explicit type casting wrapped in `try/except` blocks.
* **Real-Time Terminal Timer:** Simulates live order status updates and countdown delivery ETAs using nested loops paired with standard library string carriage returns (`end="\r"`) and system sleeps (`time.sleep(1)`).
* **Order Replay Loop:** Encapsulates the core purchasing workflow inside a master control loop (`keepgoing`), enabling multiple sequential order submissions within a single active terminal session.

## Key Dependencies

* **Python Version:** Built using pure standard Python 3.x (uses built-in `time` module—zero external `pip` packages required).

## Usage

```bash
python main.py
