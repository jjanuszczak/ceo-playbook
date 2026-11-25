# Social Media Drafts: Why SQLite Beats the Filesystem on Small Blobs (And Why Git Doesn't Need It)

- **Source Article:** `content/articles/sqlite-filesystem-git-storage/index.md`
- **Campaign:** `thought-leadership`
- **Medium:** `social`
- **X URL:** `https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x`
- **LinkedIn URL:** `https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin`

## X

### Option 1: The 35% benchmark caveat
sqlite really is ~35% faster than the filesystem for 10kb blobs.

mostly because opening 1,000 files means 1,000 open/close syscalls, and block padding wastes 20% of your disk.

above 100kb? the filesystem wins again.

know where your workload sits before you rip out ext4.

https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x

### Option 2: BeFS vs WinFS
history already ran the database-as-filesystem experiment twice.

befs kept a fast journaled filesystem and added b+tree-indexed attributes. it still runs in haiku today.

winfs layered a sql server engine over ntfs. microsoft canceled it in 2006.

targeted hybrids beat wholesale replacement.

https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x

### Option 3: Git packfiles
every few months someone asks why git doesn't just use sqlite instead of `.git/objects/`.

answer: packfiles already solved the small-file problem.

`.pack` + `.idx` files collapse thousands of objects into one handle and add delta compression on top.

sqlite only helps at the loose-object edges.

https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=x

## LinkedIn

### Option 1: The Small-Blob Illusion and Why Targeted Hybrids Win
Every few months, the claim that "SQLite is 35% faster than the filesystem" makes the rounds in engineering circles, followed by the inevitable question: why don't we just store all files in a relational database?

The SQLite team's benchmark is real. For ~10 KB blobs, SQLite is roughly 35% faster and uses ~20% less space because it amortizes `open()`/`close()` system calls and eliminates 4 KB block slack. Independent production systems like Zerodha's Blobasaur have even beaten that on sub-1 KB reads using sharded SQLite files.

But the advantage flips back to the native filesystem above ~100 KB, and OS history shows what happens when you push the idea too far:
- **BeFS (BeOS / Haiku):** Kept an extent-based journaled filesystem and added B+tree-indexed extended attributes. It succeeded and still lives on.
- **WinFS (Microsoft):** Layered a SQL Server relational engine over NTFS, hit severe complexity and resource bottlenecks, and was canceled in 2006.

**So What?**
Great systems architecture rarely comes from forcing one abstraction to do everything. Use SQLite for high-volume small blobs and queryable metadata, keep large sequential files on the filesystem, and avoid dual-copy arbitration layers that create more operational pain than they solve.

https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin

### Option 2: Why Git Doesn't Need to Replace Packfiles with SQLite
If SQLite is faster than the filesystem for thousands of tiny files, shouldn't Git replace `.git/objects/` with a SQLite database?

It is a fair question, and the answer splits cleanly in two:
1. **Loose objects:** Individual zlib files under two-level directories (`.git/objects/ab/cdef...`) do pay the small-file syscall and inode tax. Single-file backends (and Git's `reftable` work) make sense here.
2. **Packfiles:** Mature repositories spend most of their time and space in `.pack` and `.idx` files, which already collapse thousands of objects into a single file handle while adding cross-object delta compression that a plain SQLite BLOB table does not give you for free.

Meanwhile, Fossil SCM (written by SQLite's creator) proves an all-SQLite VCS works brilliantly when designed from scratch around a single-file model, but it is not a drop-in Git replacement.

**So What?**
Before proposing a storage rewrite, check whether the existing system already has a packing layer solving the bottleneck. Targeted improvements at the edges beat rebuilding the core.

https://januszczak.org/articles/sqlite-filesystem-git-storage/?utm_campaign=thought-leadership&utm_medium=social&utm_source=linkedin
