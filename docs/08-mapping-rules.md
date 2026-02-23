# Mapping Rules (Touchpoints)

## Purpose
Map release items to configuration touchpoints using keywords and hints, then score impact.

## Mapping source
`mappings/touchpoints.yml`

## Touchpoint schema
```yml
version: 1
touchpoints:
  - id: <string>
    keywords: [<string>, ...]
    categoryHints: [<string>, ...]
    criticality: <1-5>
```

# MVP Ingestion Sources (Pick One)

## Option A (Fast): Manual Entry Queue

Maintain a simple list of release items in a:

- JSON file  
  **or**
- SharePoint list  

Each item must include:

- `title`
- `type`
- `description`
- `module`
- `url`

The Power Automate flow:

1. Reads the list.
2. Normalizes each record.
3. Outputs the standardized release artifact.

---

## Option B (Preferred): Pull from Maintained RSS / HTML Page

1. Use **HTTP GET** to fetch release content page(s).
2. Split content into structured sections.
3. For each section:
   - Create a release item record.
4. Output the normalized release artifact.

---

# Required Normalization Rules

- `id`  
  Must be stable within a release.  
  Format:      