import streamlit as st


st.title("Cher's Quizlet")

# Initialize session state
if "setup_mode" not in st.session_state:
    st.session_state.setup_mode = True
    st.session_state.quiz = []
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.finished = False

if st.session_state.setup_mode:
    question = st.text_input("Question:")
    answer = st.text_area("Answer:")

    if st.button("Add Question", use_container_width=True):
        if question and answer:
            st.session_state.quiz.append({"question": question, "answer": answer})
            st.success("Question added!")
        else:
            st.warning("Please provide both a question and an answer.")

    if st.button("Start Quiz", use_container_width=True) and st.session_state.quiz:
        st.session_state.setup_mode = False
        st.session_state.total_questions = len(st.session_state.quiz)
    else:
        st.info(f"You've added {len(st.session_state.quiz)} question(s).")

else:
    if st.session_state.finished:
        st.write(f"Quiz complete! Your score is {st.session_state.score}/{st.session_state.total_questions}.")
        if st.button("Restart Quiz"):
            st.session_state.setup_mode = True
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.finished = False
    else:
        current_q = st.session_state.quiz[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question + 1}: {current_q['question']}")

        user_answer = st.text_input("Your answer:")

        if st.button("Submit", use_container_width=True):
            if user_answer.strip().lower() == current_q["answer"].strip().lower():
                st.session_state.score += 1

            st.session_state.current_question += 1

            if st.session_state.current_question == st.session_state.total_questions:
                st.session_state.finished = True