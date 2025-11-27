import pathlib
import shutil

DOCS = pathlib.Path("docs")

def update_latest(prefix: str):
    # π.χ. prefix = "CV_EN_"
    candidates = sorted(DOCS.glob(f"{prefix}*.pdf"))
    if not candidates:
        print(f"No files found for prefix {prefix}")
        return
    latest = candidates[-1]  # παίρνουμε το "μεγαλύτερο" όνομα, π.χ. πιο πρόσφατη ημερομηνία
    target = DOCS / f"{prefix.split('_')[1]}_latest.pdf"  # CV_EN_ -> EN_latest.pdf (θα το φτιάξουμε λίγο αλλιώς)

def main():
    # Πιο καθαρά: απλά ορίζουμε explicit targets
    mapping = {
        "CV_EN": "CV_EN_latest.pdf",
        "CV_NL": "CV_NL_latest.pdf",
        "CV_DE": "CV_DE_latest.pdf",
    }

    for base, alias in mapping.items():
        candidates = sorted(DOCS.glob(f"{base}_*.pdf"))
        if not candidates:
            print(f"[WARN] No files found for {base}_*.pdf")
            continue
        latest = candidates[-1]
        target = DOCS / alias
        print(f"[INFO] Setting {alias} -> {latest.name}")
        shutil.copy2(latest, target)

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    main()
