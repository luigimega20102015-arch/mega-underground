# MEGA UNDERGROUND — Garage Unlimited

Goal: Single-player sandbox for vehicle customization using the original game's garage UI, with no career progression requirements. This document is a design specification, NOT a claim that unlocks are implemented.

## Principles
- Keep the original game data outside Git; users must supply their own compatible NFSU2 installation.
- Preserve upstream MIT licensing, attribution, and separation from copyrighted EA game assets.
- Do not change default upstream behavior without an explicit local opt-in.
- Avoid changing multiplayer progression, rank or network-visible car inventories.
- Preserve existing profile saves. Test with a new profile and backups first.

## Desired experience
1. Launch MEGA UNDERGROUND and select **Garage Unlimited**.
2. Open the original in-game Customize menu (no replacement 3D garage).
3. Select any vehicle supplied by the installed game's data, including hidden European models that upstream already enables.
4. Access all compatible visual and performance parts, including unique visual awards and widebody kits.
5. Apply upgrades without career stage, reputation, currency or race-win restrictions.
6. Save multiple distinct car builds and test-drive them.
7. Restore the last selected build on next launch.

## Implementation roadmap

### Phase 1 — Source tracing / tests
- Identify the actual frontend game mode entrypoint for Customize in the recompiled game.
- Locate code paths that compute car availability, parts availability and unique reward eligibility.
- Determine how vehicle selections and builds are serialized and whether Customize presets differ from career garages.
- Add a test fixture documenting which cars and visual parts appear in a clean profile.

### Phase 2 — Controlled unlock patch
- Add a local configuration option MEGA_GARAGE_UNLIMITED, default OFF.
- In that mode ONLY, bypass career and currency gates for Customize.
- Preserve model/part compatibility: do not mount nonexistent parts on incompatible cars.
- Preserve non-sandbox game modes and existing saves.

### Phase 3 — Garage-centric launch
- Add a **Garage Unlimited** launcher action.
- Start in the game or its closest supported Customize entrypoint.
- Provide **Test Drive** and **Back to Garage** with safe save/restore behavior.

### Phase 4 — Collection
- Implement named car configurations using the game's save mechanisms when possible.
- Backups and imports without overwriting career saves.

## Definition of done
- Brand-new clean profile: can select each installed original car without completing events.
- All compatible ordinary and unique visual parts are selectable for the relevant vehicle.
- Zero in-game money or racing progress required for parts.
- Save, quit, restart: garage build restored.
- No regression to ordinary Career, LAN or Online modes.

## Current status
- Planning branch created; implementation not yet present or play-tested.
- Upstream PLAYING.md documents existing Customize, European cars, and unique visual parts after Caleb.
- The game needs a user-provided PC game copy; generated C and WebAssembly artifacts are not checked in.
