# Upload MASTER_V9 notebooks to the existing GitHub repository

Correct URL: https://github.com/tesdem/STATISTICS-BOOK (not `https://github/tesdem/STATISTICS-BOOK`).

**Recommended—preserve existing notebooks:**
1. Sign in to GitHub and open the repository. Select **Code → Download ZIP** to save a backup (or `git clone https://github.com/tesdem/STATISTICS-BOOK.git`).
2. Unzip this MASTER_V9 package on your computer. Compare the chapter notebooks against the repository before overwriting existing files. New chapters 22A and 27A, and updated Chapter 42A are the priority. The package reconstructs the other notebooks and is not guaranteed identical to the originals.
3. With Git installed, in the cloned existing repository, copy the chosen V9 files/folders into place, then run:

```bash
git add .
git commit -m "Add MASTER_V9 companion notebooks and chapter updates"
git push origin main
```

4. Refresh the repository page and confirm files and index appear. Update the repository README and ensure any publicly shared observed CSV meets licence/redistribution terms.

**Alternative browser upload:** Open the repo → **Add file** → **Upload files**. Upload extracted files in batches, retaining their folder structure, then **Commit changes**. Git command-line upload is better for many folders.

Do not upload `.venv`, credentials or private files.
