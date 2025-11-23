---
title: "Designing Around Constraints"
date: 2025-11-22
summary: "Explains why Git stores loose objects in 256 subdirectories keyed by the first two hash characters and how that simple layout optimizes filesystem performance and scalability."
description: "Details Git’s object storage strategy: content‑addressed objects (SHA hashes) are placed in a two‑character fan‑out (256 buckets) to avoid huge flat directories, speed lookups, and reduce filesystem pathology on older spinning disks. Covers loose objects vs. packfiles, partial‑hash lookups, historical constraints that shaped the design, and the broader lesson to solve real constraints rather than relying on faster hardware."
tags: 
   - "Technology"
   - "Design"
draft: false
---


_Git is a case study on cleverly designing around constraints vs throwing hardware at a problem_

## The Big Picture
The Git object layout is a classic case of "design around the actual constraints" instead of assuming "hardware will save us."

In 2005, when Linus Torvalds built Git:

- Spinning hard drives were slow at random seeks and directory lookups.
- Common filesystems (ext3, NTFS, etc.) choked badly once a directory crossed ~10,000–20,000 entries.
- A busy Linux kernel repository could easily generate hundreds of thousands of objects over time.
- SSDs basically didn’t exist for consumers, and even if you had fast hardware, many developers were on laptops or shared servers with mediocre disks.

Throwing "faster hardware" at it wouldn’t have helped most users, and it certainly wouldn’t have made Git usable on large projects back then. Instead, Linus chose a tiny, zero-cost software fix: split into 256 subdirectories using the first two hex digits of the hash. It costs almost nothing in code complexity, adds no runtime overhead, and completely sidesteps the filesystem pathology.

It’s a textbook example of thoughtful systems design:

- Solves the real bottleneck (filesystem behavior) rather than a symptom.
- Scales from tiny repos to monstrous ones with no configuration changes.
- Still beneficial today even on NVMe SSDs and modern filesystems (fewer directory entries = fewer inodes, less metadata pressure, faster clones on network filesystems, etc.).

You see the same philosophy elsewhere in Git: content-addressed storage, Merkle-tree history, packfiles, delta compression… almost everything is built to be stingy with I/O and robust on slow or unreliable hardware, because that was the reality when it was born. Faster CPUs and SSDs are nice bonuses, but Git didn’t need to wait for them to be blazingly fast. 

## Under the Covers
Git stores objects (blobs, trees, commits, and tags) in the `.git/objects` directory using a **loose object format** by default. Each object is identified by its **SHA-1 hash** (a 40-character hexadecimal string, e.g., `a1b2c3d4...` for SHA-1; Git now uses SHA-256 in some cases, but the structure is similar).

When storing a loose object:
- The **first two characters** of the hash become a **subdirectory** name (e.g., `a1`).
- The **remaining characters** become the **filename** inside that subdirectory (e.g., `b2c3d4...`).

So an object with hash `a1b2c3d4e5f6...` ends up at `.git/objects/a1/b2c3d4e5f6...`.

### Why This Specific Structure?
This is a deliberate performance optimization for filesystem efficiency:

1. **Avoids huge flat directories**  
   Many filesystems (especially ext3/ext4 in older configurations, ReiserFS, NTFS, and others common in the mid-2000s when Git was created) **slow down dramatically** or even have hard limits when a single directory contains tens or hundreds of thousands of files.  
   - Directory listing (`readdir`), lookups, and metadata operations become O(n) or worse.
   - Real-world examples: the Linux kernel repo can have millions of objects over time; putting them all directly under `.git/objects/` would make operations painfully slow.

2. **"Fan-out" with exactly 256 subdirectories**  
   Using the first two hex characters creates **256 possible subdirectories** (`00` to `ff`).  
   - This spreads objects roughly evenly (assuming uniform hash distribution).
   - Even in a repository with **millions of objects**, each subdirectory typically holds only a few thousand files — a number most filesystems handle efficiently.
   - The top-level `.git/objects/` directory itself stays tiny (just 256 entries + `pack/` and `info/`).

3. **One level is enough; deeper would be overkill**  
   - Two characters (1 byte) → 256 buckets → sufficient for virtually all repositories.
   - Using three characters (4096 subdirectories) would add unnecessary depth and overhead for typical repos.
   - Linus Torvalds and early Git developers chose this as a pragmatic sweet spot based on real filesystem behavior at the time.

4. **Bonus: Fast partial-hash lookups**  
   When you type a short unique hash (e.g., `git show a1b2c3`), Git only has to look in one specific subdirectory (`.git/objects/a1/`) and do a simple filename prefix match — very fast, even without an index.

### What Happens Later?
New objects start as **loose** (one file per object). Over time, `git gc` packs them into efficient **packfiles** (`.git/objects/pack/`) for storage and transfer, where this directory structure is no longer used. The fan-out is mainly for the loose phase.

This design has proven extremely effective and is why Git repositories remain fast even when they contain hundreds of thousands or millions of objects.