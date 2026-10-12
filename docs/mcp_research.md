# Gospel Library MCP Research

> Reviewed: 2026-10-11. Evidence: repository documentation, source code, GitHub
> metadata, and the official Church curriculum index. Neither server was
> installed or invoked; reliability and content completeness are not verified.

## Recommendation

Test **jasonbellz/gospel-library-mcp** first because its generic article fetch
offers a plausible route to the required lesson pages as well as scriptures.
This is a candidate recommendation, not an adopted dependency. Adam Harris's
server may be useful for database-backed scripture access, but the reviewed
tools do not provide Come, Follow Me lesson retrieval.

## Comparison

| Area | Jason Bell | Adam Harris |
|------|------------|-------------|
| Registered tools | Search, article fetch, category browse, scripture lookup. | Exact scripture, keyword scripture search, random scripture, conference search. |
| Content source | Fetches live Church pages; local index supports search. | Queries a supplied SQLite database locally or a Cloudflare D1 binding remotely. |
| Chapters | Parser accepts whole chapters and verse ranges. Validate extracted text and verse coverage. | Tool is oriented to explicit verse/range requests; complete chapters need additional handling. |
| Weekly lessons | Generic article retrieval can target a known official lesson URL. | No lesson retrieval tool found in the reviewed registration source. |
| Runtime | Local Node process using stdio MCP. | Local stdio entry point plus Cloudflare remote entry point. |
| Main setup dependency | Node and packages; semantic index is optional for direct retrieval. | Packages and a populated database; obtaining that dataset remains unresolved. |
| Code license evidence | MIT LICENSE file present. | No LICENSE file or recognized license found in the reviewed tree/metadata; clarify before reuse. |
| Runtime status here | Not tested. | Not tested; existing hosted endpoint was not invoked. |

Sources: [Jason's README](https://github.com/jasonbellz/gospel-library-mcp),
[Jason's tool registration](https://github.com/jasonbellz/gospel-library-mcp/blob/0fbf617d86057e3e3c62396936cf1fac290dc369/src/index.ts),
[Jason's reference parser](https://github.com/jasonbellz/gospel-library-mcp/blob/0fbf617d86057e3e3c62396936cf1fac290dc369/src/tools/scripture.ts),
[Adam's README](https://github.com/adammharris/gospel-library-mcp),
[Adam's shared tools](https://github.com/adammharris/gospel-library-mcp/blob/8f9fdca21eabe1296e8892ec3a6f3b7251379745/src/shared-tools.ts),
[Adam's local server](https://github.com/adammharris/gospel-library-mcp/blob/8f9fdca21eabe1296e8892ec3a6f3b7251379745/src/stdio-server.ts),
and [Adam's remote server](https://github.com/adammharris/gospel-library-mcp/blob/8f9fdca21eabe1296e8892ec3a6f3b7251379745/src/index.ts).

## Important findings beyond the README descriptions

### Current Come, Follow Me search coverage

Jason's index builder includes `come-follow-me-for-individuals-and-families-`
and `come-follow-me-for-sunday-school-` paths. It does not include the current
`come-follow-me-for-home-and-church-` pattern. Therefore a locally built semantic
index from this reviewed code will exclude the 2026 Home and Church manual;
the contents of a downloaded prebuilt index were not checked. Direct URL
fetching is independent of that index. Use verified lesson URLs for validation
instead of depending on semantic search to find the current week's lesson.
[Index builder source](https://github.com/jasonbellz/gospel-library-mcp/blob/0fbf617d86057e3e3c62396936cf1fac290dc369/src/lib/indexer.ts).

The official [2026 curriculum contents](https://www.churchofjesuschrist.org/study/manual/come-follow-me-for-home-and-church-old-testament-2026/000-contents?lang=eng)
provides week/date mappings and includes readings from Moses and Abraham along
with the Old Testament. Do not infer all assigned books from the manual title.
Its January 5-11 lesson assigns Moses 1 and Abraham 3, a useful small validation
case. Date/year, special weeks, and manual identity should come from the official
index rather than assumed URL numbering or a fixed weekly calculation.

### Text extraction needs validation

Jason's verse fetch collects available `#pN` elements. If no requested verse
elements exist, it falls back to the full article; if only some exist, it can
return a partial range. Article extraction can also fall back to the page body.
Validate verse coverage and content boundaries before narration. The fetcher
removes footnote markers and drops footnote anchor links while retaining their
visible words; it is not a complete footnote/cross-reference model.
[Fetch implementation](https://github.com/jasonbellz/gospel-library-mcp/blob/0fbf617d86057e3e3c62396936cf1fac290dc369/src/tools/fetch.ts).

Adam's scripture parser treats a general two-part reference such as `Genesis 2`
as chapter 1, verse 2. Request explicit chapter:verse ranges when testing it;
do not assume bare chapter references mean whole chapters. Its documented
50-verse range limit also requires checking the implementation and splitting
long requests. Conference retrieval by ID truncates long talk text at 1,500
characters in the reviewed code, despite a message suggesting an ID yields full
text. This matters if supplemental talks are used later.
[Shared-tool implementation](https://github.com/adammharris/gospel-library-mcp/blob/8f9fdca21eabe1296e8892ec3a6f3b7251379745/src/shared-tools.ts).

## Future validation plan

1. Establish the Node runtime and pin the tested repository revision/package
   version. Inspect installation dependencies before execution.
2. Start Jason's server in a controlled local setup and enumerate its tools.
   Do not build or download a full semantic index for the first retrieval test.
3. Follow the official 2026 contents to the January 5-11 lesson. Fetch that exact
   page with English selected and confirm lesson sections, scripture references,
   and links survive extraction.
4. Fetch Moses 1 as a chapter and an explicit small verse range. Compare with the
   official chapter page, including verse order and words carrying footnotes.
5. Check a longer chapter, invalid reference, missing lesson, and network failure.
   Record partial/fallback output explicitly; it must not silently become a valid
   complete session.
6. Only after retrieval succeeds, use the lesson plus the checked chapter to
   prepare a short commentary script and have the owner review alignment.
7. Record evidence and actual dead ends, then choose or reject the candidate.

Neither candidate supplies the explanation model, TTS engine, player, or
application integration. Those are separate decisions.

## Research snapshot

| Repository | Reviewed main commit | Commit date (UTC) |
|------------|----------------------|-------------------|
| jasonbellz/gospel-library-mcp | `0fbf617d86057e3e3c62396936cf1fac290dc369` | 2026-03-25 |
| adammharris/gospel-library-mcp | `8f9fdca21eabe1296e8892ec3a6f3b7251379745` | 2025-08-14 |

These revisions make the findings reproducible. Recheck upstream changes before
installation; commit recency does not establish quality or reliability.
