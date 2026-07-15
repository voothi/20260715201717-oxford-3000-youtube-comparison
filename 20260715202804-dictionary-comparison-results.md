# Dictionary Comparison Report

This report compares the original **Oxford 3000** wordlist and the **YouTube Subtitles 3000 Words in 4** list.

## Executive Summary
- **Oxford 3000 File:** `20260715200533-oxford-3000.tsv`
- **YouTube Subtitles File:** `20260715200613-3000-oxford-words-in-4.tsv`
- **Coverage Verdict:** **The second file does NOT cover the first file.**
  - **Direct Word Match Coverage:** 76.46% (2277 / 2978 words)
  - **Missing Words from Oxford 3000:** 701 words (detailed in [20260715202804-missing-words.tsv](./20260715202804-missing-words.tsv))
  - **Superfluous Words in YouTube List:** 679 words (detailed in [20260715202804-superfluous-words.tsv](./20260715202804-superfluous-words.tsv))

> [!IMPORTANT]
> **Key Finding:** The YouTube subtitles list is missing major basic vocabulary words from the Oxford 3000 (such as `able`, `absolute`, `accuse`, `agenda`, etc.) and instead contains advanced, higher-level vocabulary words from the Oxford 5000 Expanded list (such as `academy`, `accessible`, `accessory`, `accord`, `accountant`, etc.). This indicates that the YouTube list was likely generated from a different version of the dictionary, or was mixed with Oxford 5000 words while dropping basic Oxford 3000 words.

## File Statistics
| Attribute | Oxford 3000 (File 1) | YouTube Wordlist (File 2) |
| --- | --- | --- |
| **Total Lines** | 3001 | 2999 |
| **Unique Words (Parsed)** | 2978 | 2956 |
| **Multi-word entries (e.g., 'a, an')** | 38 lines | 0 lines (words are strictly split) |

## 1. Missing Words Analysis
A total of **701** words from the Oxford 3000 are completely missing from the YouTube subtitles list. Here is the breakdown by CEFR Level:

| CEFR Level | Count | Sample Missing Words |
| --- | --- | --- |
| **** | 1 | `double`... |
| **A1** | 92 | `beer`, `bird`, `blonde`, `boot`, `born`, `boyfriend`, `bye`, `cannot`... |
| **A1, A2** | 5 | `best`, `dear`, `downstairs`, `upstairs`, `welcome`... |
| **A1, A2, B1** | 1 | `better`... |
| **A1, B1** | 2 | `age`, `centre`... |
| **A2** | 122 | `able`, `according to`, `ah`, `all right`, `any more`, `anyway`, `army`, `attack`... |
| **A2, B1** | 7 | `knock`, `musical`, `normal`, `original`, `pull`, `request`, `sort`... |
| **A2, B1, B2** | 3 | `following`, `worse`, `worst`... |
| **A2, B2** | 7 | `bar`, `extreme`, `feed`, `hold`, `ideal`, `round`, `survey`... |
| **B1** | 197 | `aged`, `agent`, `amazed`, `analyse`, `apart`, `approximately`, `arrival`, `backwards`... |
| **B1, B2** | 13 | `battle`, `chain`, `equal`, `favour`, `fold`, `hunt`, `latest`, `plot`... |
| **B2** | 251 | `absolute`, `accuse`, `affair`, `afterwards`, `agenda`, `alter`, `apparent`, `apparently`... |

### Spelling / Formatting Equivalents
Out of the missing words, **82** matches are minor spelling or formatting differences (e.g., American vs. British spelling or combined words):

| Oxford 3000 Word | YouTube Word | Explanation |
| --- | --- | --- |
| `ah` | `ai` | Minor character variation/typo |
| `analyse` | `analyze` | Minor character variation/typo |
| `any more` | `anymore` | Compound word spacing |
| `arms` | `atms` | Minor character variation/typo |
| `bar` | `ar` | Minor character variation/typo |
| `based` | `baked` | Minor character variation/typo |
| `behaviour` | `behavior` | British vs. American spelling (-our vs -or) |
| `bell` | `yell` | Minor character variation/typo |
| `bet` | `bat` | Minor character variation/typo |
| `blood` | `bloom` | Minor character variation/typo |
| `born` | `corn` | Minor character variation/typo |
| `bury` | `jury` | Minor character variation/typo |
| `cap` | `nap` | Minor character variation/typo |
| `cat` | `bat` | Minor character variation/typo |
| `cd` | `co` | Minor character variation/typo |
| `cell` | `yell` | Minor character variation/typo |
| `closed` | `closet` | Minor character variation/typo |
| `clothes` | `clothe` | Minor character variation/typo |
| `clue` | `cue` | Minor character variation/typo |
| `colour` | `color` | British vs. American spelling (-our vs -or) |
| ... and 62 more | | |

## 2. Superfluous Words Analysis
The YouTube list contains **679** words that are NOT in the Oxford 3000. Here is their classification:

| Classification | Count | Sample Words |
| --- | --- | --- |
| **External Word (Not in Oxford 3000/5000)** | 389 | `accessory`, `accord`, `ache`, `adapter`, `admirable`, `agreed`, `airplane`, `aisle`... |
| **Oxford 5000 Expanded (B2)** | 136 | `accountant`, `accuracy`, `additionally`, `ambulance`, `anxiety`, `applicant`, `assumption`, `automatically`... |
| **Oxford 5000 Expanded (B2, C1)** | 5 | `alien`, `dynamic`, `exit`, `principal`, `terminal`... |
| **Oxford 5000 Expanded (C1)** | 80 | `academy`, `accessible`, `adaptation`, `administrative`, `alert`, `anchor`, `appreciation`, `backup`... |
| **Spelling/Format Variant** | 69 | `aex`, `ai`, `analyze`, `anymore`, `ar`, `atms`, `baked`, `bat`... |

## Conclusion
The YouTube subtitles list `20260715200613-3000-oxford-words-in-4.tsv` **does not cover** the original Oxford 3000 list. Instead, it has a significant mismatch of approximately **23%**, representing a mix of:
1. **Omission of standard basic vocabulary** (A1-B2 levels, 700+ words missing).
2. **Inclusion of advanced C1 level vocabulary** from the Oxford 5000 (such as `academy`, `accessible`, `accessory`, etc.).
3. **Spelling differences** (e.g. `analyse` vs `analyze`, `any more` vs `anymore`).

If you want a wordlist that fully covers the Oxford 3000, you should use the clean, curated `20260715160822-oxford-3000.en.tsv` from the project repository rather than the YouTube subtitles extraction.
