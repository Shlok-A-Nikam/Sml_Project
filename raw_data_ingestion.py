import os
import shutil
from pathlib import Path

from src.components.data_injestion import DataIngestion


def main():
	# Ensure source dataset exists
	src = Path('artifact') / 'StudentsPerformance.csv'
	dest_dir = Path('notebook') / 'data'
	dest = dest_dir / 'stud.csv'
	dest_dir.mkdir(parents=True, exist_ok=True)
	if not src.exists():
		raise FileNotFoundError(f"Source dataset not found: {src}")
	shutil.copy(src, dest)
	print(f"Copied dataset to {dest}")

	ingestion = DataIngestion()
	train_path, test_path = ingestion.initiate_data_ingestion()
	print('Train file:', train_path)
	print('Test file:', test_path)


if __name__ == '__main__':
	main()

