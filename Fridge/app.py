"""
FridgeKeeper - Flask Web Server
Run:  python3 app.py
Open: http://localhost:5050
"""

from flask import Flask, jsonify, request, render_template, send_file
import fridge_data as db
import json, os, io

app = Flask(__name__)

# ── Pages ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# ── API ────────────────────────────────────────────────────────────────────

@app.route("/api/items", methods=["GET"])
def get_items():
    """Load all items from Excel and return as JSON."""
    try:
        items = db.load_data()
        return jsonify({"status": "ok", "items": items, "categories": db.CATEGORIES})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/items", methods=["POST"])
def save_items():
    """Receive full item list and save to Excel."""
    try:
        data = request.get_json()
        items = data.get("items", [])
        db.save_data(items)
        return jsonify({"status": "ok", "saved": len(items)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete a single item by ID and save."""
    try:
        items = db.load_data()
        items = [i for i in items if i.get("ID") != item_id]
        db.save_data(items)
        return jsonify({"status": "ok", "remaining": len(items)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/expiring")
def get_expiring():
    """Return items expiring within N days (default 3)."""
    days = int(request.args.get("days", 3))
    try:
        items = db.load_data()
        expiring = db.get_expiring_soon(items, days)
        return jsonify({"status": "ok", "expiring": expiring})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/upload", methods=["POST"])
def upload_excel():
    """Accept an uploaded .xlsx file, save it as the data file, reload."""
    try:
        f = request.files.get("file")
        if not f or not f.filename.endswith((".xlsx", ".xls")):
            return jsonify({"status": "error", "message": "Please upload a .xlsx file"}), 400
        f.save(db.EXCEL_FILE)
        items = db.load_data()
        return jsonify({"status": "ok", "items": items, "categories": db.CATEGORIES,
                        "message": f"Loaded {len(items)} items from {f.filename}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/download")
def download_excel():
    """Send the current Excel file as a download."""
    try:
        if not os.path.exists(db.EXCEL_FILE):
            db.create_excel()
            # Create sample Excel if none exists
        return send_file(db.EXCEL_FILE, as_attachment=True,
                         download_name="fridge_groceries.xlsx",
                         mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/create-sample", methods=["POST"])
def create_sample():
    """Create a fresh Excel with sample data."""
    try:
        db.create_excel()
        items = db.load_data()
        return jsonify({"status": "ok", "items": items, "categories": db.CATEGORIES})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ── Run ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    PORT = 5050
    print(f"""
  ❄️  FridgeKeeper is running!
  ➜  Open in browser: http://localhost:{PORT}
  ➜  Press Ctrl+C to stop
    """)
    
    # Create sample Excel if none exists
    if not os.path.exists(db.EXCEL_FILE):
        db.create_excel()
        print(f"  ✅  Created sample Excel: {db.EXCEL_FILE}\n")

    app.run(host="0.0.0.0", port=PORT, debug=True)
