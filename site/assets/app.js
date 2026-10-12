"use strict";

(() => {
  const $ = (id) => document.getElementById(id);
  const audio = $("audio");
  const storageKey = "scripture-explained:2026-10-12:v1";
  const dataBase = new URL("./data/", document.baseURI);
  const controls = ["previous", "back", "play", "forward", "next", "seek", "speed", "autoplay"];
  let library, index = 0, pendingTime = null, activeSegment = -1, segmentElements = [];
  let playRequest = 0, lastSaved = 0, scrubbing = false;
  let saved = {};
  try {
    const value = JSON.parse(localStorage.getItem(storageKey) || "{}");
    if (value && typeof value === "object") saved = value;
  } catch (_) { /* Playback still works when browser storage is unavailable. */ }

  const formatTime = (value) => {
    const seconds = Math.max(0, Math.floor(Number(value) || 0));
    return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`;
  };
  const chapter = () => library.chapters[index];
  const length = () => Number.isFinite(audio.duration) ? audio.duration : chapter().duration;
  const setStatus = (message) => { $("player-status").textContent = message; };

  function remember(force = false) {
    if (!library || pendingTime !== null) return;
    const now = Date.now();
    if (!force && now - lastSaved < 1000) return;
    lastSaved = now;
    saved = {
      chapterId: chapter().id,
      time: audio.currentTime,
      speed: Number($("speed").value),
      autoplay: $("autoplay").checked,
      follow: $("follow").checked,
    };
    try { localStorage.setItem(storageKey, JSON.stringify(saved)); } catch (_) {}
  }

  function playbackUI() {
    const playing = !audio.paused && !audio.ended;
    $("play").setAttribute("aria-label", playing ? "Pause" : "Play");
    $("play").title = playing ? "Pause" : "Play";
    $("play-symbol").setAttribute("d", playing ? "M6 4h4v16H6zM14 4h4v16h-4z" : "M8 4l12 8-12 8z");
    if ("mediaSession" in navigator) {
      try { navigator.mediaSession.playbackState = playing ? "playing" : "paused"; } catch (_) {}
    }
  }

  function updatePosition() {
    if (!library) return;
    const time = pendingTime ?? audio.currentTime;
    const duration = length();
    $("seek").max = duration;
    if (!scrubbing) $("seek").value = time;
    $("seek").setAttribute("aria-valuetext", `${formatTime(time)} of ${formatTime(duration)}`);
    $("elapsed").textContent = formatTime(time);
    $("duration").textContent = formatTime(duration);
    let nextSegment = -1;
    chapter().segments.forEach((segment, i) => { if (time >= segment.start) nextSegment = i; });
    if (nextSegment !== activeSegment) {
      if (activeSegment >= 0) segmentElements[activeSegment].classList.remove("is-current");
      activeSegment = nextSegment;
      if (activeSegment >= 0) {
        const element = segmentElements[activeSegment];
        element.classList.add("is-current");
        if ($("follow").checked && !audio.paused && !scrubbing) {
          element.scrollIntoView({ block: "center", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
        }
      }
    }
    if ("mediaSession" in navigator && "setPositionState" in navigator.mediaSession && Number.isFinite(audio.duration) && audio.duration > 0) {
      try {
        navigator.mediaSession.setPositionState({ duration: audio.duration, playbackRate: audio.playbackRate, position: Math.min(audio.currentTime, audio.duration) });
      } catch (_) { /* Some Safari versions expose only part of Media Session. */ }
    }
  }

  function seekTo(time) {
    const target = Math.min(length(), Math.max(0, Number(time) || 0));
    if (audio.readyState >= 1) {
      audio.currentTime = target;
      pendingTime = null;
    } else pendingTime = target;
    updatePosition();
    remember(true);
    if (audio.paused) setStatus(`Ready to play from ${formatTime(target)}.`);
  }

  async function play() {
    const request = ++playRequest;
    setStatus("Loading audio…");
    try {
      await audio.play();
      if (request === playRequest) setStatus("Scripture and commentary · follow along below");
    } catch (error) {
      if (request !== playRequest || error.name === "AbortError") return;
      setStatus(error.name === "NotAllowedError" ? "Tap Play to begin listening." : "Audio could not play. Check your connection and tap Play again.");
      playbackUI();
    }
  }

  function renderTranscript() {
    const fragment = document.createDocumentFragment();
    segmentElements = chapter().segments.map((segment, i) => {
      const article = document.createElement("article");
      article.className = "transcript-segment";
      article.dataset.role = segment.role;
      const heading = document.createElement("div");
      heading.className = "segment-heading";
      const label = document.createElement("h3");
      label.textContent = segment.role === "scripture" ? "Scripture" : "Commentary";
      const jump = document.createElement("button");
      jump.className = "segment-jump";
      jump.textContent = formatTime(segment.start);
      jump.setAttribute("aria-label", `Listen to ${label.textContent.toLowerCase()} at ${formatTime(segment.start)}`);
      jump.addEventListener("click", () => { seekTo(segment.start); play(); });
      heading.append(label, jump);
      article.append(heading);
      if (segment.role === "scripture") {
        segment.verses.forEach((verse) => {
          const paragraph = document.createElement("p");
          const number = document.createElement("span");
          number.className = "verse-number";
          number.textContent = verse.number;
          paragraph.append(number, document.createTextNode(verse.text));
          article.append(paragraph);
        });
      } else {
        segment.text.split(/\n\s*\n/).forEach((text) => {
          const paragraph = document.createElement("p");
          paragraph.textContent = text;
          article.append(paragraph);
        });
      }
      fragment.append(article);
      return article;
    });
    $("transcript").replaceChildren(fragment);
    const sources = chapter().sources.map((source) => {
      const item = document.createElement("li"), link = document.createElement("a");
      link.textContent = source.title;
      link.href = source.url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      item.append(link);
      return item;
    });
    $("source-list").replaceChildren(...sources);
    activeSegment = -1;
  }

  function selectChapter(nextIndex, continuePlaying = false, time = 0) {
    if (nextIndex < 0 || nextIndex >= library.chapters.length) return;
    remember(true);
    ++playRequest;
    audio.pause();
    index = nextIndex;
    pendingTime = Math.max(0, Math.min(time, chapter().duration));
    audio.src = new URL(chapter().audio, dataBase).href;
    audio.load();
    audio.playbackRate = Number($("speed").value);
    $("chapter-title").textContent = chapter().title;
    $("chapter-focus").textContent = chapter().focus;
    $("chapter-count").textContent = `${index + 1} / ${library.chapters.length}`;
    document.title = `${chapter().title} · Scripture Explained`;
    $("previous").disabled = index === 0;
    $("next").disabled = index === library.chapters.length - 1;
    [...$("chapter-list").children].forEach((button, i) => {
      button.setAttribute("aria-current", i === index ? "true" : "false");
    });
    renderTranscript();
    setStatus(pendingTime > 0 ? `Ready to resume at ${formatTime(pendingTime)}.` : "Ready when you are.");
    if ("mediaSession" in navigator && "MediaMetadata" in window) {
      try {
        navigator.mediaSession.metadata = new MediaMetadata({
          title: chapter().title,
          artist: "Scripture Explained",
          album: `${library.title} · ${library.dates}`,
          artwork: [{ src: new URL("./assets/book.svg", document.baseURI).href, sizes: "any", type: "image/svg+xml" }],
        });
      } catch (_) {}
    }
    updatePosition();
    playbackUI();
    // Keep this immediate: mobile playback must retain the user's tap gesture.
    if (continuePlaying) play();
  }

  function changeChapter(offset) { selectChapter(index + offset, !audio.paused); }

  function mediaControls() {
    if (!("mediaSession" in navigator)) return;
    const actions = {
      play,
      pause: () => { ++playRequest; audio.pause(); },
      seekbackward: (details) => seekTo(audio.currentTime - (details.seekOffset || 15)),
      seekforward: (details) => seekTo(audio.currentTime + (details.seekOffset || 15)),
      seekto: (details) => seekTo(details.seekTime),
      previoustrack: () => changeChapter(-1),
      nexttrack: () => changeChapter(1),
    };
    Object.entries(actions).forEach(([action, handler]) => {
      try { navigator.mediaSession.setActionHandler(action, handler); } catch (_) {}
    });
  }

  audio.addEventListener("loadedmetadata", () => {
    if (!library) return;
    if (pendingTime !== null) {
      audio.currentTime = Math.min(pendingTime, audio.duration || chapter().duration);
      pendingTime = null;
    }
    audio.playbackRate = Number($("speed").value);
    updatePosition();
    remember(true);
  });
  audio.addEventListener("timeupdate", () => { updatePosition(); remember(); });
  audio.addEventListener("play", playbackUI);
  audio.addEventListener("pause", () => { playbackUI(); remember(true); });
  audio.addEventListener("playing", () => setStatus("Scripture and commentary · follow along below"));
  audio.addEventListener("waiting", () => { if (!audio.paused) setStatus("Buffering audio…"); });
  audio.addEventListener("error", () => setStatus("Audio could not load. Check your connection and try Play again."));
  audio.addEventListener("ended", () => {
    remember(true);
    if ($("autoplay").checked && index < library.chapters.length - 1) selectChapter(index + 1, true);
    else setStatus(index === library.chapters.length - 1 ? "You’ve reached the end of this week’s reading." : "Chapter complete. Choose Next when you’re ready.");
    playbackUI();
  });
  $("play").addEventListener("click", () => {
    if (audio.paused) play();
    else { ++playRequest; audio.pause(); setStatus("Paused · your place is saved."); }
  });
  $("previous").addEventListener("click", () => changeChapter(-1));
  $("next").addEventListener("click", () => changeChapter(1));
  $("back").addEventListener("click", () => seekTo((pendingTime ?? audio.currentTime) - 15));
  $("forward").addEventListener("click", () => seekTo((pendingTime ?? audio.currentTime) + 15));
  $("seek").addEventListener("input", () => { scrubbing = true; $("elapsed").textContent = formatTime($("seek").value); });
  $("seek").addEventListener("change", () => { const time = Number($("seek").value); scrubbing = false; seekTo(time); });
  $("speed").addEventListener("change", () => { audio.playbackRate = Number($("speed").value); updatePosition(); remember(true); });
  $("autoplay").addEventListener("change", () => remember(true));
  $("follow").addEventListener("change", () => remember(true));
  window.addEventListener("pagehide", () => remember(true));
  document.addEventListener("visibilitychange", () => { if (document.hidden) remember(true); });

  async function initialize() {
    controls.forEach((id) => { $(id).disabled = true; });
    try {
      const response = await fetch(new URL("library.json", dataBase));
      if (!response.ok) throw new Error(`Library request: ${response.status}`);
      library = await response.json();
      if (!Array.isArray(library.chapters) || !library.chapters.length) throw new Error("Empty library");
      $("lesson-title").textContent = library.title;
      $("lesson-dates").textContent = library.dates;
      $("lesson-reading").textContent = library.reading;
      $("lesson-link").href = library.lessonUrl;
      $("week-length").textContent = `${library.chapters.length} chapters · ${Math.round(library.chapters.reduce((sum, entry) => sum + entry.duration, 0) / 60)} min`;
      const rates = [...$("speed").options].map((option) => option.value);
      $("speed").value = rates.includes(String(saved.speed)) ? String(saved.speed) : "1";
      $("autoplay").checked = saved.autoplay === true;
      $("follow").checked = saved.follow === true;
      library.chapters.forEach((entry, i) => {
        const button = document.createElement("button");
        button.className = "chapter-button";
        button.setAttribute("aria-label", `${entry.title}, ${formatTime(entry.duration)}`);
        const name = document.createElement("span"), time = document.createElement("span");
        name.className = "chapter-name";
        name.textContent = entry.title;
        time.className = "chapter-time";
        time.textContent = formatTime(entry.duration);
        button.append(name, time);
        button.addEventListener("click", () => { if (i !== index) selectChapter(i, !audio.paused); });
        $("chapter-list").append(button);
      });
      controls.forEach((id) => { $(id).disabled = false; });
      const restoreIndex = library.chapters.findIndex((entry) => entry.id === saved.chapterId);
      // Capture saved time before chapter selection writes new playback state.
      const restoreTime = Number.isFinite(saved.time) ? saved.time : 0;
      pendingTime = 0;
      selectChapter(Math.max(0, restoreIndex), false, restoreTime);
      mediaControls();
      audio.controls = false;
      $("enhanced-controls").hidden = false;
    } catch (_) {
      setStatus("The transcript could not load. Open this page through GitHub Pages or the local preview server, then refresh.");
      $("chapter-focus").textContent = "You can still play Isaiah 58 using the audio controls.";
      $("transcript").textContent = "Transcript unavailable. Please refresh when connected.";
      audio.src = new URL("audio/Isaiah_58_Explained.mp3", dataBase).href;
    }
  }
  initialize();
})();
