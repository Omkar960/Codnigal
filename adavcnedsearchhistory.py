from hf import generate_response
import streamlit as st
import io
def setup_ui():
    st.set_page_config(page_title="AI Teaching Assistant", layout="centered")
    st.title("AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")

    if "history" not in st.session_state:
        st.session_state.history = []
    user_input = st.text_input("Enter your question here:")
    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button("Clear Conversation"):
            st.session_state.history = []
            st.experimental_rerun()
    with col_export:
        if st.session_state.history:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, start=1):
                export_text += f"Q{idx}: {qa['question']}\nA{idx}: {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)
            st.download_button(
                label="Export Chat History",
                data=bio,
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain",
            )
    if st.button("Ask"):
        if user_input and user_input.strip():
            with st.spinner("Generating AI response..."):
                response = generate_response(user_input.strip(), temperature=0.3)
                st.session_state.history.append({
                    "question": user_input.strip(),
                    "answer": response,
                })
                st.experimental_rerun()
        else:
            st.warning("Please enter a question before clicking Ask.")
    st.markdown("### Conversation History")
    st.markdown(
        """<style>
            .history-wrap {max-height: 420px; overflow-y: auto; padding-right: 6px;}
            .qa-card {border: 1px solid #e6e6e6; background: #ffffff; border-radius: 10px; padding: 14px 16px; margin: 10px 0; box-shadow: 0 1px 2px rgba(0,0,0,0.04);}
            .q {font-weight: 700; color: #0a6ebd; margin-bottom: 8px;}
            .a {white-space: pre-wrap; color: #333; line-height: 1.5;}
        </style>""",
        unsafe_allow_html=True,
    )
    history_html = '<div class="history-wrap">'
    for idx, qa in enumerate(st.session_state.history, start=1):
        history_html += (
            '<div class="qa-card">'
            f'<div class="q">Q{idx}: {qa["question"]}</div>'
            f'<div class="a">A{idx}: {qa["answer"]}</div>'
            '</div>'
        )
    history_html += '</div>'
    st.markdown(history_html, unsafe_allow_html=True)
def main():
    setup_ui()
if __name__ == "__main__":
    main()