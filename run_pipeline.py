"""
Bluestock Mutual Fund Analytics - Master Pipeline

This script runs the major project stages in sequence. It is designed to work
from the project root folder and skips missing scripts gracefully so that the
final repository remains easy to execute on another machine.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

SCRIPTS = [
    "bluestock_day1_to_day5_final_project/data_ingestion.py",
    "bluestock_day1_to_day5_final_project/live_nav_fetch.py",
    "bluestock_day1_to_day5_final_project/fund_master_analysis.py",
    "bluestock_day1_to_day5_final_project/amfi_validation.py",
    "bluestock_day1_to_day5_final_project/data_cleaning_and_sqlite_loader.py",
    "bluestock_day1_to_day5_final_project/eda_analysis.py",
    "bluestock_day1_to_day5_final_project/performance_analytics.py",
    "scripts/recommender.py",
]


def run_script(relative_path: str) -> None:
    """Run a Python script if it exists, otherwise print a skip message."""
    script_path = ROOT / relative_path
    if not script_path.exists():
        print(f"SKIP: {relative_path} not found")
        return

    print(f"RUNNING: {relative_path}")
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(script_path.parent),
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Pipeline failed at: {relative_path}")


def main() -> None:
    """Execute all available project scripts in order."""
    for script in SCRIPTS:
        run_script(script)
    print("Pipeline execution completed successfully.")


if __name__ == "__main__":
    main()
