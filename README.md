# Oxford 3000 YouTube Comparison

This repository is dedicated to verifying the coverage of the YouTube subtitles wordlist (`3000 Oxford Words in 4 Hours` video) against the official Oxford 3000 vocabulary database.

## Table of Contents
- [Source Video Information](#source-video-information)
- [Repository Structure](#repository-structure)
- [Running the Analysis](#running-the-analysis)
- [Running the Unit Tests](#running-the-unit-tests)
- [Related Projects](#related-projects)

---

## Source Video Information
- **Title:** Learn 3000 Oxford Words in 1 Video (4 Hours) - Understand 95% of English – Real Conversations
- **URL:** [YouTube Video Link](https://www.youtube.com/watch?v=240MQzLUZRo)
- **Description:** This video promises to cover the entire Oxford 3000 wordlist using subtitles. This repository contains the raw subtitle transcripts in English (.en) and Russian (.ru) translation along with text transcripts.
- **Source Video Materials (Copied to Root):**
  - [Learn 3000 Oxford Words in 1 Video (4 Hours) - Understand 95% of English – Real Conversations - YouTube.url](./Learn%203000%20Oxford%20Words%20in%201%20Video%20(4%20Hours)%20-%20Understand%2095%25%20of%20English%20%E2%80%93%20Real%20Conversations%20-%20YouTube.url) (Shortcut to video)
  - English Subtitles (.srt): [20260713121030-learn-3000-oxford-words.en.srt](./20260713121030-learn-3000-oxford-words.en.srt)
  - English Transcript (.txt): [20260713121030-learn-3000-oxford-words.en.txt](./20260713121030-learn-3000-oxford-words.en.txt)
  - Russian Subtitles (.srt): [20260713121030-learn-3000-oxford-words.ru.srt](./20260713121030-learn-3000-oxford-words.ru.srt)
  - Russian Transcript (.txt): [20260713121030-learn-3000-oxford-words.ru.txt](./20260713121030-learn-3000-oxford-words.ru.txt)

- **Kardenwort Core Exports (from `20241223170748-kardenwort`):**
  - English sentence triplets JSON: [20260713162200-hi-rose-good-morning.triple.sentence.en.json](./20260713162200-hi-rose-good-morning.triple.sentence.en.json)
  - English sentence triplets TSV: [20260713162200-hi-rose-good-morning.triple.sentence.en.tsv](./20260713162200-hi-rose-good-morning.triple.sentence.en.tsv)
  - English word triplets TSV: [20260713162224-hi-rose-good-morning.triple.word.en.tsv](./20260713162224-hi-rose-good-morning.triple.word.en.tsv)

[Return to Top](#oxford-3000-youtube-comparison)

## Repository Structure
```text
U:\voothi\20260715201717-oxford-3000-youtube-comparison\
├── scripts/
│   └── compare_dicts.py                     # Normalized comparison and classification script
├── tests/
│   └── test_compare.py                      # Unit tests for comparison functions
├── 20260715200613-3000-oxford-words-in-4.tsv # YouTube subtitles wordlist to verify
├── 20260715160822-oxford-3000.en.tsv        # Oxford 3000 reference database with levels
├── 20260715165539-oxford-5000-expanded.en.tsv # Oxford 5000 expanded reference database
├── 20260713121030-learn-3000-oxford-words.* # Video subtitles and text files (en/ru)
├── 20260713162200-hi-rose-good-morning.*    # Kardenwort Core export files
├── 20260715202804-dictionary-comparison-results.md # Markdown findings report
├── 20260715202804-missing-words.tsv         # TSV dataset of missing words
├── 20260715202804-superfluous-words.tsv     # TSV dataset of superfluous words
├── Learn 3000 Oxford Words... - YouTube.url  # Link to YouTube video source
├── .gitattributes                           # Git attributes configuration
├── .gitignore                               # Git ignore configuration
├── LICENSE                                  # MIT License
└── README.md                                # This document
```

[Return to Top](#oxford-3000-youtube-comparison)

## Running the Analysis
To run the dictionary comparison script and update the results:
```powershell
python scripts/compare_dicts.py
```

The script will read the datasets, match them against spelling rules and CEFR level definitions from the local reference databases, and write a detailed analysis markdown report to [20260715202804-dictionary-comparison-results.md](./20260715202804-dictionary-comparison-results.md) along with detailed TSV lists of missing and superfluous words to [20260715202804-missing-words.tsv](./20260715202804-missing-words.tsv) and [20260715202804-superfluous-words.tsv](./20260715202804-superfluous-words.tsv).

[Return to Top](#oxford-3000-youtube-comparison)

## Running the Unit Tests
Execute the unit test suite from the terminal:
```powershell
python tests/test_compare.py
```

[Return to Top](#oxford-3000-youtube-comparison)

---

## Related Projects
- **Oxford Curation Project:** [Oxford 3000/5000 Wordlist Curation & Caching Pipeline](../20260715190122-oxford-3000-5000/README.md)
- **Kardenwort Core:** [Kardenwort Core Extraction Project](../20241223170748-kardenwort/README.md)

[Return to Top](#oxford-3000-youtube-comparison)
