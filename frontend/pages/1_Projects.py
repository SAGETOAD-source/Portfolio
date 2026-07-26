import streamlit as st
from common import GLOBAL_CSS
from data import PROJECTS

st.set_page_config(page_title="Projects | Krishnendu Das", page_icon="💻", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

projects = PROJECTS

# Maps exact project title -> list of asset paths (images/video) to show under that card
MEDIA_MAP = {
    "Auto Shorts Bot — Automated Short-Form Video Pipeline": {
        "video": "frontend/assets/demo_clip.mp4",
    },
    "AI Shorts Generator from Long-Form Video": {
        "images": [
            "frontend/assets/ai_shorts_hero.jpg",
            "frontend/assets/ai_shorts_clips.jpg",
            "frontend/assets/ai_shorts_analysis.jpg",
        ],
    },
    "AI Meme Caption Generator": {
        "images": ["frontend/assets/meme_caption_generator.jpg"],
    },
    "Project Clown — Custom Chrome New Tab Extension": {
        "images": ["frontend/assets/project_clown_dashboard.png"],
    },
}

st.markdown("# Projects")

for p in projects:
    with st.container(border=True):
        star = "⭐ " if p.get("flagship") else ""
        st.markdown(f"### {star}{p['title']}")
        st.caption(p['stack'])
        st.write(p['description'])

        links = f"[GitHub]({p['github']})"
        for k, v in p.get("links", {}).items():
            links += f"  •  [{k}]({v})"
        st.markdown(links)

        media = MEDIA_MAP.get(p['title'])
        if media:
            if "video" in media:
                st.video(media["video"])
            if "images" in media:
                for img in media["images"]:
                    st.image(img, use_column_width=True)