# Dummy PO Translations

This tool generates dummy translations from a PO file.

# Requirements

- Docker

# Install

- $ `git clone git@github.com:OnTheGoSystems/dummy-po-translation.git`
- $ `cd dummy-po-translation`
- $ `docker build --network=host -t dummy-po-translation .`

# Usage

- Use the example PO file [translations.po](translations.po) or replace it with your own PO file
- $ `docker run --rm -v $(pwd):/app dummy-po-translation /app/translations.po`
- The [translations-generated.po](translations-generated.po) and [translations-generated.mo](translations-generated.mo) files will be generated

# Options

- `-f`, `--factor`: The expansion factor for the dummy translation (default: `1.5`)