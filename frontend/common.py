import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GLOBAL_CSS = """
<style>
/* Hide default Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}

/* Global Theme */
.stApp { 
    background: #05050a; 
    color: #e8e8ea; 
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* Typography */
h1, h2, h3 { 
    font-family: 'Outfit', 'Segoe UI', sans-serif; 
    font-weight: 700;
    letter-spacing: -0.5px;
}
h1 { color: #ffffff; }
h2 { color: #5eead4; margin-top: 1rem; }

/* Links */
a { 
    color: #5eead4 !important; 
    text-decoration: none;
    transition: color 0.2s ease-in-out;
}
a:hover {
    color: #9adfb6 !important;
    text-decoration: underline;
}

/* Badges / Skills */
.badge {
    display: inline-block; 
    background: rgba(47, 74, 60, 0.4);
    color: #5eead4; 
    border: 1px solid rgba(94, 234, 212, 0.3);
    border-radius: 999px; 
    padding: 6px 14px; 
    font-size: 13px; 
    font-weight: 500;
    margin: 4px 6px 4px 0;
    transition: all 0.3s ease;
    backdrop-filter: blur(4px);
}
.badge:hover {
    background: rgba(94, 234, 212, 0.15);
    border-color: rgba(94, 234, 212, 0.6);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(94, 234, 212, 0.1);
}

/* Streamlit Container / Cards styling */
[data-testid="stVerticalBlock"] > div > [data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 1rem;
    transition: all 0.3s ease;
}
[data-testid="stVerticalBlock"] > div > [data-testid="stVerticalBlockBorderWrapper"]:hover {
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(94, 234, 212, 0.3);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #05050a;
}
::-webkit-scrollbar-thumb {
    background: #1e2b22;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #2f4a3c;
}
</style>
"""