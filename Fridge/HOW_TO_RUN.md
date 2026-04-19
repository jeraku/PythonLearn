# ❄️ FridgeKeeper — Run as localhost website

## 1. Install dependencies
```bash
pip install flask openpyxl pandas
```

## 2. Put these files in the same folder:
```
your-folder/
├── app.py               ← Flask server
├── fridge_data.py       ← Excel data layer
├── fridge_groceries.xlsx← Your grocery data
└── templates/
    └── index.html       ← The web UI
```

## 3. Run the server
```bash
python app.py
```

## 4. Open in browser
```
http://localhost:5050
```

That's it! Every change you make in the browser auto-saves to Excel within 1 second.

## API endpoints (for reference)
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/items | Load all items |
| POST | /api/items | Save all items |
| DELETE | /api/items/:id | Delete one item |
| POST | /api/upload | Upload new .xlsx |
| GET | /api/download | Download current .xlsx |
| GET | /api/expiring?days=3 | Items expiring soon |
| POST | /api/create-sample | Reset with sample data |
