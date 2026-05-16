import io,re
from io import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config5
from groq import generate_response

MATH_SYSTEM =  """You are a Math Wizard built by Omkar, trained to help students master math..."""
IMAGE_MODEL = "stabilityai/stable-diffusion-3-medium-diffusers"
IMAGE_NEGATIVE_PROMPT = "ugly, blurry, low quality, deformed, bad anatomy"
CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card{border:1px solid #e6e6e6;background:#fff;border-radius:10px;padding:14px 16px;margin:10px 0;
box-shadow:0 1px 2px rgba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
.a{white-space:pre-wrap;color:#333;line-height:1.5;}
</style>
"""
img_client = InferenceClient(api_key=config5.HF_API_KEY)
def exporttext(history):
    txt = "".join([f"Q{i}]: {h['question']}\nA{i}: {h['answer']}\n\n" for i,h in enumerate(history,1)])
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio
def teachinganser(q:str) -> str:
    return generate_response(q,temperature=0.3,max_tokens=1024)
def mathagenerate(q: str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nMaths Problem: {q}"
    return generate_response(prompt,temperature=0.1,max_tokens=1024)

math_generate = mathagenerate
def generate_image(prompt: str):
    try:
        image = img_client.text_to_image(prompt=prompt, model=IMAGE_MODEL, negative_prompt=IMAGE_NEGATIVE_PROMPT)
        return image, None
    except Exception as e:
        return None, str(e)
def run_ai_teachingassistant():
    st.title("Teaching Genie")
    st.session_state.setdefault("history_ata", [])
    st.session_state.setdefault("last_image", None)
    c1, c2 = st.columns([1, 2])
    with c1:
        mode = st.selectbox("Assistant", ["Teaching Assistant", "Math Assistant", "Text-to-Image"])
        label = "Image Prompt" if mode == "Text-to-Image" else "Question"
        question = st.text_area(label, height=160)
        difficulty = None
        if mode == "Math Assistant":
            difficulty = st.selectbox("Difficulty", ["Beginner", "Regular", "Challenging"], index=1)
        if st.button("Ask"):
            q = (question or "").strip()
            if not q:
                st.warning("Please enter a prompt.")
            else:
                if mode == "Math Assistant":
                    ans = math_generate(q, difficulty)
                    st.session_state["history_ata"].insert(0, {"question": q, "answer": ans, "mode": mode, "difficulty": difficulty})
                elif mode == "Text-to-Image":
                    image, err = generate_image(q)
                    if err:
                        st.error(f"Image generation failed: {err}")
                        st.session_state["last_image"] = None
                        ans = "Image generation failed."
                    else:
                        st.session_state["last_image"] = image
                        ans = "Image generated successfully."
                        st.session_state["history_ata"].insert(0, {"question": q, "answer": ans, "mode": mode, "difficulty": difficulty})
                else:
                    ans = teachinganser(q)
                    st.session_state["history_ata"].insert(0, {"question": q, "answer": ans, "mode": mode, "difficulty": difficulty})
        if st.button("Clear History"):
            st.session_state["history_ata"] = []
            st.session_state["last_image"] = None
        st.download_button("Export History", data=exporttext(st.session_state["history_ata"]), file_name="teaching_history.txt")
    with c2:
        st.markdown(CHAT_CSS, unsafe_allow_html=True)
        st.subheader("Conversation")
        if st.session_state.get("last_image") is not None:
            st.image(st.session_state["last_image"], caption="Generated image", use_column_width=True)
            try:
                buf = BytesIO()
                st.session_state["last_image"].save(buf, format="PNG")
                st.download_button("Download Image", buf.getvalue(), "generated_image.png", "image/png")
            except Exception:
                pass
        if not st.session_state["history_ata"]:
            st.info("No interactions yet — ask a question from the left.")
        else:
            for i, h in enumerate(st.session_state["history_ata"], 1):
                meta = h.get("difficulty") or h.get("mode") or ""
                st.markdown(f"<div class='card'><div class='q'>Q{i}: {h['question']}</div><div class='meta'>{meta}</div><div class='a'>{h['answer']}</div></div>", unsafe_allow_html=True)
def exporttxt(history):
    txt = "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']}" for i, h in enumerate(history,1)])
    return io.BytesIO(txt.encode("utf-8"))
def setupui():
    st.set_page_config(page_title=" Math Genie",layout="centered")
    st.title("Math Genie")
    st.write("Solve any math problem with detalied step-by-step explanation.")
    with st.expander("My Example Problems"):
        st.markdown(""" **Probability:** Tossing coins, rolling dice
        - Example: 'What's the probability of getting heads twice in 3 coin tosses?'
        **Algebra:** Word problems and equations
        - Example: 'A number increases by 5 is 12. What's the number?' """)
        st.session_state.setdefault("history",[])
        st.session_state.setdefault("k",0)
        c1,c2 = st.columns([1,2])
        if c1.button("Clear"):
            st.session_state.history = []; st.rerun()
        if st.session_state.history:
            c2.download_button("Export",exporttxt(st.session_state.history),"Math_Mastermind_Solutions.txt ","text/plain")
        with st.form("math_form",clear_on_submit=True):
            q = st.text_area("Enter your math problem:", height = 100,placeholder="Example: Solve x^2 + 5x + 6 = 0",key=f"q_{st.session_state.k}")
            a,b = st.columns([3,1])
            solve = a.form_submit_button("Solve",use_container_width=True)
            level = b.selectbox("Choose your level",["Beginner","Regular","Challenging"],index = 1)
            if solve:
                if not q.strip(): st.warning("Enter problem first.")
                else:
                    with st.spinner("Solving..."):
                        ans = math_generate(q.strip(),level)
                    st.session_state.history.insert(0,{"q":q.strip(),"a":ans,"lvl":level})
                    st.session_state.k += 1; st.rerun()
        if not st.session_state.history: return
        st.markdown("### 🧾 Solution History (Latest First)")
        st.markdown("""<style>
                        .box{max-height:500px;overflow-y:auto;border:2px solid #4CAF50;padding:12px;background:#f7fbff;border-radius:10px}
                        .q{font-weight:700;color:#2E7D32;margin-top:12px}
                        .lvl{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
                        .a{white-space:pre-wrap;color:#1B5E20;background:#fff;padding:10px;border-radius:8px;border-left:4px solid #4CAF50;margin:6px 0 14px}
                        </style>""", unsafe_allow_html=True)
        html = '<div class = "box">'
        for i ,h in enumerate(st.session_state.history,1):
                    html += f'<div class = "q">Q{i}: {h["q"]}<span class = "lvl">{h["lvl"]}</span></div>'
                    html += f'<div class = "a"> {h["a"]}</div>'
        st.markdown(html + "</div>",unsafe_allow_html=True)
def main():
    st.set_page_config(page_title="Modular AI Toolbox", layout="centered")
    run_ai_teachingassistant()
if __name__ == "__main__":
    main()


