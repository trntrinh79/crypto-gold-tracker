# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Bird (X/Twitter)
- **User:** @henlotrevor (Trevor)
- **Auth:**
  - `auth_token`: `79c13efb85307e627d24267c8725da27bc51ec72`
  - `ct0`: `93dd9fb9b977755912959e0e4c59251b4f8161af0c24f57f1e26ffa10ec21aff2ee05cedcf22c28c54bc10595142edec744d4a246ec7e2f09183e9168568bed789c6a89a6de2b64f82047cc45b7ebdbd`
- **Usage:** Pass these as `--auth-token` and `--ct0` flags when running `bird`.

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.