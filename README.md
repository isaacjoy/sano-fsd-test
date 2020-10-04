# Sano Genetics Full-stack engineer task

# Isaac's Application

6. 

Loom video on enrollments: https://www.loom.com/share/76c5a80b4d594cd4974c12fa3faee8b8

7. **Suppose we would like to build a forum section for each Study. Users can create Posts, and Comment on other Users’ Posts. How would you build this? What would the database models and relationships look like? Write a paragraph outlining your strategy, and what considerations we would need to take into account.**

I think I would use Nuxt + Django REST to help Google’s better index the content for SEO purposes. The models would form a normalised data structure to be stored in a relational database. To start with, I would write the models in Django. Next I would would work on the frontend, initially not making any fancy design (just the logic with marrying the api). Finally, I would iterate on the design until I was happy. 

Things I would take into account: 

* Spam - strong user verification would be necessary. 
* SEO - to benefit from a massive amount of user generated content.
* Escaping input from raw text fields.

8.  **When you created an account, you specified a password. How would we validate that a user password is sufficiently complex so that it is difficult to crack? Are there third party options we could use? Explain your recommendations in a paragraph, and if you have time, implement a pragmatic solution.**

Force users to make a password that is longer than 6 characters and contains an uppercase, number and special character. For third party implementations we could verify against haveibeenpwned api to see if an email has been exposed with associated password. 

9. **This authentication system uses client localStorage. This is insecure - why? Demonstrate how a third party client dependency could maliciously break this login. Explain your recommendations in a paragraph, and if you have time, implement a pragmatic solution to the problem.**

It’s insecure because any JS code on page can access it like plugins. But if the worst case occurs and a hacker can execute JS on your website, having access to local storage is definitely not the worst thing that can happen (they could add a keylogger). I would recommend keeping your JWT in localstorage. 

