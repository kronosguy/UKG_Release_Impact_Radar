# Architecture

## Power Automate components
1. Snapshot flow
   - Pull config categories
   - Normalize
   - Store snapshot artifacts

2. Release ingest flow
   - Collect release items
   - Normalize
   - Store release artifacts

3. Impact compute flow
   - Load latest snapshot + release items + mapping rules
   - Map release -> touchpoints -> config exposure
   - Score and rank
   - Write outputs (report + queue + change log)

## Storage (no Dataverse assumption)
- SharePoint document library OR OneDrive folder for JSON artifacts
- GitHub repo stores documentation + mapping rules + exported reports