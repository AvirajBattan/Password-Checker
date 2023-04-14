#importing library
import requests
import sys
import hashlib

# this function takes the first five charachter of the hashed password (provided syntax by the api) and request for the password data and count with the help of api
def response(head):

  # main api link plus head of the password
  api='https://api.pwnedpasswords.com/range/'+head
  response=requests.get(api)
  
  if response.status_code!=200:
    raise RuntimeError('Error has occured')

  return response


# this funtion takes the tail of the hashed password and matches to the retrived data and return the count.
def count_pass(tail,pass_data):
  
    # print(pass_data.text.splitlines())
    for i in pass_data.text.splitlines():
        
        hased_pass,count=i.split(":")
        if tail==hased_pass:
            return count
    
    return 0


# this function encode the password in UTF-8 and then do the hashing with sha1 algorithm.
def check_pass(password):

  gen_hash=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  head=gen_hash[:5]
  tail=gen_hash[5:]
  password_data=response(head)
  
  return count_pass(tail,password_data)


def main(arg):
  
  #arg is the list of passwords to be check
  for password in arg:
    count=check_pass(password)
    if count:
      print(f"SEEMS LIKE PASSWORD IS BEEN HACKED {count} TIMES")
    else:
      print("NEVER HACKED")


if __name__=="__main__":

  # accepting the argument from the terminal
  sys.exit(main(sys.argv[1:]))