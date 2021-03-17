# 0x06. Regular expression

## Concepts

_For this project, students are expected to look at this concept:_

-   [Regular Expression](https://intranet.hbtn.io/concepts/29)
## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the  `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```

## Resources

**Read or watch**:

-   [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg "Regular expressions - basics")
-   [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q "Regular expressions - advanced")
-   [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ "Rubular is your best friend")
-   [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw "Use a regular expression against a problem: now you have 2 problems")
-   [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A "Learn Regular Expressions with simple, interactive exercises")

## Tasks
### 0. Simply matching Holberton
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210317T100322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=50307287ea3896e95bd8fced1aab872530ce69e31f1ca5e25c0ba2900a0a28fb)

Requirements:

-   The regular expression must match  `Holberton`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```
### 1. Repetition Token #0
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210317T100322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c76c39f35aba87787aba31db41a3da0fe85726ae5ceefa381eec37631bd8d4f0)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 2. Repetition Token #1
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210317T100322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=19bc2ebd4288421f4aebbbbb826f883e33404594faf657acbaa61027088fd6d1)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 3. Repetition Token #2
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210317T100322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a590907203ae5682ef22064909d7784108535d7c5b938e0c57e8d879fe241d6b)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
### 4. Repetition Token #3
![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210317%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210317T100322Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9936ff980176f1c70600639a9665d865d0cc43107069bb4b02c5dbfec1cca116)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets
### 5. Not quite HBTN yet
Requirements:

-   The regular expression must be exactly matching a string that starts with  `h`  ends with  `n`  and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```
### 6. Call me maybe
This task is brought to you by Holberton professional advisor  [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw "Neha Jain"), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```
### 7. OMG WHY ARE YOU SHOUTING?
Requirement:

-   The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```
### 8. Textme
This exercise was prepared for you by  [Guillaume Plessis](https://intranet.hbtn.io/rltoken/l2JCUH5R2qdg7YVMYR1UmA "Guillaume Plessis"), VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project  [on Twitter](https://intranet.hbtn.io/rltoken/FuFAuWPWMeiCgyQkh3SwZA "on Twitter").

For this task, youll be taking over Guillaumes responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

-   Your script should output:  `[SENDER],[RECEIVER],[FLAGS]`
    -   The sender phone number or name (including country code if present)
    -   The receiver phone number or name (including country code if present)
    -   The flags that were used

You can find a  [log file here](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/78/text_messages.log "log file here").

Example:

```
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
```
### 9. Pass LinkedIn technical interview level0
One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.


