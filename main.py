from smtplib import SMTP
from email.message import EmailMessage

# FOR GOOGLE EMAIL:
google_port = 587
google_fqdn_host = 'smtp.gmail.com'
google_smtp_server = 'smtp.gmail.com:587'

# both of below two lines of codes work for creating a smtp server
smtp_server = SMTP(google_fqdn_host, google_port)
# smtp_server = SMTP(google_smtp_server)

# log into email account with email address and password
# password below is retrieved from a private text file. You can create a text file
# to store your own password and retrieve it by reading the file. My email address
# is also stored inside the text file, on its first line. The second line is password.
with open('password.txt', 'r') as file:
    myemail = file.readline().strip()
    password = file.readline().strip()

# create email message with Python's email module
# I stored email content inside a txt file
with open('email_content.txt', 'r') as f:
    # create a text/plain message instance
    msg = EmailMessage()
    msg.set_content(f.read())

# headers of EmailMessage
msg['Subject'] = f'Read this Test Email'
msg['From'] = 'Me'
# for sending to multiple addresses, each email can be seperated by a comma ','
msg['To'] = "yourownemail@address.com" 

# attach image to the file, 
with open('myimage.jpg', 'rb') as f:
    img_byte = f.read()
# if the image type is unknown, there are Python libraries for such as 
# 'filetype' etc for infering file type and MIME type
msg.add_attachment(img_byte, maintype='image', subtype='jpg')


# Now since the headers, content and attachment has been added to msg,
# we can send email message thru the smtp server

# smtp_server.starttls() # for yahoo and gmail, this is needed before login() call

# Instead the above line of code,we use 'with' statement.
# the SMTP QUIT command is issued automatically when the with statement exits.
with SMTP(google_smtp_server) as server:    
    server.starttls() # call this before login()
    server.login(myemail, password)
    server.send_message(msg)
 
# smtp_server.quit()

