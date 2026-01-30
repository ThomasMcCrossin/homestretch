# Comparison: 2023 Filed T2 vs FY2024/FY2025 Packet

**Filed Return Source:** `data/2023 - 14587430 Canada Inc..pdf`
**Packet Source:** `UfileToFill/ufile_packet/packet.json`
**Analysis Date:** 2026-01-27

---

## Executive Summary

The 2023 filed return was a **nil return** for the stub period (2022-12-08 to 2023-05-31) with $0 net income and no GIFI schedules. The FY2024 and FY2025 returns are the first active filing years with financial activity.

**Overall Consistency:** **GOOD** - No blocking inconsistencies identified.

---

## Extracted Data from 2023 Filed PDF

### Corporation Identification (Pages 1, 12, 20)

| Field | 2023 Filed Value | Page Reference |
|-------|------------------|----------------|
| Corporation Name | 14587430 Canada Inc. | Page 1, 12 |
| Business Number | 748003142RC0001 | Page 2, 12 |
| Tax Year Start | 2022-12-08 | Page 1, 12 |
| Tax Year End | 2023-05-31 | Page 1, 12 |
| Jurisdiction | Nova Scotia | Page 6 |
| Corp Type | CCPC (Box 1 ticked) | Page 12 |

### Address (Page 12)

| Field | 2023 Filed Value |
|-------|------------------|
| Location of books | 125 Victoria St E |
| City | Amherst |
| Province | NS |
| Postal Code | B4H1X9 |

### Key Elections/Answers (Pages 12-14)

| Question | 2023 Filed Answer | Page |
|----------|-------------------|------|
| IFRS used? | No (line 270) | Page 14 |
| Corporation inactive? | Yes (line 280) | Page 14 |
| First year after incorporation? | Yes (line 070) | Page 12 |
| Resident of Canada? | Yes (line 080) | Page 12 |
| Acquisition of control? | No (line 063) | Page 12 |
| Functional currency election? | No (line 079 blank) | Page 12 |
| Internet income? | No (line 180) | Page 13 |
| Schedule 1 differences? | No (line 201) | Page 13 |
| Shareholders >10%? | Yes (line 173) | Page 13 |

### Schedule 24 - First-time Filer (Page 23)

| Field | 2023 Filed Value |
|-------|------------------|
| Type of operation | 99 (Other) |
| Predecessor corporations | None |
| Wind-up subsidiaries | None |

### Schedule 50 - Shareholders (Page 24)

| Name | SIN | Common % | Preferred % |
|------|-----|----------|-------------|
| Thomas McCrossin | XXX-XXX-XXX | 25 | 25 |
| Dwayne Ripley | XXX-XXX-XXX | 75 | 75 |

### Financial Data (Pages 8, 14)

| Field | 2023 Filed Value |
|-------|------------------|
| Net income (Schedule 1 code A) | $0 |
| Taxable income (line 360) | $0 |
| Part I tax payable (line 700) | $0 |
| Business limit (line 410) | $239,726 |

### Contact Information (Pages 6, 20)

| Field | 2023 Filed Value |
|-------|------------------|
| Signing Officer | Dwayne Ripley |
| Position | President |
| Phone | (902) 669-2700 |
| Contact Person | Thomas McCrossin |
| Contact Phone | (902) 321-6749 |
| Email | tom@curlys.ca |

---

## Comparison Results

### MATCHES (Consistent between 2023 filed and packet)

| Item | 2023 Filed | Packet FY2024/FY2025 | Status |
|------|------------|---------------------|--------|
| Corporation Name | 14587430 Canada Inc. | 14587430 Canada Inc. | MATCH |
| Business Number | 748003142RC0001 | 748003142RC0001 | MATCH |
| Head Office Address | 125 Victoria St E, Amherst NS B4H1X9 | 125 Victoria St E, Amherst NS B4H1X9 | MATCH |
| Jurisdiction | NS (Nova Scotia) | NS | MATCH |
| Corp Type | CCPC | CCPC | MATCH |
| IFRS | No | No | MATCH |
| Functional Currency | CAD (no election) | CAD (no election) | MATCH |
| Signing Officer | Dwayne Ripley, President | Dwayne Ripley, President | MATCH |
| Signing Officer Phone | (902) 669-2700 | (902) 669-2700 | MATCH |
| Contact Person | Thomas McCrossin | Thomas McCrossin | MATCH |
| Contact Phone | (902) 321-6749 | (902) 321-6749 | MATCH |
| Email | tom@curlys.ca | tom@curlys.ca | MATCH |
| Shareholder: Dwayne Ripley | 75% common, 75% preferred | 75% common, 75% preferred | MATCH |
| Shareholder: Thomas McCrossin | 25% common, 25% preferred | 25% common, 25% preferred | MATCH |
| Dwayne SIN | XXX-XXX-XXX | XXX-XXX-XXX | MATCH |
| Thomas SIN | XXX-XXX-XXX | XXX-XXX-XXX | MATCH |

### DIFFERENCES (Expected changes between years)

