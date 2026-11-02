# MEGA UNDERGROUND — mod staging (prototype)

This folder defines a **metadata-only** staging format for user-supplied vehicle add-ons. It does **not** install cars, convert NFSU2 formats, load assets, patch WebAssembly, or replace NFSU2 Unlimiter.

## Local workflow
1. Keep an original, legally obtained NFSU2 PC v1.2 installation **outside Git**.
2. Obtain add-on car packs from their authors, checking redistribution terms.
3. Unpack each pack in a local private directory, not in this repository.
4. Create one JSON manifest using `vehicle-manifest.example.json` and validate it:
   `python3 mega_mods/validate_manifest.py path/to/vehicle.json`
5. Once actual game integration exists, use the manifest to identify model, parts, dependencies, and potential conflicts.

## Compatibility states
- `metadata-only`: manifest passes validation; **no runtime compatibility guaranteed**.
- `native-pc-tested`: manually confirmed in the supported PC setup.
- `web-tested`: future milestone after engine/asset loader work.

Avoid assuming an ASI/DLL will execute in WebAssembly. A valid manifest doesn't make the vehicle playable.

No game files, author-created car assets, or proprietary binaries should be committed without appropriate rights.
