import streamlit as st

'''
made by Hamza, 

github repo: https://github.com/HamzaNasir0/Python-Fancy-Read-Me-Generator


'''

# --- CONFIG ---
st.set_page_config(
    page_title="Markdown Editor",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown(
    """
    <style>
    .header-title {
        font-family: 'Nunito', sans-serif;
        color: #2E86AB;
    }
    .sidebar .sidebar-content {
        background-color: #F7F9FB;
    }
    .download-btn {
        background-color: #2E86AB;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TITLE SECTION ---
st.markdown("<h1 class='header-title'>Markdown Editor</h1>", unsafe_allow_html=True)
st.markdown("Write your Markdown, preview it live, and download it as a `.md` file.")

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Settings")

# License choices + badge insertion
license_options = [
    "MIT License",
    "Apache License 2.0",
    "GNU GPLv3",
    "BSD 3-Clause",
    "Creative Commons Attribution 4.0",
    "None"
]
selected_license = st.sidebar.selectbox("Choose a license:", license_options)

file_name = st.sidebar.text_input("Output file name:", "README.md")

template_choice = st.sidebar.selectbox(
    "Insert a boilerplate template?",
    ["None", "Basic README", "Project README", "Blog Post"]
)

# --- TEMPLATES ---
TEMPLATES = {
    "Basic README": "# Project Title\n\n## Description\n\n## Installation\n\n## Usage\n\n## License\n",
    "Project README": "# Project Name\n\n### What it does\n\n### Why it matters\n\n### How to use it\n\n### Screenshots\n\n### License\n",
    "Blog Post": "# Blog Post Title\n\n## Intro\n\n## Main Content\n\n## Conclusion\n\n---\n*Published on …*"
}

# --- LICENSE BADGES & TEXT ---
LICENSE_BADGES = {
    "MIT License": "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
    "Apache License 2.0": "[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)",
    "GNU GPLv3": "[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)",
    "BSD 3-Clause": "[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)",
    "Creative Commons Attribution 4.0": "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0)",
    "None": ""
}

LICENSE_TEXT = {
    "MIT License": "This project is licensed under the MIT License.",
    "Apache License 2.0": "Licensed under the Apache License, Version 2.0.",
    "GNU GPLv3": "This project is licensed under the GNU GPL v3.0.",
    "BSD 3-Clause": "Distributed under the BSD 3-Clause License.",
    "Creative Commons Attribution 4.0": "Licensed under CC BY 4.0.",
    "None": ""
}

# --- MAIN AREA ---
if template_choice != "None":
    default_text = TEMPLATES[template_choice]
else:
    default_text = ""

markdown_text = st.text_area(
    "Write your Markdown here:",
    value=default_text,
    height=350,
    placeholder="# Your Title\n\nYour content here..."
)

# --- PROCESSING ---
final_md = markdown_text
if selected_license != "None":
    badge = LICENSE_BADGES[selected_license]
    final_md = badge + "\n\n" + final_md
    final_md += f"\n\n---\n **License:** {LICENSE_TEXT[selected_license]}"

# --- LIVE PREVIEW & ACCENT STYLING ---
if markdown_text.strip():
    st.markdown("### Live Preview", unsafe_allow_html=True)
    # Insert accent stylings using inline HTML styles if necessary
    styled_preview = f"<div style='color:blue; font-weight:bold;'>{final_md}</div>"
    # But to keep Markdown rendering, we just display normally
    st.markdown(final_md, unsafe_allow_html=True)
    
    # Download Button
    st.download_button(
        label="Download .md",
        data=final_md,
        file_name=file_name if file_name.endswith(".md") else f"{file_name}.md",
        mime="text/markdown"
    )
    st.success("Your file is ready for download!")
else:
    st.info("Start typing Markdown above to see the preview and download button.")

# --- FOOTER ---
st.markdown(
    f"""<hr>
    <p style="text-align:center; font-size:large; color:grey;">
    Made By Hamza using <a href="https://streamlit.io" target="_blank">Streamlit</a>
    </p>""",
    unsafe_allow_html=True
)
