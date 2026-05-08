from groq import generate_response

import io, streamlit as st

SYSTEM_PROMPT = """You are a Math Wizard built by Aanya always precise, patient, and full of clarity.
For every math problem:
1. Show detailed steps
2. Explain the method
3. Highlight the final answer"""
def math_generate(problem:str,level:str,temperature=0.1,max_tokens=1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMath Problem ({level}): {problem}"
    return generate_response(prompt,temperature=temperature,max_tokens=max_tokens)
def exporttxt(history):
    txt = "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']}" for i, h in enumerate(history,1)])
    return io.BytesIO(txt.encode("utf-8"))
def setupui():
    st.set_page_config(page_title=" Math Genie",layout="centered")
    st.title("Math Genie")
    st.write("Solve nay math problem with detalied step-by-step explanation.")
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
if __name__ == "__main__":
    setupui()

