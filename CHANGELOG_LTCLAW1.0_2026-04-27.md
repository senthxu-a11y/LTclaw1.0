# LTclaw1.0 Local Modification Log

Date: 2026-04-27

This file summarizes the local source changes completed for the customized
`LTclaw1.0` desktop/client build.

## Completed changes

### 1. Desktop startup and WebView stability

- Fixed the desktop startup path so the desktop client can actually open a
  native window instead of only starting the backend.
- Forced Windows desktop startup to use the `edgechromium` backend in
  `pywebview`.
- Added desktop wrapper logging to:
  `C:\Users\xuguangyao\.ltclaw_gy_x\desktop_logs\desktop.wrapper.log`
- Changed the validated Windows launch path to use `pythonw.exe` for
  no-console startup while preserving the desktop window.
- Restored the desktop window to normal windowed mode instead of default
  maximized/fullscreen startup.

### 2. Branding cleanup

- Replaced visible `QwenPaw` branding in the customized runtime path with
  `LTCLAW-GY.X` in the console title/header and Windows packaging metadata.
- Updated the header version display to use the project/backend version.
- Cleaned multiple Windows packaging remnants that still referenced the old
  product naming.

### 3. Telemetry and init cleanup

- Removed telemetry-related code paths and prompt/marker logic from init and
  related runtime code.
- Simplified startup behavior so customized builds do not show the old
  telemetry/init guidance path.

### 4. Console/UI runtime fixes

- Fixed runtime CSS selector coverage for the actual prefixed class names used
  by the app so the sidebar and related layout styles apply correctly.
- Reduced frontend dynamic import warnings by narrowing page module discovery
  to actual route/page entry modules instead of broad page internals.
- Cleaned the TypeScript app config by removing deprecated `baseUrl` usage and
  preserving the `@/*` alias via `./src/*`.

### 5. Windows packaging chain cleanup

- Fixed Windows build scripts that still referenced non-existent
  `src/qwenpaw/...` paths.
- Updated wheel/packaging scripts to use the real `ltclaw_gy_x` package name.
- Updated the packaged Windows launcher scripts to call `ltclaw_gy_x` instead
  of old `qwenpaw` entry points.
- Fixed the NSIS installer registry path to use `LTCLAW-GY.X`.

### 6. Runtime/process cleanup

- Confirmed runtime data directories are under the user profile:
  - `C:\Users\xuguangyao\.ltclaw_gy_x`
  - `C:\Users\xuguangyao\.ltclaw_gy_x.secret`
- Removed stray root-level workdir copies and an unused `fix_classnames.py`.
- Fixed Windows shutdown/process enumeration text decoding so shutdown no
  longer emits GBK decode exceptions during process scanning.

## Verification completed

- Desktop window successfully launched and showed the title
  `LTCLAW-GY.X Desktop`.
- Python compile checks passed for the touched backend/CLI files.
- Frontend TypeScript config validation passed.
- `npm run build` passed.
- Git worktree was cleaned and committed after the changes.

## Key commits from this customization round

- `27f2614` Clean desktop runtime and LTCLAW-GY.X branding
- `1386463` Reduce frontend dynamic import warnings
- `4d4be78` Stabilize Windows desktop startup
- `86a8257` Finalize desktop window sizing and tsconfig cleanup

