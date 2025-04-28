import streamlit as st
import openai

# Set your OpenAI API Key
openai.api_key = st.secrets["openai"]["api_key"]

# Function to generate an outline
def generate_outline(topic, tone):
    prompt = f"Create a YouTube video script outline for the topic: '{topic}'. Structure it into Introduction, Main Points, and Conclusion. Make it in a {tone} tone."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert YouTube scriptwriter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to expand the outline into a full script
def expand_script(outline, tone):
    prompt = f"Expand this YouTube script outline into a full 500-word script in a {tone} tone:\n\n{outline}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert YouTube scriptwriter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to suggest catchy titles
def suggest_title(topic):
    prompt = f"Suggest 5 catchy YouTube video titles for the topic: '{topic}'."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a YouTube SEO expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("🎬 YouTube Video Script Assistant")

# Input fields
topic = st.text_input("Enter your video topic/title idea:")

tone = st.selectbox(
    "Choose the tone/style for your video:",
    ("Friendly", "Funny", "Educational", "Storytelling", "Serious")
)

# Button to generate the script
if st.button("Generate Script"):
    if topic:
        with st.spinner('Generating outline...'):
            outline = generate_outline(topic, tone)
        with st.spinner('Expanding into full script...'):
            script = expand_script(outline, tone)
        with st.spinner('Suggesting titles...'):
            titles = suggest_title(topic)
        
        # Display the results
        st.subheader("Script Outline")
        st.write(outline)
        
        st.subheader("Full Script")
        st.write(script)
        
        st.subheader("Title Suggestions")
        st.write(titles)
    else:
        st.error("⚠️ Please enter a topic to generate a script!")
