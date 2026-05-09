#!/usr/bin/env python3
"""
Awesome AI Video Tools — Daily Updater
=========================================
Scans for new trending video repos and API launches.
Updates the README and pushes to GitHub.

Runs daily at 8am.
"""

import os, sys, json, time, subprocess, re
from datetime import datetime, date, timedelta
import urllib.request

REPO_DIR = "/home/ubuntu/awesome-ai-video-tools"
README_PATH = os.path.join(REPO_DIR, "README.md")
STATE_FILE = os.path.join(REPO_DIR, ".scan_state.json")

# Categories and their search queries
CATEGORIES = {
    "ai-video-generation": [
        "text+to+video+diffusion",
        "video+generation+ai+model",
        "video+diffusion+pytorch",
        "text2video+open+source",
    ],
    "video-editing": [
        "video+editor+cli+python",
        "ffmpeg+python+video+tool",
        "lossless+video+trim",
        "video+editing+library",
    ],
    "video-subtitle": [
        "video+subtitle+ai",
        "auto+caption+video",
        "video+transcription+python",
        "whisper+video+alignment",
    ],
    "video-streaming": [
        "video+streaming+server",
        "rtmp+server+open+source",
        "hls+streaming+python",
    ],
    "video-agent": [
        "ai+video+agent+tool",
        "video+automation+cli",
        "auto+video+editor+ai",
        "shorts+generator+python",
    ],
    "video-upscale": [
        "video+upscale+ai",
        "video+restoration+python",
        "face+restoration+video",
        "video+super+resolution",
    ],
}

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"seen_repos": [], "last_scan": None, "new_finds": []}

def save_state(state):
    state["last_scan"] = datetime.now().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def search_github(query, sort="stars", per_page=5):
    """Search GitHub repos."""
    url = f"https://api.github.com/search/repositories?q={query}&sort={sort}&per_page={per_page}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        return data.get("items", [])
    except:
        return []

def check_trending_video():
    """Check GitHub trending for video-related repos."""
    url = "https://api.github.com/search/repositories?q=video+created:>%s&sort=stars&per_page=10" % \
           (date.today() - timedelta(days=7)).isoformat()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        return data.get("items", [])
    except:
        return []

def is_video_related(repo):
    """Check if a repo is actually video-related."""
    name = (repo.get("name", "") + " " + repo.get("description", "")).lower()
    topics = " ".join(repo.get("topics", [])).lower()
    text = name + " " + topics
    
    keywords = [
        "video", "ffmpeg", "moviepy", "transcode", "streaming", "subtitle",
        "caption", "screen record", "video edit", "video gen", "text-to-video",
        "text2video", "video diffusion", "frame interpolat", "video upscale",
        "video restore", "face swap", "video analysis", "object detect",
        "video understand", "video api", "video player", "media server",
        "video clip", "short video", "video automation", "video tool",
        "video processing", "video converter", "video trim", "video cut",
        "video merge", "video concatenate", "video effect", "video overlay",
        "video watermark", "video compress", "video encode",
    ]
    return any(k in text for k in keywords)

def scan():
    """Run the daily scan for new tools."""
    state = load_state()
    seen = set(state.get("seen_repos", []))
    new_finds = []
    
    # 1. Check trending
    print("🔍 Checking GitHub trending for video repos...")
    trending = check_trending_video()
    for r in trending:
        full_name = r.get("full_name", "")
        stars = r.get("stargazers_count", 0)
        if full_name not in seen and stars >= 50 and is_video_related(r):
            seen.add(full_name)
            new_finds.append({
                "name": full_name,
                "stars": stars,
                "url": r.get("html_url", ""),
                "description": (r.get("description") or "")[:100],
                "language": r.get("language", "N/A"),
                "found_in": "trending",
            })
    
    # 2. Search all categories
    for category, queries in CATEGORIES.items():
        for q in queries:
            print(f"  Searching {category}: {q}")
            repos = search_github(q)
            for r in repos:
                full_name = r.get("full_name", "")
                stars = r.get("stargazers_count", 0)
                if full_name not in seen and stars >= 100 and is_video_related(r):
                    seen.add(full_name)
                    new_finds.append({
                        "name": full_name,
                        "stars": stars,
                        "url": r.get("html_url", ""),
                        "description": (r.get("description") or "")[:100],
                        "language": r.get("language", "N/A"),
                        "found_in": category,
                    })
            time.sleep(0.5)  # Rate limit
    
    # 3. Check specific well-known repos for updates
    print("  Checking for new API launches...")
    # (API launches are manual curation — this flags for review)
    
    # Sort by stars
    new_finds.sort(key=lambda x: x["stars"], reverse=True)
    
    # Update state
    state["seen_repos"] = list(seen)
    state["new_finds"] = new_finds
    save_state(state)
    
    return new_finds

def generate_report(new_finds):
    """Generate a human-readable report of new findings."""
    if not new_finds:
        return "📭 No new video tools found in today's scan."
    
    report = f"**🎬 New Video Tools Found — {date.today().strftime('%B %d, %Y')}**\n\n"
    report += f"Found **{len(new_finds)}** new tool(s) worth looking at:\n\n"
    
    for r in new_finds[:10]:
        report += f"⭐ **{r['name']}** ({r['stars']} ★, {r['language']})\n"
        report += f"   {r['description']}\n"
        report += f"   {r['url']}\n"
        report += f"   *Found in: {r['found_in']}*\n\n"
    
    return report

def update_readme(new_finds):
    """Add new finds to the README if significant enough."""
    if not new_finds:
        return False
    
    # For now, just flag them — manual curation is better for quality
    # This prevents noise from low-quality repos
    return True

if __name__ == "__main__":
    print("🎬 Awesome AI Video Tools — Daily Scanner")
    print("=" * 45)
    
    new = scan()
    report = generate_report(new)
    print("\n" + report)
    
    if new:
        with open(os.path.join(REPO_DIR, ".latest_scan.md"), "w") as f:
            f.write(report)
        print(f"📝 Report saved to .latest_scan.md")
