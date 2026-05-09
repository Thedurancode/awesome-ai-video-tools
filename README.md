<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=Awesome%20AI%20Video%20Tools&fontSize=50&fontAlignY=35&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <b>60 open-source repos + 28 production APIs</b><br>
  <i>For AI agents that need to create, edit, understand, transcribe, stream, or analyze video</i>
</p>

<p align="center">
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools/stargazers"><img src="https://img.shields.io/github/stars/Thedurancode/awesome-ai-video-tools?style=flat&logo=github&color=yellow"/></a>
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools"><img src="https://img.shields.io/badge/tools-88_total-blue"/></a>
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools"><img src="https://img.shields.io/badge/APIs-28_ready-green"/></a>
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-purple"/></a>
</p>

---

## 🎬 Why This Exists

> *Created by **Ed Duran** — a developer who's been coding for over 20 years, but spent 15 of those years in the film industry.*

Most video tools on GitHub are built by developers for developers. They're powerful but assume you already know the pipeline — how to chain ffmpeg with transcription, when to reach for an API vs a CLI tool, which model actually works for your use case.

This list is different. It's built by someone who's **been on both sides of the camera** — writing code for two decades while simultaneously producing, editing, and directing video content. Every tool here was evaluated through the lens of: *"Would an AI agent actually use this in a real pipeline?"*

The result: **60 hand-picked open-source repos + 28 production APIs**, organized by what they actually do, with real endpoints, real pricing, and real code patterns an agent can copy-paste.

---

## 📊 At a Glance

| Category | Count | Top Pick | Stars |
|----------|-------|----------|------|
| 🎨 **AI Video Generation** | 13 | stable-diffusion-webui | ⭐163k |
| ✂️ **Video Editing** | 10 | lossless-cut | ⭐40k |
| 🔊 **Audio & Subtitle Tools** | 8 | whisper | ⭐99k |
| 🧠 **Video Understanding** | 9 | opencv | ⭐87k |
| 📡 **Streaming & Servers** | 5 | SRS | ⭐29k |
| 🔄 **Transcoding** | 4 | FFmpeg | ⭐60k |
| 🎭 **Face & Restoration** | 4 | faceswap | ⭐55k |
| 🤖 **AI Agent Tools** | 7 | remotion | ⭐46k |

**Total: 88 tools** combining for **~1.2 million GitHub stars** worth of community validation.

---

## Table of Contents

