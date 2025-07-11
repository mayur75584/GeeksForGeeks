'''

Code Gladiators Coding Contest

World Army vs Aliens (100 Marks)

The world is going to be attacked by the aliens. The space intelligence department has raised an alarm and the world armies are coming together to fight them. The planning and strategizing is being done to make the maximum impact on the alien ships. The deadly missiles are to be put into action. The missiles are targeted to destroy the alien ships in space and disable them to land on the Earth.

The army is planning to launch the attack at A time (hh mm) to get an advantage. For each attack, they know the time the missile will require to hit the coming alien ship. They all are busy in preparation and want to know the time at which the blast will occur and the alien ship will be destroyed in pieces. Can you find the time of the blast ?

Note: The World Army follows a 24-hour time format and you need to find the time of blast accordingly. The time will be in the hh mm format.

Example:



Input Format

The first line of input consists of the launch time in hh mm format separated by space.

The second line of input consists of the travel time for the missile in hh mm format separated by space.


Constraints

00<= hh <=23

00<= mm <=59


Output Format
Print the time at which the blast will occur and the spaceship will be destroyed.

Sample TestCase 1
Input
19 50
02 20
Output
22 10

Time Limit(X):
    0.50 sec(s) for each input.
Memory Limit:
    512 MB
Source Limit:
    100 KB
Allowed Languages:
    C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''

def func(lt,tt):
    h1,m1=lt.split()
    h2,m2=tt.split()
    h3=(int(h1)+int(h2)+(int(m1)+int(m2))//60)%24
    m3=(int(m1)+int(m2))%60
    if len(str(h3))==1:
        h3='0'+str(h3)
    if len(str(m3))==1:
        m3='0'+str(m3)
    return str(h3)+' '+str(m3)

if __name__ == '__main__':
    lt=input()
    tt=input()
    # lt='19 50'
    # tt='02 20'
    # lt='19 50'
    # tt='04 20'
    res=func(lt,tt)
    print(res)