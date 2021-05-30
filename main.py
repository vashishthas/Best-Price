import requests
from bs4 import BeautifulSoup

def checkPrice(itemUrl, desiredPrice,to):
    try:
        headers={"User-Agent":'Your user agent'}  #Your user agent id needed
        page=requests.get(itemUrl,headers=headers)
        htmlContent=page.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        
        con=soup.find(id="priceblock_ourprice")
        if(con is None):
            con=soup.find(id="priceblock_dealprice")

        con=con.get_text().strip()
        price=float(con[2:])
        print(price)

        if(price<=desiredPrice):
            sendMail(itemUrl,to,price)

    except Exception as e:
        print(f"Error in finding the price:  {e}")

def sendMail(itemUrl,to,price):
    try:
        import smtplib
        emailId='email_needed' #sending email id
        password='password_needed' #sending email password
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(emailId,password)
        subject="Price fell down"
        body=f"The item price is {price}\nCheck the link:{itemUrl}"
        msg=f"Subject:{subject}\n\n {body}"
        server.sendmail(emailId,to,msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Some error occured while sending the email: {e}")

if __name__=='__main__':
    itemUrl=input("Enter item URL: ")
    desiredPrice=int(input("Enter desired price: "))
    to=input("Enter your mail where you want to receive notification: ")
    checkPrice(itemUrl,desiredPrice,to)