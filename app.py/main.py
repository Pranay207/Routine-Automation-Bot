import streamlit as st
from tracker import init_db, log_task, get_logs
from reminders import send_email_reminder  # or send_whatsapp_reminder

# Initialize DB
init_db()

st.title("🧘 Daily Routine Automation Bot")

# Input Section
st.subheader("Log Your Task")
task_name = st.text_input("Task Name")
status = st.selectbox("Status", ["Done", "Skipped"])
if st.button("Log Task"):
    if task_name:
        log_task(task_name, status)
        st.success(f"Logged: {task_name} - {status}")
    else:
        st.error("Enter a task name!")

# View Logs
st.subheader("📊 Task Logs")
logs = get_logs()
if logs:
    st.table(logs)
else:
    st.info("No tasks logged yet.")

# Send Reminder (Manual for Testing)
st.subheader("Send Reminder")
reminder_task = st.text_input("Task to Remind")
recipient_email = st.text_input("Recipient Email")
smtp_user = st.text_input("SMTP Email")
smtp_pass = st.text_input("SMTP Password", type="password")

if st.button("Send Email Reminder"):
    if reminder_task and recipient_email and smtp_user and smtp_pass:
        send_email_reminder(recipient_email, "Daily Reminder", f"Don't forget to do: {reminder_task}", smtp_user, smtp_pass)
        st.success(f"Reminder sent to {recipient_email}")
    else:
        st.error("Fill all fields to send reminder!")

