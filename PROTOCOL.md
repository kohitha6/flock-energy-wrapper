# Protocol Specification: Urja Meter Ops

## Overview
The "Urja Meter Ops" portal is a legacy server-rendered web application used by utility operations staff to track 403 smart meters across distribution transformers (DTs).

## Authentication Mechanism
- Uses form-based session login (`/login`).
- Relies on persistent HTTP cookies to maintain authorized state across page requests.

## Data Structure & Scraping Strategy
- Pages return standard HTML with data structured inside HTML tables (`<table>`, `<tr>`, `<td>`).
- Pagination is query-param driven (`?page=N`), spanning 21 total pages for meter listings.
- Key fields parsed: Meter Number, Serial, Make, Phase, Status, and Associated Distribution Transformer (DT).

## Known Quirks
- No native JSON API exists; all data extraction requires scraping HTML tables.
- Sessions can time out if inactive, requiring re-authentication logic in the background wrapper.