import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
def sentmail():
#**********************************************Mail Module**********************************************************
    fromaddr = "xyz@gmail.com"
    toaddr = "xyz@gmail.com"
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    # storing the receivers email address  
    msg['To'] = toaddr  
    # storing the subject  
    msg['Subject'] ="Automated Mail"  
    # string to store the body of the mail 
    body ="""Hi Sir/Ma'am,

    This is Automation Mail using Python mail from Python Beginners please do not reply this mail this is system genrated mail

    Thanks,
    Python Beginners Team"""
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent  
    filename = 'test.xlsx'
    attachment = open(filename, "rb")
    #with path Attachment
    #attachment=open("E://Prediction_Work//Data_Mail_Json//BoxOffice2019-12-24.xlsx","rb")
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "Your Gmail Password here") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text)
    #Mail Sent Confirmation
    print("Mail Sent Sucessfully")
    # terminating the session 
    s.quit()
#*****************************************************End Sent mail code****************************************************
sentmail()
