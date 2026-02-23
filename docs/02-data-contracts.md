# Data Contracts

## Config Snapshot (config-snapshot.json)
Fields:
- tenantId
- capturedAtUtc
- category
- objects[]:
  - objectType
  - objectId
  - name
  - orgScope
  - payloadHash
  - payload (optional for MVP storage size control)

## Release Item (release-items.json)
Fields:
- releaseId
- publishDate
- module
- title
- type
- description
- tags[] (derived)
- touchpoints[] (mapped)
- requiresAction (boolean)