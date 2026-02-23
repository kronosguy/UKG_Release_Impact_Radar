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

## Mapping algorithm (MVP)
1. Lowercase the release item `title` + `description`
2. For each touchpoint:
   - If any `keywords[]` appear, add that touchpoint
3. If none match, set `touchpoints=[]` and route the item to Needs Review

## Impact scoring inputs (MVP)
- `criticality` (from touchpoint)
- `exposure` (0/1): does the tenant have configs in that category?
- `breadth` (0-3): how widely used (optional in MVP)

## Output labels (MVP)
- `HIGH`: criticality 5 and exposure=1
- `MED`: criticality 3-4 and exposure=1
- `LOW`: exposure=1 and score is low
- `IGNORE`: exposure=0
- `REVIEW`: no touchpoints matched
