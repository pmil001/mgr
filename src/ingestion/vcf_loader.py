from pyspark.sql import SparkSession
import os
import sys
from pathlib import Path

venv_python = sys.executable
os.environ['PYSPARK_PYTHON'] = venv_python
os.environ['PYSPARK_DRIVER_PYTHON'] = venv_python

# Upewnij się, że COMSPEC wskazuje na cmd.exe
if 'COMSPEC' not in os.environ:
    os.environ['COMSPEC'] = r'C:\Windows\System32\cmd.exe'

path = os.environ.get('VCF_PATH')

import glow

if not path:
    # Opcjonalnie: możesz tu ustawić ścieżkę domyślną lub przerwać działanie
    raise ValueError("BŁĄD: Zmienna środowiskowa VCF_PATH nie jest ustawiona w PowerShell!")

# Konwersja na format ścieżki odpowiedni dla Twojego OS (np. Windows)
vcf_path = Path(path).as_posix() # Spark preferuje forward slashes /

print(f"--- Próba wczytania pliku z: {vcf_path} ---")


spark = (SparkSession.builder
    .appName("GlowVCF")
    .config("spark.jars.packages", "io.projectglow:glow-spark3_2.12:1.2.1")
    .getOrCreate())

spark = glow.register(spark)
df =(spark.read
    .format('vcf')
    .option("includeSampleIds", True)
    .option("flattenInfoFields", True)
    .load(vcf_path))

df.printSchema()

df.select("contigName", "start", "end", "referenceAllele", "alternateAlleles").show(5)
