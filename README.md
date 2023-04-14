# Password-Checker
Its Motive is tell that whether your password is UNIQUE and SAFE or not.

This is python script that tells whether "Given Password" is being found in the data breach or not.
If any user around the world have used "Given Password" for authentication and if that password is found in data breached password list then this script retruns number of times this password is being found.

In this Script we use API to collect the password data (API is PROVIDED in code).
In this Script to collect the data we have to First encode the password using ths "SHA1" algorithm and then using the first 5 charachter we have to make API call to get the list of the password.
Data that we get from api call is the list  of the tails of the password (tail is explain in code) is the tail of the respose data matches to the tail of our password than "COUNT" is returned.