| Item | 2023 Filed | Packet FY2024/FY2025 | Notes |
|------|------------|---------------------|-------|
| Tax Year Period | 2022-12-08 to 2023-05-31 (stub) | 2023-06-01 to 2024-05-31 / 2024-06-01 to 2025-05-31 | Expected: different periods |
| Corporation Inactive? | Yes | No | Expected: corp became active |
| First year after incorporation? (T2 line 070) | Yes | No (FY2024/FY2025) | 2023 stub already filed as first-time filer (Schedule 24) |
| Internet income (line 180)? | No | Yes (implied by Shopify sales) | New activity |
| Schedule 1 differences (line 201)? | No | Yes (meals add-back, penalties) | Active year has adjustments |
| Net income (Schedule 1 code A) | $0 | $16,655 (FY2024), $28,349 (FY2025) | Expected: active operations |
| Taxable income (line 360) | $0 | $16,985 (FY2024), $28,827 (FY2025) | Expected: active operations |
| Schedule 100/125 attached? | No | Yes | Expected: active year requires GIFI |
| Business limit (line 410) | $239,726 (prorated 175 days) | $500,000 (full year) | Expected: full year limit |

### UNKNOWN / COULD NOT EXTRACT

| Item | Notes |
|------|-------|
| NAICS Code | Not printed in the PDF text extraction, but UFile prefill files show NAICS = 722512 (Limited-Service Eating Places) for both 2023 and 2024 entry |
| Mailing Address | PDF text extraction doesn’t reliably include the mailing/books address blocks; see UFile prefill exports for the exact addressee fields |
| Principal Products | 2023 PDF lines 284-289 appear blank; packet doesn't specify % breakdown |

---

## Additional diffs found in UFile prefill exports (not reliably visible in PDF text)

These aren’t necessarily “wrong”, but they are exactly the kind of subtle carryforward differences that can cause inconsistency if UFile pulls forward different defaults year-to-year.

- **Location of books and records – “Name of addressee”**
  - 2023 prefill: **Curly’s** (`output/UfileToFill/Other Addresses/2023.txt`)
  - 2024 prefill: **Dwayne Ripley** (`output/UfileToFill/Other Addresses/CurrentlyIn2024/otheraddresses2024.txt`)
  - Recommendation: keep FY2024/FY2025 aligned to the **already-filed 2023 return** unless you intentionally changed it. The packet keeps:
    - Mailing addressee = **Dwayne Ripley**
    - Books & records addressee = **Curly’s**

- **“Has the mailing/books address changed since last time a T2 return was filed?”**
  - 2023 prefill shows **No Change** in both sections.
  - 2024 prefill shows a blank placeholder (`---`) in at least one section.
  - Recommendation: for FY2024/FY2025, answer consistently based on whether you actually changed these addresses since last filed return.

## Consistency Flags

### NO FLAGS - Safe to Proceed

1. **Corporation identity**: BN, name, address all match exactly
2. **Shareholder structure**: Same shareholders with same percentages and SINs
3. **Corp type**: CCPC throughout - consistent
4. **IFRS**: Consistently "No"
5. **Contact information**: All contacts match

### INFORMATIONAL NOTES

1. **Year-end consistency**: 2023 stub ended 2023-05-31; FY2024 starts 2023-06-01 - continuous
2. **First year flag**: FY2024/FY2025 should answer **"No"** to T2 line 070 because the filed 2023 stub return already answered "Yes" and filed Schedule 24
3. **Business limit**: Full $500,000 for FY2024/FY2025 (vs. prorated in 2023 stub)
4. **Schedule 50**: Same shareholder data - can be copied forward

---

## Recommendations

1. **T2 line 070 / Schedule 24**: For FY2024/FY2025, answer **No** (Schedule 24 already filed with the 2023 stub return).

2. **NAICS Code**: Keep **722512** (Limited-Service Eating Places) consistent with the filed 2023 return / UFile prefill exports.

3. **Internet Income (line 180)**: Answer "Yes" for FY2024/FY2025 due to Shopify sales activity.

4. **Schedule 1 (line 201)**: Answer "Yes" due to meals/entertainment add-back and penalty add-back.

5. **Schedule 88**: May be required if answering "Yes" to line 180 (Internet income).

---

## PDF Extraction Quality

| Page Range | Extraction Quality | Notes |
|------------|-------------------|-------|
| 1-5 (Diagnostics) | Good | Text extracted cleanly |
| 6 (Executive Summary) | Good | All fields visible |
| 7 (Assembly Instructions) | Good | |
| 8-9 (Schedule 200 Summary) | Good | Financial figures visible |
| 10-11 (Carryforward Schedule) | Good | All blank as expected |
| 12-14 (T2 Form) | Good | All checkboxes and values visible |
| 15-19 (T2 Calculations) | Good | Business limit visible |
| 20 (Summary/Certification) | Good | Contact info visible |
| 21-22 (Bar Code Return) | Good | |
| 23 (Schedule 24) | Good | Type 99 selected |
| 24 (Schedule 50) | Good | Both shareholders visible |
| 25-26 (T183 CORP) | Good | Authorization details visible |

**Overall PDF Extraction**: HIGH QUALITY - No OCR required; text-based PDF with clean extraction.

---

*This comparison was generated by analyzing the 2023 filed PDF against packet.json. All page references are to the 26-page PDF file.*
