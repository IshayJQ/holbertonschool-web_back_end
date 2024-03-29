 ![Project badge](https://intranet.hbtn.io/assets/pathway/006_color-21d9dd12a952c0dcfa9471902c922dde2a053f71943f7645391458f701eeec29.png) 
0%# Python - Async Comprehension
## Details
Master By: Emmanuel Turlay, Staff Software Engineer at Cruise Weight: 1Your score will be updated as you progress. ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240117%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240117T212649Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5cab37ae37e09c97923e86f333c6a4f3b8fd61e7762fd991433d6ce622c095d7) 

## Resources
Read or watch :
* [PEP 530 – Asynchronous Comprehensions](https://intranet.hbtn.io/rltoken/UFCR8qW3nHmEDZZaHqXL7Q) 

* [What’s New in Python: Asynchronous Comprehensions / Generators](https://intranet.hbtn.io/rltoken/PAGwxZUyVGBR8EMFGGNnGg) 

* [Type-hints for generators](https://intranet.hbtn.io/rltoken/SAxOMI925qJrJVGmZ0JBNw) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/7bPmbDGSheZBV1GZtaNBXg) 
 ,  without the help of Google :
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  ` python3 `  (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/env python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the  ` pycodestyle `  style (version 2.5.x)
* The length of your files will be tested using  ` wc ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your functions should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' ` 
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.
## Tasks
### 0. Async Generator
          mandatory         Progress vs Score  Task Body Write a coroutine called   ` async_generator `   that takes no arguments. 
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the   ` random `   module. 
```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]

```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` python_async_comprehension ` 
* File:  ` 0-async_generator.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Async Comprehensions
          mandatory         Progress vs Score  Task Body Import   ` async_generator `   from the previous task and then write a coroutine called   ` async_comprehension `   that takes no arguments. 
The coroutine will collect 10 random numbers using an async comprehensing over   ` async_generator `  , then return the 10 random numbers.
```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]


```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` python_async_comprehension ` 
* File:  ` 1-async_comprehension.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Run time for four parallel comprehensions
          mandatory         Progress vs Score  Task Body Import   ` async_comprehension `   from the previous file and write a   ` measure_runtime `   coroutine that will execute   ` async_comprehension `   four times in parallel using   ` asyncio.gather `  .
 ` measure_runtime `   should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135


```
 Task URLs  Technical information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` python_async_comprehension ` 
* File:  ` 2-measure_runtime.py ` 
 Self-paced manual review  Panel footer - Controls 
### Score
 ![Project badge](https://intranet.hbtn.io/assets/pathway/006_color-21d9dd12a952c0dcfa9471902c922dde2a053f71943f7645391458f701eeec29.png) 
0%Your score will be updated as you progress.
Please review  all the tasks  before you start the peer review.
Review all the tasks×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 18.04 - Python 3.7
Ubuntu 18.04 with Python 3.7
[Run]() 
×#### Recommended Sandboxes
[View User Containers (deprecated)](https://intranet.hbtn.io/user_containers/current) 
New sandbox * [US East (N. Virginia)	 - Ubuntu 22.04 LTS]() 

* [South America (São Paulo) - Ubuntu 22.04 LTS]() 

* [Europe (Paris) - Ubuntu 22.04 LTS]() 

* [Europe (Paris) - Cyber - WebSec 0x00]() 

* [Europe (Paris) - Cyber - NetSec 0x01]() 

* [Europe (Paris) - Cyber - NetSec 0x02]() 

* [Europe (Paris) - Cyber - NetSec 0x04]() 

* [Asia Pacific (Sydney) - Ubuntu 22.04 LTS]() 

No sandboxes yet![Previous project](https://intranet.hbtn.io/projects/2343) 
              Next project            
