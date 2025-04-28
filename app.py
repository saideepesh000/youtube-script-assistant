import openai
import streamlit as st

openai.api_key = "YOUR-OPENAI-API-KEY"

def generate_outline(topic):
    prompt = f"Create a YouTube video script outline for the topic: '{topic}'. Structure it into Introduction, Main Points, and Conclusion."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an expert YouTube scriptwriter."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def expand_script(outline):
    prompt = f"Expand this YouTube script outline into a full 500-word script:\n\n{outline}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an expert YouTube scriptwriter."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def suggest_title(topic):
    prompt = f"Suggest 5 catchy YouTube video titles for the topic: '{topic}'."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a YouTube SEO expert."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("🎬 YouTube Video Script Assistant")

topic = st.text_input("Enter your video topic/title idea:")

if st.button("Generate Script"):
    if topic:
        with st.spinner('Generating outline...'):
            outline = generate_outline(topic)
        with st.spinner('Expanding into full script...'):
            script = expand_script(outline)
        with st.spinner('Suggesting titles...'):
            titles = suggest_title(topic)
        
        st.subheader("Script Outline")
        st.write(outline)
        
        st.subheader("Full Script")
        st.write(script)
        
        st.subheader("Title Suggestions")
        st.write(titles)
    else:
        st.error("Please enter a topic!")
