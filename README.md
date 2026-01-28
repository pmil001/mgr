# mgr

genomic-ingestion-vcf/ 
├──.python-version # Wersja Pythona (3.11) dla narzędzia uv 
├── pyproject.toml # Zależności i konfiguracja projektu 
├── README.md # Dokumentacja techniczna 
├── docker-compose.yml # Orkiestracja klastra Cassandra i Spark 
├──.gitignore # Wykluczenia (.venv, /data, /logs) 
│ ├── config/ # Konfiguracja środowiska 
│ ├── spark_conf.yaml # Parametry sesji Spark i Glow 
│ └── cassandra_schema.cql # Definicje Keyspace i Tabel 
│ ├── data/ # Lokalny magazyn (dane testowe) 
│ ├── raw/ # Surowe pliki VCF (np. chromosom 22) 
│ └── ontology/ # Plik go-basic.obo 
│ ├── notebooks/ # Eksploracja danych (EDA) 
│ └── 01_data_exploration.ipynb 
│ ├── src/ # Kod źródłowy (ETL) 
│ ├── init.py 
│ ├── main.py # Punkt wejścia (spark-submit) 
│ ├── ingestion/ # Moduł "Extract" (VCF + Glow) - Bronze 
│ │ ├── init.py 
│ │ └── vcf_loader.py 
│ ├── enrichment/ # Moduł "Transform" (Gene Ontology) - Silver 
│ │ ├── init.py 
│ │ └── go_mapper.py 
│ └── storage/ # Moduł "Load" (Cassandra + Tuning) - Gold 
│ ├── init.py 
│ └── cassandra_writer.py 
│ ├── tests/ # Testy jednostkowe 
│ └── test_ingestion.py 
└── logs/ # Logi wydajnościowe (Baseline)


