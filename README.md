# i-love-pdf

```bash

uv sync
deactivate

```

## Split

```bash
uv run i-love-pdf split doc.pdf

```

split par x pages

```bash
uv run i-love-pdf split doc.pdf -p x

```

dossier sortie

```bash
uv run i-love-pdf split doc.pdf -p x -o mon_output

```

## Merge

```bash
uv run i-love-pdf merge doc1.pdf doc2.pdf -o merged.pdf
```
