#!/usr/bin/env python3
"""Phase 0 evidence tools. Never collect the official bus navigation website.

Python 3.10+, standard library only. Catalog results are discovery evidence,
not proof that a particular route or trip is available.
"""

import argparse
import csv
import gzip
import hashlib
import io
import json
import sys
import unicodedata
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path


CATALOG_URLS = (
    "https://api.gtfs-data.jp/v2/feeds?pref=12",
    "https://api.gtfs-data.jp/v2/feeds?org_name=%E4%BA%AC%E6%88%90",
    "https://api.gtfs-data.jp/v2/files?pref=12&target_date=2026-11-08",
)
PUBLIC_FIELDS = (
    "organization_id", "organization_name", "feed_id", "feed_name",
    "feed_license", "feed_license_id", "feed_license_url",
    "latest_feed_start_date", "latest_feed_end_date", "last_published_at",
    "file_from_date", "file_to_date", "file_url", "real_time",
)


def now():
    return datetime.now(timezone.utc).isoformat()


def catalog():
    results = []
    for url in CATALOG_URLS:
        request = urllib.request.Request(url, headers={"User-Agent": "buss-phase0/0.3"})
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read(8_000_001)
            if len(raw) > 8_000_000:
                raise ValueError("Catalog response exceeded the research size limit")
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            data = json.loads(raw)
            if data.get("code") != 200 or not isinstance(data.get("body"), list):
                raise ValueError("Unexpected public catalog response")
            items = data["body"]
            results.append({
                "url": url,
                "retrieved_at": now(),
                "http_status": response.status,
                "decoded_body_sha256": hashlib.sha256(raw).hexdigest(),
                "record_count": len(items),
                "records": [{k: item[k] for k in PUBLIC_FIELDS if k in item}
                            for item in items],
            })
    return {
        "purpose": "Public catalog discovery, not target-service verification",
        "metadata_attribution": "GTFSデータリポジトリ / 一般社団法人社会基盤情報流通推進協議会 (AIGID)",
        "metadata_license": "CC BY 4.0 (repository terms, Article 5.2)",
        "metadata_terms_url": "http://docs.gtfs-data.jp/site/kiyaku.pdf",
        "modification": "Selected metadata fields; contact fields omitted",
        "target_route_data_verified": False,
        "results": results,
    }


def inspect_gtfs(path):
    raw = path.read_bytes()
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        def rows(name):
            with archive.open(name) as stream:
                return list(csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8-sig")))

        stops, routes, trips = (rows(name) for name in ("stops.txt", "routes.txt", "trips.txt"))
        stop_matches = [s["stop_id"] for s in stops
                        if any(n in s["stop_name"] for n in ("稲毛駅", "長沼原町"))]
        route_matches = [r["route_id"] for r in routes
                         if any(n in unicodedata.normalize("NFKC", " ".join(r.values()))
                                for n in ("稲31", "稲32"))]
        return {
            "inspected_at": now(),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "agency_names": [a["agency_name"] for a in rows("agency.txt")],
            "stop_count": len(stops), "route_count": len(routes), "trip_count": len(trips),
            "target_stop_name_matches": stop_matches,
            "target_route_name_matches": route_matches,
            "feed_info": rows("feed_info.txt") if "feed_info.txt" in archive.namelist() else [],
            "target_route_data_verified": False,
            "scope": "Name screening only; positive matches still require stop_times, service dates, direction and boarding/alighting validation",
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--catalog", action="store_true", help="GET three documented public metadata endpoints once")
    group.add_argument("--gtfs", type=Path, help="Inspect a local, lawfully obtained GTFS ZIP offline")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = catalog() if args.catalog else inspect_gtfs(args.gtfs)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        print(f"Verification failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
