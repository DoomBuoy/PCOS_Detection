from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd
from pcos_detection.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    #  ...existing code...

    file_path_with_infertility = "https://drive.google.com/uc?id=1hb-vYxJOjVlYu747eD5TEmzLDSnZ9PYl"
    file_path_without_infertility = "https://docs.google.com/spreadsheets/d/1_tuPLLCvzccMdTRyiIOusbosPpThCqWl/export?format=xlsx"

    # Download and load CSV (with infertility)
    PCOS_inf = pd.read_csv(file_path_with_infertility)

    # Download and load XLSX (without infertility), using the correct sheet
    PCOS_woinf = pd.read_excel(file_path_without_infertility, sheet_name="Full_new")

    # Save each dataset separately to ../data/raw/
    raw_data_dir = Path(__file__).parent.parent / "data" / "raw"
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    inf_path = raw_data_dir / "PCOS_with_infertility.csv"
    woinf_path = raw_data_dir / "PCOS_without_infertility.csv"

    PCOS_inf.to_csv(inf_path, index=False)
    PCOS_woinf.to_csv(woinf_path, index=False)

    logger.success(f"PCOS with infertility saved to {inf_path}")
    logger.success(f"PCOS without infertility saved to {woinf_path}")
# ...existing code...
if __name__ == "__main__":
    app()