- [🎨 AI Video Generation](#-ai-video-generation)
- [✂️ Video Editing (CLI & Programmatic)](#️-video-editing-cli--programmatic)
- [🔊 Audio & Subtitle Tools](#-audio--subtitle-tools)
- [📡 Video Streaming & Servers](#-video-streaming--servers)
- [🔄 Transcoding](#-transcoding)
- [🧠 Video Understanding & Analysis](#-video-understanding--analysis)
- [🎭 Face & Video Restoration](#-face--video-restoration)
- [🤖 AI Agent Video Tools](#-ai-agent-video-tools)
- [🌐 Production APIs](#-production-apis--agent-ready-reference)
- [💰 Cost Comparison](#-cost-comparison)
- [🏆 Top 10 for AI Agents](#-top-10-for-ai-agents)
- [🔧 How to Use This](#-how-to-use-this)

---

# 🎨 AI Video Generation

Tools that generate video from text, images, or other inputs using AI. **The fastest-moving category in tech right now.**

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | ⭐163k | Python | The gold standard — image & video gen UI |
| 2 | [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | ⭐65k | Python | Node-based UI for SD + video workflows |
| 3 | [huggingface/diffusers](https://github.com/huggingface/diffusers) | ⭐34k | Python | State-of-the-art diffusion models |
| 4 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | ⭐12k | JS | 200+ models (Flux, Kling, Sora, Veo) |
| 5 | [facebookresearch/DiT](https://github.com/facebookresearch/DiT) | ⭐8.6k | Python | Scalable Diffusion Transformers |
| 6 | [open-mmlab/mmagic](https://github.com/open-mmlab/mmagic) | ⭐7.4k | Python | Multimodal generation toolbox |
| 7 | [showlab/Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) | ⭐5.6k | - | Curated list of video diffusion models |
| 8 | [showlab/Tune-A-Video](https://github.com/showlab/Tune-A-Video) | ⭐4.4k | Python | One-shot text-to-video |
| 9 | [Picsart-AI-Research/Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) | ⭐4.2k | Python | Zero-shot text-to-video |
| 10 | [ali-vilab/VGen](https://github.com/ali-vilab/VGen) | ⭐3.2k | Python | Holistic video gen ecosystem |
| 11 | [google-research/frame-interpolation](https://github.com/google-research/frame-interpolation) | ⭐3.1k | Python | FILM: smooth slow-motion |
| 12 | [williamyang1991/Rerender_A_Video](https://github.com/williamyang1991/Rerender_A_Video) | ⭐3.0k | Python | Text-guided video-to-video |
| 13 | [showlab/MotionDirector](https://github.com/showlab/MotionDirector) | ⭐1.0k | Python | Motion customization |
| 14 | [PKU-YuanGroup/ConsisID](https://github.com/PKU-YuanGroup/ConsisID) | ⭐839 | Python | Identity-preserving video gen |

---

# ✂️ Video Editing (CLI & Programmatic)

Tools for programmatic video editing — perfect for AI agents to manipulate clips without a GUI.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) | ⭐40k | TypeScript | Lossless trim — instant, no re-encode |
| 2 | [Zulko/moviepy](https://github.com/Zulko/moviepy) | ⭐15k | Python | Programmatic video editing in Python |
| 3 | [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python) | ⭐11k | Python | Python bindings for FFmpeg |
| 4 | [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) | ⭐5.7k | Python | Full open-source video editor |
| 5 | [mifi/editly](https://github.com/mifi/editly) | ⭐5.4k | TypeScript | Declarative CLI video editing |
| 6 | [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | ⭐4.8k | Python | Scene cut/transition detection |
| 7 | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | ⭐4.3k | Nim | Auto-detect and remove silence |
| 8 | [jeanslack/Videomass](https://github.com/jeanslack/Videomass) | ⭐1.6k | Python | Cross-platform FFmpeg GUI |
| 9 | [OpenShot/libopenshot](https://github.com/OpenShot/libopenshot) | ⭐1.5k | C++ | Video editing library |
| 10 | [mohyware/clip-js](https://github.com/mohyware/clip-js) | ⭐738 | TypeScript | Online editor (Remotion + FFmpeg) |

---

# 🔊 Audio & Subtitle Tools

Transcription, captioning, subtitles — essential for any video content pipeline.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [openai/whisper](https://github.com/openai/whisper) | ⭐99k | Python | State-of-the-art speech-to-text |
| 2 | [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) | ⭐17k | Python | Netflix-level subtitle + dubbing |
| 3 | [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) | ⭐14k | Python | LLM-powered subtitle gen |
| 4 | [YaoFANGUK/video-subtitle-remover](https://github.com/YaoFANGUK/video-subtitle-remover) | ⭐11k | Python | AI subtitle & watermark removal |
| 5 | [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) | ⭐9.9k | Python | Speaker diarization |
| 6 | [YaoFANGUK/video-subtitle-extractor](https://github.com/YaoFANGUK/video-subtitle-extractor) | ⭐8.8k | Python | OCR subtitle extraction to SRT |
| 7 | [smacke/ffsubsync](https://github.com/smacke/ffsubsync) | ⭐7.7k | Python | Auto-sync subtitles to video |
| 8 | [m1guelpf/auto-subtitle](https://github.com/m1guelpf/auto-subtitle) | ⭐2.2k | Python | Auto-generate + burn subtitles |

---

# 📡 Video Streaming & Servers

Stream, serve, and rebroadcast video at scale.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [ossrs/srs](https://github.com/ossrs/srs) | ⭐29k | C++ | Real-time media server |
| 2 | [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | ⭐19k | Go | SRT/WebRTC/RTSP/RTMP/HLS |
| 3 | [gwuhaolin/livego](https://github.com/gwuhaolin/livego) | ⭐10k | Go | Lightweight live streaming |
| 4 | [datarhei/restreamer](https://github.com/datarhei/restreamer) | ⭐5.0k | HTML | Self-hosted streaming |
| 5 | [mediacms-io/mediacms](https://github.com/mediacms-io/mediacms) | ⭐4.9k | JS | Open source video CMS |

---

# 🔄 Transcoding

Convert, compress, and optimize video for any format.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | ⭐60k | C | The universal video toolkit |
| 2 | [handbrake/handbrake](https://github.com/handbrake/handbrake) | ⭐23k | C | Gold standard transcoding |
| 3 | [HaveAGitGat/Tdarr](https://github.com/HaveAGitGat/Tdarr) | ⭐4.1k | Makefile | Distributed transcode automation |
| 4 | [gpac/gpac](https://github.com/gpac/gpac) | ⭐3.2k | C | Multimedia framework |

---

# 🧠 Video Understanding & Analysis

AI-powered video analysis, object detection, scene understanding.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [opencv/opencv](https://github.com/opencv/opencv) | ⭐87k | C++ | Computer vision Swiss Army knife |
| 2 | [open-mmlab/mmtracking](https://github.com/open-mmlab/mmtracking) | ⭐3.9k | Python | Video object detection & tracking |
| 3 | [OpenGVLab/InternVideo](https://github.com/OpenGVLab/InternVideo) | ⭐2.3k | Python | Video foundation model |
| 4 | [facebookresearch/TimeSformer](https://github.com/facebookresearch/TimeSformer) | ⭐1.9k | Python | Space-time video attention |
| 5 | [DAMO-NLP-SG/VideoLLaMA3](https://github.com/DAMO-NLP-SG/VideoLLaMA3) | ⭐1.2k | Python | Multimodal video understanding |
| 6 | [unum-cloud/UForm](https://github.com/unum-cloud/UForm) | ⭐1.2k | Python | Pocket-sized multimodal AI |
| 7 | [videoflow/videoflow](https://github.com/videoflow/videoflow) | ⭐1.0k | Python | Video analysis pipelines |
| 8 | [scanner-research/scanner](https://github.com/scanner-research/scanner) | ⭐624 | C++ | Efficient video analysis at scale |
| 9 | [microsoft/VideoX](https://github.com/microsoft/VideoX) | ⭐1.1k | Python | Video cross-modal models |

---

# 🎭 Face & Video Restoration

Face swap, restoration, upscaling, enhancement.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [deepfakes/faceswap](https://github.com/deepfakes/faceswap) | ⭐55k | Python | Face swap for video |
| 2 | [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | ⭐37k | Python | Face restoration |
| 3 | [Xinntao/Real-ESRGAN](https://github.com/Xinntao/Real-ESRGAN) | ⭐35k | Python | Video upscaling & restoration |
| 4 | [nagadomi/waifu2x](https://github.com/nagadomi/waifu2x) | ⭐28k | Lua | Anime super-resolution |

---

# 🤖 AI Agent Video Tools

Specialized tools designed for AI agents to create, schedule, and publish video content autonomously.

| # | Repo | Stars | Lang | What It Does |
|---|------|-------|------|-------------|
| 1 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | ⭐46k | TypeScript | **Make videos programmatically with React** |
| 2 | [YILS-LIN/short-video-factory](https://github.com/YILS-LIN/short-video-factory) | ⭐3.9k | TypeScript | One-click short video generation |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | ⭐3.6k | Python | Agentic video production (500+ skills) |
| 4 | [SamurAIGPT/AI-Youtube-Shorts-Generator](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator) | ⭐3.5k | Python | Opus Clip alternative — long→shorts |
| 5 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | ⭐3.2k | Python | End-to-end AI short drama production |
| 6 | [HA6Bots/TikTok-Compilation-Video-Generator](https://github.com/HA6Bots/TikTok-Compilation-Video-Generator) | ⭐931 | Python | Auto clip collection + compilations |
| 7 | [NisaarAgharia/AI-Shorts-Creator](https://github.com/NisaarAgharia/AI-Shorts-Creator) | ⭐757 | Python | AI auto-crop + highlight extraction |

---

# 🌐 Production APIs — Agent-Ready Reference

The actual APIs an AI agent can call right now to generate, edit, transcribe, host, and analyze video. **Includes endpoints, auth, and copy-paste Python code.**

### 🎬 Video Generation APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **Runway** | `api.runwayml.ai/v1/text_to_video` | API Key | Free / $12-$76/mo | Cinematic gen |
| 2 | **Pika** | `api.pika.art/v1/generate` | API Key | Free 80cr / $8-$76/mo | Social clips |
| 3 | **Kling** | Via `fal.ai` or direct API | API Key | ~$0.07/s | Best motion |
| 4 | **Google Veo** | Vertex AI | OAuth | $0.40/s via fal.ai | Google ecosystem |
| 5 | **Genmo Mochi** | `api.genmo.ai/v1/generate` | API Key | Free (Apache 2.0) | Self-hostable |
| 6 | **Wan 2.5** | Via `fal.ai` | API Key | $0.05/s | Cheapest quality |
| 7 | **Hailuo/Ovi** | Via `fal.ai` | API Key | $0.20/video | Short clips |
| 8 | **InVideo** | `api.invideo.io/v1` | API Key | Free / ~$20/mo | Long-form |
| 9 | **Sora** | ❌ No public API | ChatGPT only | ChatGPT $20/mo | Cinematic |

```python
# Generate B-roll for any video
response = requests.post(
    "https://api.runwayml.ai/v1/text_to_video",
    headers={"Authorization": f"Bearer {RUNWAY_KEY}"},
    json={"prompt": "Drone shot of a lake at sunset", "duration": 5}
)
```

### 🗣️ Avatar & Talking Head APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **HeyGen** | `api.heygen.com/v2/video/generate` | API Key | Free 3/mo / $29-$99/mo | Avatar presenters |
| 2 | **Synthesia** | `api.synthesia.io/v2/videos` | API Key | Free 1,200cr / $14-$59/mo | Enterprise avatars |
| 3 | **ElevenLabs** | `api.elevenlabs.io/v1` | API Key | Free 10kcr / $6-$99/mo | Voiceover + dubbing |

```python
# Create an AI avatar presenter
response = requests.post(
    "https://api.heygen.com/v2/video/generate",
    headers={"X-Api-Key": HEYGEN_KEY},
    json={
        "avatar": {"avatar_id": "Oliver-avatar"},
        "script": {"text": "Welcome to our marketplace!"},
        "background": {"color": "#1a1a2e"}
    }
)
```

### ✂️ Video Editing & Processing APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **Shotstack** | `api.shotstack.io/v1/render` | API Key | $0.20-$0.30/credit | Programmatic editing |
| 2 | **Mux** | `api.mux.com/video/v1` | API Key+Token | Free / ~$0.003/min | Hosting & streaming |
| 3 | **api.video** | `ws.api.video/v1` | API Key | Free encoding, pay storage | Cost-effective |
| 4 | **Kapwing** | `api.kapwing.com/v1` | API Key | Free tier | Online editing |

```python
# Assemble a video programmatically
response = requests.post(
    "https://api.shotstack.io/v1/render",
    headers={"x-api-key": SHOTSTACK_KEY},
    json={"timeline": {"tracks": [{"clips": [{
        "asset": {"type": "video", "src": video_url},
        "start": 0, "length": 10
    }]}]}}
)
```

### 🎙️ Transcription & Audio Intelligence APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **Deepgram** | `api.deepgram.com/v1/listen` | API Key | Free $200cr / $0.0048/min | Real-time, Nova-3 |
| 2 | **AssemblyAI** | `api.assemblyai.com/v2` | API Key | Free $50cr / $0.21/hr | Multilingual accuracy |
| 3 | **Gladia** | `api.gladia.io/v2` | API Key | 10h free/mo / $0.61/hr | Budget option |
| 4 | **Rev.ai** | `api.rev.ai/speechtotext/v1` | API Key | $0.014/min | Enterprise |

```python
# Transcribe any video
response = requests.post(
    "https://api.deepgram.com/v1/listen",
    headers={"Authorization": f"Token {DEEPGRAM_KEY}"},
    json={"url": video_url},
    params={"model": "nova-3", "smart_format": "true"}
)
transcript = response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
```

### 🖼️ Video Understanding & Analysis APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **Google VI** | `videointelligence.googleapis.com/v1` | OAuth | $0.10/min | Label detection |
| 2 | **AWS Rekognition** | `rekognition.amazonaws.com` | IAM | $0.10/min | Face detection |
| 3 | **Azure Video Indexer** | `api.videoindexer.ai` | API Key | Free 10h / $0.06/min | Deep analysis |

### 🚀 Inference Platforms (Run Multiple Models)

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 1 | **fal.ai** | `api.fal.ai/v1` | API Key | $1.89/hr H100 | Run Kling, Veo, Wan |
| 2 | **Replicate** | `api.replicate.com/v1` | API Key | Pay per prediction | Open-source models |
| 3 | **Hugging Face** | Inference API | API Key | Free tier / GPU paid | Community models |

---

# 💰 Cost Comparison

**Per minute of output across the most popular APIs:**

| API | Cost/min | Notes |
|-----|----------|-------|
| **Wan 2.5** | $3.00 | Cheapest quality gen |
| **Kling 2.5** | $4.20 | via fal.ai |
| **Veo 3** | $24.00 | via fal.ai |
| **Runway Gen-3** | ~$1.00 * | Subscription, unlimited * |
| **Deepgram** | $0.0048 | Cheapest transcription |
| **Mux** | $0.0032 | Hosting + delivery |
| **Shotstack** | ~$0.30 | Rendering |

*Runway is subscription-based, not per-minute. $12/mo for 125 credits = ~$0.10/video.*

---

# 🏆 Top 10 for AI Agents

If you're building an AI agent that needs to handle video, **start here:**

| Priority | Tool | Why |
|----------|------|-----|
| 🥇 | **remotion-dev/remotion** | Programmatic video with React — most agent-friendly |
| 🥇 | **Zulko/moviepy** | Python-native — easy for agents to script |
| 🥇 | **openai/whisper** | Best-in-class transcription |
| 🥈 | **mifi/lossless-cut** | Instant cutting, no re-encode |
| 🥈 | **kkroening/ffmpeg-python** | FFmpeg wrapper for Python agents |
| 🥈 | **WyattBlue/auto-editor** | Auto-remove silence from raw footage |
| 🥉 | **Breakthrough/PySceneDetect** | Scene detection for intelligent clipping |
| 🥉 | **mifi/editly** | Declarative video assembly |
| 🥉 | **SamurAIGPT/AI-Youtube-Shorts-Generator** | Long content → shorts |
| 🥉 | **smacke/ffsubsync** | Auto-sync subtitles |

---

# 🔧 How to Use This

### For AI Agents

Most tools chain together naturally. Example pipelines:

**Content repurposing agent:**
```
Long video → whisper (transcribe) → auto-editor (remove silence) → 
lossless-cut (trim highlights) → moviepy (add text/branding) → 
ffmpeg (encode for TikTok/Reels)
```

**Video production agent:**
```
Script → HeyGen (generate avatar) → Runway (generate B-roll) → 
Shotstack (assemble) → Deepgram (add captions) → Mux (host & deliver)
```

**Video analysis agent:**
```
Video → Google VI (label scenes) → whisper (transcribe) → 
pyannote (speaker diarization) → ffsubsync (align subtitles) → 
VideoLingo (translate if needed)
```

### For Developers

Each tool is production-ready with active maintenance. Filter by language (Python-heavy), stars (community-validated), and license (mostly MIT/Apache 2.0).

---

<p align="center">
  <b>Created by Ed Duran</b><br>
  <i>A developer who's been coding for over 20 years, but also spent 15 years in the film industry.</i><br><br>
  <a href="https://github.com/Thedurancode">GitHub</a> •
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools">Repo</a> •
  <a href="https://github.com/Thedurancode/awesome-ai-video-tools/issues">Suggest a Tool</a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%"/>
</p>
