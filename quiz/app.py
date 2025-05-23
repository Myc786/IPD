import streamlit as st
import datetime

st.set_page_config(page_title="IPD Quiz App", layout="wide")
st.title("📘 IPD Quiz App – Day-by-Day Assessment")

# --- Sidebar Navigation ---
day = st.sidebar.selectbox("Select Quiz Day", ["Day One", "Day Two (Coming Soon)"])
st.sidebar.markdown("---")
st.sidebar.markdown("📅 Date: May 12, 2025")

if day == "Day One":
    st.header("Day One – Teaching as a Profession & Role of Teachers")
    st.markdown("Answer the questions below. You'll get feedback after submission.")

    questions = [
        {
            "question": "What is the main purpose of the Initial Professional Development (IPD) programme for PSTs?",
            "options": ["To teach new subjects to teachers", "To orient newly recruited teachers with professional knowledge, skills, and attitudes", "To conduct exams for teachers", "To replace existing teachers"],
            "answer": "To orient newly recruited teachers with professional knowledge, skills, and attitudes",
            "explanation": "The IPD programme aims to equip newly recruited PSTs with the necessary professional knowledge, skills, and attitudes to perform their duties effectively."
        },
        {
            "question": "What is one of the key activities conducted on Day 1 of the IPD programme?",
            "options": ["Conducting a post-test", "Discussing teachers' role as facilitators", "Preparing lesson plans", "Microteaching practice"],
            "answer": "Discussing teachers' role as facilitators",
            "explanation": "Day 1 includes discussing teachers' role as facilitators from 11:30 am to 01:30 pm."
        },
        {
            "question": "According to Handout 1.1, what theme did UNESCO announce for World Teachers' Day in October 2022?",
            "options": ["Teachers and Technology", "The Transformation of Education Begins with Teachers", "Education for All", "Teachers as Leaders"],
            "answer": "The Transformation of Education Begins with Teachers",
            "explanation": "UNESCO announced the theme 'The Transformation of Education Begins with Teachers' for World Teachers' Day 2022."
        },
        {
            "question": "What is one of the seven criteria used to define teaching as a profession?",
            "options": ["High salary packages", "Organized body of professional knowledge", "Short working hours", "Minimal training requirements"],
            "answer": "Organized body of professional knowledge",
            "explanation": "Teaching is defined as a profession by having an organized body of professional knowledge that separates teachers from others."
        },
        {
            "question": "Why should teaching be considered a noble profession?",
            "options": ["It offers high financial rewards", "It prepares students for their future life and inspires them", "It requires minimal effort", "It has no challenges"],
            "answer": "It prepares students for their future life and inspires them",
            "explanation": "Teaching is a noble profession because it prepares students for their future life and inspires them, beyond just imparting knowledge."
        },
        {
            "question": "What does the joint message from ILO, UNESCO, and others emphasize on World Teachers' Day 2022?",
            "options": ["Reducing teachers' workload", "Bringing qualified, supported, and inspirational teachers into classrooms", "Increasing teachers' salaries", "Shortening the school year"],
            "answer": "Bringing qualified, supported, and inspirational teachers into classrooms",
            "explanation": "The joint message emphasizes bringing qualified, supported, and inspirational teachers into classrooms to improve learning and well-being."
        },
        {
            "question": "What is a key challenge for the teaching profession mentioned in Handout 1.1?",
            "options": ["Lack of holidays", "It doesn’t enjoy high status in society compared to other professions", "Too many teachers in the field", "No need for professional development"],
            "answer": "It doesn’t enjoy high status in society compared to other professions",
            "explanation": "A general opinion is that teaching doesn’t enjoy high status in society like doctors or engineers."
        },
        {
            "question": "What is one measure suggested to enhance the status of the teaching profession?",
            "options": ["Reducing teacher training", "Attracting the brightest graduates to teaching with a passion for learning", "Limiting teachers' roles", "Decreasing the use of technology"],
            "answer": "Attracting the brightest graduates to teaching with a passion for learning",
            "explanation": "Attracting bright graduates with a passion for learning is a measure to enhance the status of teaching."
        },
        {
            "question": "What role do teachers play in contributing to society, according to Handout 1.1?",
            "options": ["They focus only on academic exams", "They provide personal and caring service by diagnosing students’ learning needs", "They avoid community involvement", "They limit student interaction"],
            "answer": "They provide personal and caring service by diagnosing students’ learning needs",
            "explanation": "Teachers contribute to society by diagnosing students’ learning needs and using relevant pedagogies."
        },
        {
            "question": "What is a requirement for teachers to progress in their career?",
            "options": ["Avoiding continuous professional development", "Completing professional qualifications and participating in CPD", "Teaching only one subject", "Working independently without collaboration"],
            "answer": "Completing professional qualifications and participating in CPD",
            "explanation": "Teachers must complete professional qualifications and participate in CPD to progress."
        },
        {
            "question": "What is the purpose of Activity 1.1 on Day 1?",
            "options": ["To conduct a practical teaching session", "To discuss the importance of the teaching profession and CPs’ views", "To prepare a lesson plan", "To evaluate teaching portfolios"],
            "answer": "To discuss the importance of the teaching profession and CPs’ views",
            "explanation": "Activity 1.1 involves brainstorming on the importance of the teaching profession and CPs’ views."
        },
        {
            "question": "What is one question CPs are asked to discuss in Activity 1.1?",
            "options": ["How to use technology in teaching", "Why should teaching be considered a profession?", "How to manage a classroom", "What is the national curriculum?"],
            "answer": "Why should teaching be considered a profession?",
            "explanation": "One question in Activity 1.1 is 'Why should teaching be considered as profession?'"
        },
        {
            "question": "What does Handout 1.2 quote from John Dewey?",
            "options": ["'Teach today as you did yesterday.'", "'You can’t teach today the same way you did yesterday to prepare students for tomorrow.'", "'Teachers should avoid technology.'", "'Students don’t need critical thinking.'"],
            "answer": "'You can’t teach today the same way you did yesterday to prepare students for tomorrow.'",
            "explanation": "John Dewey’s quote is about adapting teaching methods for the future."
        },
        {
            "question": "What has changed in the 21st century education system, according to Handout 1.2?",
            "options": ["It has become less technological", "It emphasizes students’ thinking, interpersonal, and technological skills", "It focuses only on rote learning", "It avoids student engagement"],
            "answer": "It emphasizes students’ thinking, interpersonal, and technological skills",
            "explanation": "The 21st century education system emphasizes thinking, interpersonal, and technological skills."
        },
        {
            "question": "What is the new role of teachers in the 21st century, as per Handout 1.2?",
            "options": ["Sage on the stage", "Guide on the side or facilitator", "Strict disciplinarian", "Exam coordinator"],
            "answer": "Guide on the side or facilitator",
            "explanation": "Teachers’ role has shifted from 'sage on the stage' to 'guide on the side' or facilitator."
        },
        {
            "question": "What is one responsibility of 21st-century teachers mentioned in Handout 1.2?",
            "options": ["Avoiding digital tools", "Preparing students for future life by fostering critical thinking and creativity", "Limiting student interaction", "Focusing only on textbooks"],
            "answer": "Preparing students for future life by fostering critical thinking and creativity",
            "explanation": "Teachers must prepare students for future life by fostering critical thinking and creativity."
        },
        {
            "question": "What is a major challenge for teachers in the 21st century, according to Handout 1.2?",
            "options": ["Reducing classroom time", "Improving their digital literacy and making students digitally literate", "Avoiding student feedback", "Teaching without lesson plans"],
            "answer": "Improving their digital literacy and making students digitally literate",
            "explanation": "A key challenge is improving digital literacy for both teachers and students."
        },
        {
            "question": "What does the 'teacher as leader' role involve, as per Handout 1.2?",
            "options": ["Limiting their role to classroom teaching", "Motivating and supporting meaningful educational change across the system", "Avoiding collaboration with others", "Focusing only on administrative tasks"],
            "answer": "Motivating and supporting meaningful educational change across the system",
            "explanation": "Teachers as leaders motivate and support educational change across the system."
        },
        {
            "question": "What is one role teachers perform as pedagogical leaders?",
            "options": ["Avoiding curriculum implementation", "Influencing students’ learning through active engagement and optimizing resources", "Reducing student participation", "Ignoring national standards"],
            "answer": "Influencing students’ learning through active engagement and optimizing resources",
            "explanation": "Pedagogical leaders influence learning through active engagement and resource optimization."
        },
        {
            "question": "What has changed about students’ needs in the 21st century, according to Handout 1.2?",
            "options": ["They need less engagement", "Their learning needs and interests have changed", "They don’t require technology", "They prefer traditional teaching"],
            "answer": "Their learning needs and interests have changed",
            "explanation": "Students’ learning needs and interests have changed in the 21st century."
        },
        {
            "question": "What is one goal of the 21st-century learning framework mentioned in Handout 1.2?",
            "options": ["Reducing teachers’ roles", "Achieving Sustainable Development Goals, especially Goal 4 on quality education", "Limiting technology use", "Focusing only on exams"],
            "answer": "Achieving Sustainable Development Goals, especially Goal 4 on quality education",
            "explanation": "The framework aims to achieve SDGs, especially Goal 4 on quality education."
        },
        {
            "question": "What is one quality of effective teachers highlighted in Handout 1.2?",
            "options": ["Avoiding lifelong learning", "Being builders of the nation and lifelong learners", "Limiting student interaction", "Ignoring digital literacy"],
            "answer": "Being builders of the nation and lifelong learners",
            "explanation": "Effective teachers are builders of the nation and lifelong learners."
        },
        {
            "question": "What is one question CPs are asked in Activity 1.2?",
            "options": ["How to prepare a lesson plan?", "What are the essential qualities of 21st-century teachers?", "How to conduct a pre-test?", "What is the national curriculum framework?"],
            "answer": "What are the essential qualities of 21st-century teachers?",
            "explanation": "Activity 1.2 asks, 'What are the essential qualities of 21st-century teachers?'"
        },
        {
            "question": "Why is the integration of technology important in 21st-century teaching?",
            "options": ["To reduce teaching time", "To prepare students for their digital lives and future", "To avoid student engagement", "To limit critical thinking"],
            "answer": "To prepare students for their digital lives and future",
            "explanation": "Technology integration prepares students for their digital lives and future."
        },
        {
            "question": "What does Handout 1.2 suggest teachers should create in the classroom?",
            "options": ["A strict environment", "An enabling environment for collaborative learning", "A teacher-centered environment", "A silent classroom"],
            "answer": "An enabling environment for collaborative learning",
            "explanation": "Teachers should create an enabling environment for collaborative learning."
        },
        {
            "question": "What is one way teachers can develop students holistically, according to Handout 1.2?",
            "options": ["Using a single teaching method", "Using a multidisciplinary approach to teaching and learning", "Avoiding group activities", "Limiting student creativity"],
            "answer": "Using a multidisciplinary approach to teaching and learning",
            "explanation": "A multidisciplinary approach helps develop students holistically."
        },
        {
            "question": "What is one suggestion for transforming teacher education from Handout 1.1?",
            "options": ["Reducing the practicum component", "Including a practicum/clinical component", "Avoiding professional certification", "Limiting teacher training"],
            "answer": "Including a practicum/clinical component",
            "explanation": "Transforming teacher education includes adding a practicum/clinical component."
        },
        {
            "question": "What does Handout 1.2 say about the complexity of teaching in the 21st century?",
            "options": ["Teaching has become simpler", "Teaching has become quite complex and demanding", "Teaching requires no new skills", "Teaching avoids technology"],
            "answer": "Teaching has become quite complex and demanding",
            "explanation": "Teaching has become quite complex and demanding in the 21st century."
        },
        {
            "question": "What is one role of teachers as facilitators mentioned in Handout 1.2?",
            "options": ["Delivering lectures only", "Preparing students for future life by fostering critical thinking", "Avoiding student questions", "Focusing only on exams"],
            "answer": "Preparing students for future life by fostering critical thinking",
            "explanation": "As facilitators, teachers prepare students for future life by fostering critical thinking."
        },
        {
            "question": "What is the final task for CPs on Day 1?",
            "options": ["Conducting a post-test", "Reflecting on their professional learning for sharing the next day", "Preparing a lesson plan", "Delivering a microteaching session"],
            "answer": "Reflecting on their professional learning for sharing the next day",
            "explanation": "CPs must reflect on their professional learning for sharing with a large group the next day."
        }
    ]

    responses = []
    submitted = False

    with st.form("quiz_form"):
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            responses.append(st.radio("", q['options'], key=f"q{i}"))
        submitted = st.form_submit_button("Submit")

    if submitted:
        score = 0
        feedback = []
        for i, q in enumerate(questions):
            user_ans = responses[i]
            if user_ans == q['answer']:
                st.success(f"✅ Q{i+1}: Correct – {q['answer']}")
                score += 1
            else:
                st.error(f"❌ Q{i+1}: Incorrect – Correct answer: {q['answer']}")
                feedback.append(f"Q{i+1}. Correct answer: {q['answer']}\nExplanation: {q['explanation']}")

        st.markdown("### 🧾 Your Result")
        st.info(f"You scored **{score} out of {len(questions)}**.")

        if feedback:
            st.markdown("### 📝 Feedback")
            for fb in feedback:
                st.write(fb)

        # Downloadable result
        if st.button("📄 Download Result as Text"):
            result_text = f"Day: {day}\nScore: {score}/{len(questions)}\n\n"
            for i, q in enumerate(questions):
                result_text += f"Q{i+1}: {q['question']}\nYour Answer: {responses[i]}\nCorrect Answer: {q['answer']}\nExplanation: {q['explanation']}\n\n"
            st.download_button("Download Results", result_text, file_name="ipd_day_one_results.txt")

elif day == "Day Two (Coming Soon)":
    st.warning("🚧 Day Two content is under construction. Please check back later.")
