# GitHub Pages Setup — Deployment Candidate

> Prepared 2026-10-11; browser checks recorded in the changelogs. Owner review
> and an actual GitHub Pages deployment are pending.

The publishable tool is the entire `site/` directory, including its nine MP3s.
No npm install, build command, or TTS account is needed to host it.

## Deploy this project repository

1. Create your repository on GitHub and push this project to its default branch
   (`main` or `master`). Include `site/` and `.github/workflows/pages.yml`.
   The generated files in `output/` are ignored; the publishable copies in
   `site/data/audio/` are intentionally included in Git.
2. In the GitHub repository, open **Settings → Pages**. Under **Build and deployment**,
   set **Source** to **GitHub Actions**.
3. Open **Actions → Deploy Scripture Explained to GitHub Pages → Run workflow**
   on the default branch. Future pushes changing `site/` deploy automatically.
4. Open the URL shown by the successful deployment (normally
   `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`). Open it in Safari on the
   iPhone, pick a chapter, and tap Play.

The workflow publishes `site/` as the web root. Do not select the repository root
as a branch publishing source when using this folder structure; that root does
not contain the app's `index.html`. The workflow skips non-default branches.
If using a default branch other than main/master, add its name to the push
trigger in `pages.yml`; manual dispatch already supports the default branch.

These steps follow [GitHub's publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Alternative: a separate website-only repository

Extract the provided `Scripture_Explained_GitHub_Pages.zip` into a separate
repository's root, so `index.html`, `assets/`, and `data/` are directly in the root.
In Settings → Pages choose **Deploy from a branch**, then the default branch and
**/(root)**. The ZIP contains the ready website, not this project's source tools.

## Local preview

From this project directory, use the existing isolated Python installation:

```powershell
.\.tools\tts_env\Scripts\python.exe tools/preview_site.py
```

Then open `http://127.0.0.1:8765/`. Stop the server with Ctrl+C when finished.
Any standard Python 3 installation can run the preview tool without dependencies.
Opening `site/index.html` directly as a file can block the transcript JSON request;
use the preview server or GitHub Pages.

## Refreshing prepared content

After editing and rendering the local session files, export again:

```powershell
.\.tools\tts_env\Scripts\python.exe tools/prepare_site.py
```

Commit the refreshed `site/data/library.json` and MP3s. The exporter does not
regenerate speech or download sources. It rejects stale session/rendering data.

## First iPhone check

Test Play, lock the screen, and check continued audio and system controls. Also
check next-chapter playback and the car's Bluetooth controls. The player provides
[Media Session controls](https://developer.mozilla.org/en-US/docs/Web/API/Media_Session_API)
where supported, but this machine's Chrome tests cannot verify the iPhone's
behavior. This initial hosted version requires connectivity to load chapter audio;
it does not yet save the full week for reliable offline use.
