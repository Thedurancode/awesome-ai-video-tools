# Awesome AI Video Tools 🎬

> A curated list of the **best video-related tools for AI agents** on GitHub — sorted by stars, categorized by use case.

**50 hand-picked repos** for AI agents that need to create, edit, understand, transcribe, stream, or analyze video.

---

## 📊 Quick Stats

| Category | Count | Top Tool |
|----------|-------|----------|
| 🎨 AI Video Generation | 10 | AUTOMATIC1111/stable-diffusion-webui ⭐163k |
| ✂️ Video Editing | 9 | mifi/lossless-cut ⭐40k |
| 🔊 Audio/Subtitle Tools | 6 | openai/whisper ⭐99k |
| 📡 Video Streaming & Servers | 5 | ossrs/srs ⭐29k |
| 🔄 Transcoding | 4 | handbrake/handbrake ⭐23k |
| 🧠 Video Understanding | 6 | opencv/opencv ⭐87k |
| 🎭 Face & Restoration | 4 | deepfakes/faceswap ⭐55k |
| 🤖 AI Agent Video Tools | 6 | remotion-dev/remotion ⭐46k |

---

## 1. 🎨 AI Video Generation

Tools that generate video from text, images, or other inputs using AI.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 1 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | ⭐163k | Python | The gold standard for stable diffusion — image & video gen UI |
| 2 | [huggingface/diffusers](https://github.com/huggingface/diffusers) | ⭐34k | Python | State-of-the-art diffusion models for image, video, audio |
| 3 | [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | ⭐65k | Python | Powerful node-based UI for stable diffusion + video workflows |
| 4 | [showlab/Tune-A-Video](https://github.com/showlab/Tune-A-Video) | ⭐4.4k | Python | One-shot text-to-video generation from image models |
| 5 | [Picsart-AI-Research/Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) | ⭐4.2k | Python | Zero-shot text-to-video using existing diffusion models |
| 6 | [ali-vilab/VGen](https://github.com/ali-vilab/VGen) | ⭐3.2k | Python | Holistic video generation ecosystem with diffusion models |
| 7 | [google-research/frame-interpolation](https://github.com/google-research/frame-interpolation) | ⭐3.1k | Python | FILM: Frame interpolation for smooth slow-motion |
| 8 | [showlab/Show-1](https://github.com/showlab/Show-1) | ⭐1.1k | Python | Marrying pixel and latent diffusion for text-to-video |
| 9 | [williamyang1991/Rerender_A_Video](https://github.com/williamyang1991/Rerender_A_Video) | ⭐3.0k | Python | Zero-shot text-guided video-to-video translation |
| 10 | [showlab/MotionDirector](https://github.com/showlab/MotionDirector) | ⭐1.0k | Python | Motion customization of text-to-video models |
| 11 | [facebookresearch/DiT](https://github.com/facebookresearch/DiT) | ⭐8.6k | Python | Scalable Diffusion Models with Transformers |
| 12 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | ⭐12k | JS | 200+ models (Flux, Kling, Sora, Veo) in one platform |
| 13 | [PKU-YuanGroup/ConsisID](https://github.com/PKU-YuanGroup/ConsisID) | ⭐839 | Python | Identity-preserving text-to-video generation |

## 2. ✂️ Video Editing (CLI & Programmatic)

Tools for programmatic video editing — perfect for AI agents to manipulate clips.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 14 | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) | ⭐40k | TypeScript | Lossless trim/cut — instant, no re-encode |
| 15 | [Zulko/moviepy](https://github.com/Zulko/moviepy) | ⭐15k | Python | Programmatic video editing in Python (our stack) |
| 16 | [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python) | ⭐11k | Python | Python bindings for FFmpeg with complex filter support |
| 17 | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | ⭐4.3k | Nim | Auto-detect and remove silence/dead air |
| 18 | [mifi/editly](https://github.com/mifi/editly) | ⭐5.4k | TypeScript | Declarative CLI video editing + API — splice, effects, text |
| 19 | [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) | ⭐5.7k | Python | Full open-source video editor with Python API |
| 20 | [OpenShot/libopenshot](https://github.com/OpenShot/libopenshot) | ⭐1.5k | C++ | Video editing library with Python bindings |
| 21 | [jeanslack/Videomass](https://github.com/jeanslack/Videomass) | ⭐1.6k | Python | Cross-platform FFmpeg GUI with batch processing |
| 22 | [mohyware/clip-js](https://github.com/mohyware/clip-js) | ⭐738 | TypeScript | Online video editor built with Remotion + FFmpeg |
| 23 | [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | ⭐4.8k | Python | Scene cut/transition detection library |

## 3. 🔊 Audio & Subtitle Tools

Transcription, captioning, subtitles — essential for video content pipelines.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 24 | [openai/whisper](https://github.com/openai/whisper) | ⭐99k | Python | State-of-the-art speech-to-text / video transcription |
| 25 | [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) | ⭐17k | Python | Netflix-level subtitle cutting, translation, AI dubbing |
| 26 | [WEIFENG2333/VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner) | ⭐14k | Python | LLM-powered subtitle gen, segmentation, correction |
| 27 | [YaoFANGUK/video-subtitle-remover](https://github.com/YaoFANGUK/video-subtitle-remover) | ⭐11k | Python | AI removal of hard-coded subtitles & watermarks |
| 28 | [YaoFANGUK/video-subtitle-extractor](https://github.com/YaoFANGUK/video-subtitle-extractor) | ⭐8.8k | Python | OCR-based hard subtitle extraction to SRT |
| 29 | [smacke/ffsubsync](https://github.com/smacke/ffsubsync) | ⭐7.7k | Python | Auto-sync subtitles to video (no more out-of-sync) |
| 30 | [m1guelpf/auto-subtitle](https://github.com/m1guelpf/auto-subtitle) | ⭐2.2k | Python | Auto-generate and burn subtitles for any video |
| 31 | [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) | ⭐9.9k | Python | Speaker diarization — who spoke when |

## 4. 📡 Video Streaming & Servers

Stream, serve, and rebroadcast video at scale.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 32 | [ossrs/srs](https://github.com/ossrs/srs) | ⭐29k | C++ | High-performance real-time media server (RTMP, WebRTC, HLS) |
| 33 | [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | ⭐19k | Go | Ready-to-use SRT/WebRTC/RTSP/RTMP/HLS media server |
| 34 | [gwuhaolin/livego](https://github.com/gwuhaolin/livego) | ⭐10k | Go | Lightweight live streaming server in Go |
| 35 | [datarhei/restreamer](https://github.com/datarhei/restreamer) | ⭐5.0k | HTML | Complete self-hosted streaming server |
| 36 | [mediacms-io/mediacms](https://github.com/mediacms-io/mediacms) | ⭐4.9k | JS | Open source video CMS with REST API |

## 5. 🔄 Transcoding

Convert, compress, and optimize video for any format.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 37 | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | ⭐60k | C | The universal video toolkit — everything wraps this |
| 38 | [handbrake/handbrake](https://github.com/handbrake/handbrake) | ⭐23k | C | The gold standard for video transcoding |
| 39 | [HaveAGitGat/Tdarr](https://github.com/HaveAGitGat/Tdarr) | ⭐4.1k | Makefile | Distributed transcode automation with FFmpeg/HandBrake |
| 40 | [gpac/gpac](https://github.com/gpac/gpac) | ⭐3.2k | C | Multimedia framework for streaming and transcoding |

## 6. 🧠 Video Understanding & Analysis

AI-powered video analysis, object detection, scene understanding.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 41 | [opencv/opencv](https://github.com/opencv/opencv) | ⭐87k | C++ | The Swiss Army knife of computer vision |
| 42 | [open-mmlab/mmagic](https://github.com/open-mmlab/mmagic) | ⭐7.4k | Python | Multimodal generation & restoration toolbox |
| 43 | [open-mmlab/mmtracking](https://github.com/open-mmlab/mmtracking) | ⭐3.9k | Python | Video object detection, MOT, SOT, VIS |
| 44 | [OpenGVLab/InternVideo](https://github.com/OpenGVLab/InternVideo) | ⭐2.3k | Python | Video foundation model for multimodal understanding |
| 45 | [DAMO-NLP-SG/VideoLLaMA3](https://github.com/DAMO-NLP-SG/VideoLLaMA3) | ⭐1.2k | Python | Frontier multimodal video understanding model |
| 46 | [videoflow/videoflow](https://github.com/videoflow/videoflow) | ⭐1.0k | Python | Framework for complex video analysis pipelines |
| 47 | [facebookresearch/TimeSformer](https://github.com/facebookresearch/TimeSformer) | ⭐1.9k | Python | Space-time attention for video understanding |
| 48 | [unum-cloud/UForm](https://github.com/unum-cloud/UForm) | ⭐1.2k | Python | Pocket-sized multimodal AI for video understanding |
| 49 | [scanner-research/scanner](https://github.com/scanner-research/scanner) | ⭐624 | C++ | Efficient video analysis at scale |

## 7. 🎭 Face & Video Restoration

Face swap, restoration, upscaling, enhancement.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 50 | [deepfakes/faceswap](https://github.com/deepfakes/faceswap) | ⭐55k | Python | Deepfakes face swap for video |
| 51 | [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | ⭐37k | Python | Practical face restoration for video |
| 52 | [Xinntao/Real-ESRGAN](https://github.com/Xinntao/Real-ESRGAN) | ⭐35k | Python | General image/video upscaling and restoration |
| 53 | [nagadomi/waifu2x](https://github.com/nagadomi/waifu2x) | ⭐28k | Lua | Image super-resolution for anime-style video |

## 8. 🤖 AI Agent Video Tools

Specialized tools for AI agents to create, schedule, and publish video content.

| # | Repo | Stars | Language | What It Does |
|---|------|-------|----------|-------------|
| 54 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | ⭐46k | TypeScript | **Make videos programmatically with React** — perfect for AI agents |
| 55 | [SamurAIGPT/AI-Youtube-Shorts-Generator](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator) | ⭐3.5k | Python | Open-source Opus Clip alternative — auto clip long videos to shorts |
| 56 | [YILS-LIN/short-video-factory](https://github.com/YILS-LIN/short-video-factory) | ⭐3.9k | TypeScript | One-click product marketing short video generation |
| 57 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | ⭐3.2k | Python | End-to-end AI short drama production workspace |
| 58 | [HA6Bots/TikTok-Compilation-Video-Generator](https://github.com/HA6Bots/TikTok-Compilation-Video-Generator) | ⭐931 | Python | Bot system that auto-collects clips and makes compilations |
| 59 | [NisaarAgharia/AI-Shorts-Creator](https://github.com/NisaarAgharia/AI-Shorts-Creator) | ⭐757 | Python | AI auto-crop + highlight extraction with GPT-4 |
| 60 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | ⭐3.6k | Python | Open-source agentic video production with 500+ agent skills |

---

## 🏆 Top 10 for AI Agents

If you're building an AI agent that needs to handle video, start here:

| Priority | Tool | Why |
|----------|------|-----|
| 🥇 | **remotion-dev/remotion** | Programmatic video creation with React — most agent-friendly |
| 🥇 | **Zulko/moviepy** | Python-native video editing — easy for agents to script |
| 🥇 | **openai/whisper** | Best-in-class transcription for any video |
| 🥈 | **mifi/lossless-cut** | Instant cutting without re-encoding |
| 🥈 | **kkroening/ffmpeg-python** | FFmpeg wrapper for Python agents |
| 🥈 | **WyattBlue/auto-editor** | Auto-remove silence — perfect for raw footage |
| 🥉 | **Breakthrough/PySceneDetect** | Scene detection for intelligent clipping |
| 🥉 | **mifi/editly** | Declarative video assembly — good for batch |
| 🥉 | **SamurAIGPT/AI-Youtube-Shorts-Generator** | Turn long content into shorts |
| 🥉 | **smacke/ffsubsync** | Auto-sync subtitles, great for pipeline automation |

---

## 🔧 How to Use This As an AI Agent

Most of these tools work beautifully together. Example pipeline:

```
Raw video → whisper (transcribe) → auto-editor (remove silence) → 
lossless-cut (trim) → moviepy (add text/effects) → ffmpeg (encode)
```

Or for content creation:

```
Long video → SamurAIGPT (clip highlights) → remotion (add branding) →
ffmpeg-python (batch resize for TikTok/Reels)
```

---

## 📡 Top 20 AI Video APIs — Agent-Ready Reference

The actual APIs an AI agent can call right now to generate, edit, transcribe, host, and analyze video. Includes pricing, endpoints, and agent usage patterns.

### 🎬 Video Generation APIs

| # | API | Endpoint | Auth | Pricing (Agent-Friendly) | Best For |
|---|-----|----------|------|--------------------------|----------|
| 1 | **Runway** | `api.runwayml.ai/v1/text_to_video` | API Key | Free tier, Standard $12/mo, Pro $28/mo | Cinematic text/video generation |
| 2 | **Pika** | `api.pika.art/v1/generate` | API Key | Free 80cr/mo, $8-$76/mo | Quick social clips, Pikascenes |
| 3 | **Kling AI** | `api.klingai.com/v1/videos` | API Key | ~$0.07/s via fal.ai | Best motion quality, physics |
| 4 | **Google Veo** | `us-central1-aiplatform.googleapis.com/v1/projects/...` | OAuth/Vertex AI | $0.40/s via fal.ai | Google Cloud ecosystem |
| 5 | **Genmo** | `api.genmo.ai/v1/generate` | API Key | Free (open source) | Self-hostable, Apache 2.0 |
| 6 | **Wan 2.5** (Alibaba) | Via `fal.ai` or Alibaba API | API Key | $0.05/s | Cheapest quality gen |
| 7 | **Hailuo / Ovi** | Via `fal.ai` | API Key | $0.20/video | Cost-effective short clips |
| 8 | **Seedance** (ByteDance) | API rolling out via ByteDance | API Key | TBD | TikTok editing patterns |
| 9 | **InVideo AI** | `api.invideo.io/v1` | API Key | Free tier, ~$20/mo | Long-form (30min) videos |
| 10 | **Sora** (OpenAI) | ❌ No public API yet | ChatGPT only | ChatGPT Plus $20/mo | Cinematic quality |

**Agent Pattern:**
```python
# Generate B-roll for a talking head video
response = requests.post(
    "https://api.runwayml.ai/v1/text_to_video",
    headers={"Authorization": f"Bearer {RUNWAY_KEY}"},
    json={"prompt": "Drone shot of a lake at sunset", "duration": 5}
)
```

### 🗣️ Avatar & Talking Head APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 11 | **HeyGen** | `api.heygen.com/v2/video/generate` | API Key | Free 3/mo, $29-$99/mo | Avatar presenters, digital twins |
| 12 | **Synthesia** | `api.synthesia.io/v2/videos` | API Key | Free 1,200cr, $14-$59/mo | Enterprise avatar videos |
| 13 | **ElevenLabs** | `api.elevenlabs.io/v1` | API Key | Free 10kcr, $6-$99/mo | Voiceover + lip-sync dubbing |

**Agent Pattern:**
```python
# Create an AI avatar video
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
| 14 | **Shotstack** | `api.shotstack.io/v1/render` | API Key | $0.20-$0.30/credit | Programmatic video assembly |
| 15 | **Mux** | `api.mux.com/video/v1` | API Key + Token | Free tier, ~$0.003/min | Video hosting & streaming |
| 16 | **api.video** | `ws.api.video/v1` | API Key | Free encoding, pay storage | Cost-effective hosting |
| 17 | **Descript** | ❌ No public API | Desktop app only | $16-$50/mo | Text-based editing UI |
| 18 | **Kapwing** | `api.kapwing.com/v1` | API Key | Free tier, paid for more | Online editing + API |

**Agent Pattern:**
```python
# Programmatically assemble a video with Shotstack
response = requests.post(
    "https://api.shotstack.io/v1/render",
    headers={"x-api-key": SHOTSTACK_KEY},
    json={
        "timeline": {
            "tracks": [{
                "clips": [{
                    "asset": {"type": "video", "src": video_url},
                    "start": 0, "length": 10,
                    "transition": {"type": "fade"}
                }]
            }]
        }
    }
)
```

### 🎙️ Transcription & Audio Intelligence APIs

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 19 | **Deepgram** | `api.deepgram.com/v1/listen` | API Key | Free $200cr, $0.0048/min | Real-time STT, Nova-3 model |
| 20 | **AssemblyAI** | `api.assemblyai.com/v2` | API Key | Free $50cr, $0.21/hr | Accurate multilingual STT |
| 21 | **Gladia** | `api.gladia.io/v2` | API Key | 10h free/mo, $0.61/hr | Budget competitor |
| 22 | **Rev.ai** | `api.rev.ai/speechtotext/v1` | API Key | $0.014/min | Enterprise STT |

**Agent Pattern:**
```python
# Transcribe a video file
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
| 23 | **Google Video Intelligence** | `videointelligence.googleapis.com/v1` | OAuth | $0.10/min | Label detection, shot change |
| 24 | **AWS Rekognition Video** | `rekognition.amazonaws.com` | IAM | $0.10/min | Face detection, celebrity recognition |
| 25 | **Azure Video Indexer** | `api.videoindexer.ai` | API Key | Free 10h, $0.06/min | Deep video analysis |

### 🚀 Inference Platforms (Runs Multiple Models)

| # | API | Endpoint | Auth | Pricing | Best For |
|---|-----|----------|------|---------|----------|
| 26 | **fal.ai** | `api.fal.ai/v1` | API Key | $1.89/hr H100 GPU | Run Kling, Veo, Wan, Ovi |
| 27 | **Replicate** | `api.replicate.com/v1` | API Key | Pay per prediction | Run open-source video models |
| 28 | **Hugging Face** | `api-inference.huggingface.co/models/...` | API Key | Free tier, paid for GPU | Community video models |

### 💡 Agent Usage Patterns

**Cold call lead generation (our aqua-rent setup):**
```
Lead data → HeyGen API (generate avatar intro) → Mux (host) → 
custom script → send to prospect
```

**Content repurposing agent:**
```
Long video → Deepgram (transcribe & chapters) → AssemblyAI (summarize) → 
Runway/Pika (generate B-roll) → Shotstack (assemble cuts) → Mux (deliver to social)
```

**Property video agent:**
```
Walkthrough video → Google VI (label rooms/objects) → 
Shotstack (add text overlays) → api.video (host for listing)
```

### 💰 Cost Comparison (Per Minute of Output)

| API | Cost/min | Notes |
|-----|----------|-------|
| Wan 2.5 | $3.00 | via fal.ai, cheapest gen |
| Kling 2.5 | $4.20 | via fal.ai |
| Veo 3 | $24.00 | via fal.ai |
| Runway Gen-3 | ~$1.00 | Subscription, unlimited |
| Deepgram | $0.0048 | Cheapest transcription |
| Mux | $0.0032 | Hosting + delivery |
| Shotstack | ~$0.30 | Rendering |

---

## 🌟 Contributing

PRs welcome! Know a great video tool for AI agents? Open an issue or PR.

---

## 📝 License

MIT — Do whatever you want with this list.
