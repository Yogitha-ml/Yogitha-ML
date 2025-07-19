#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello')


# In[2]:


a=10


# In[3]:


a


# In[4]:


a+a


# In[7]:


h="hello"


# In[8]:


len(h)


# In[9]:


type(h)


# In[10]:


len(' cc papa')


# In[14]:


myword="hello world"


# In[15]:


myword


# In[16]:


myword[0]


# In[20]:


letter = 'z'


# In[21]:


letter * 10


# In[22]:


x='uppeer'


# In[23]:


x.upper()


# In[25]:


print('this is a string {}'.format('INSERTED'))


# In[26]:


result=157/354


# In[27]:


result


# In[32]:


print('the result is {r:1.3}'.format(r=result))


# In[34]:


print(f'hello the result is {result}')


# In[35]:


name = "cc"
age = 2


# In[36]:


print(f"{name} is {age} years old now.")


# In[43]:


print("Python {}"".format'rules!'))


# In[1]:


set('parallel')


# In[2]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'hello this is a text file')


# In[4]:


myfile = open('myfile.txt')


# In[5]:


pwd


# In[12]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'hello this is a text file\nthis is a 2nd file\nthis is a 3rd file')


# In[14]:


myfile=open('myfile.txt')


# In[15]:


myfile.read()


# In[16]:


myfile.read()


# In[17]:


myfile.seek(0)


# In[22]:


myfile.read()


# In[23]:


myfile.seek(0)


# In[33]:


myfile.readlines()


# In[27]:


with open('myfile.txt',mode = 'r')as myfile:
    myfile.txt = myfile.read()


# In[28]:


get_ipython().run_cell_magic('writefile', 'my_nf.txt', 'one on\ntwo on\nthree on')


# In[29]:


with open('my_nf.txt',mode='r') as f:
    print(f.read())


# In[30]:


with open('my_nf.txt',mode='a')as f:
    f.write('fourth on')


# In[31]:


with open('my_nf.txt',mode='r') as f:
    print(f.read())


# In[34]:


with open('aaa.txt',mode='w') as f:
    f.write('this is mine')


# In[35]:


with open('aaa.txt',mode='r') as f:
    print(f.read())


# In[36]:


# test#




# In[44]:


2*5+50.2/2*(2**3)-110.55


# In[45]:


4*(6+5)


# In[46]:


4*6+5


# In[47]:


3+1.5+4


# In[48]:


type(8.5)


# In[50]:


import math
math.sqrt(12)


# In[51]:


s='hello'


# In[52]:


s[1]


# In[53]:


s[::-1]


# In[54]:


a=[0,0,0]


# In[55]:


a.append(0)


# In[56]:


a


# In[64]:


list1=[1,2,[3,4,'hello']]


# In[65]:


list1.pop()


# In[66]:


list1


# In[68]:


list1.append([3,4,'goodbye'])


# In[69]:


list1


# In[70]:


l4=[5,3,4,6,1]


# In[71]:


l4.sort()


# In[72]:


l4


# In[73]:


d={'simple_key':'hello'}


# In[75]:


d.values()


# In[76]:


d1={'k1':{'k2':'hello'}}


# In[96]:


d1['k1']['k2']


# In[97]:


d2={'k1':[{'nested_key':['this is deep',['hello']]}]}


# In[102]:


d2['k1'][0]['nested_key'][1]


# In[103]:


d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# In[114]:


d['k1'][2]['k2'][1]['tough'][2][0]


# In[115]:


list5=[1,2,2,33,4,4,11,11,3,3,4,4]


# In[116]:


set(list5)


# In[117]:


2>3


# In[118]:


3<=2


# In[119]:


3==2.0


# In[120]:


4**0.5 != 2


# In[121]:


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]


# In[122]:


l_one[2][0] >= l_two[2]['k1']


# In[123]:


# for loops



# In[126]:


hungry = False
if hungry:
    print('Feed me!')
else:
    print('im not hungry')


# In[130]:


loc = 'Bank'

if loc == 'Bank':
    print('in there')
elif loc == 'Street':
    print('turn right')
else:
    print('welcome')


# In[131]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[134]:


for num in mylist:
    print(num)


# In[138]:


for num in mylist:
    if num%2==0:
        print(num)
    else:
        print(f'odd number:{num}')


# In[141]:


list_sum=0

for num in mylist:
    list_sum=list_sum+num
print(list_sum)


# In[ ]:





# In[9]:


mystring='sammy'
for letter in mystring:
    if letter=='a':
        continue
    print(letter)


# In[10]:


mystring='sammy'
for letter in mystring:
    if letter=='a':
        break
    print(letter)


# In[11]:


x=[1,2,3]


# In[12]:


for items in x:
    pass
print('end of script')


# In[1]:


x=0
while x<5:
    print(x)
    x+=1


# In[2]:


x=0

while x<5:
    if x == 2:
        break
    print(x)
    x+=1


# In[3]:


mylist=[1,2,3]


# In[5]:


for num in range(1,10,2):
    print(num)


# In[6]:


list(range(0,11,2))


# In[7]:


index_count=0
for letter in 'abcde':
    print('at index{} the letter is{}'.format(index_count,letter))
    index_count +=1


# In[8]:


index_count=0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count +=1


# In[10]:


word='abcde'
for item in enumerate(word):
    print(item)


# In[11]:


word='abcde'
for letter,index in enumerate(word):
    print(letter)
    print(index)
    print('\n')


# In[20]:


names=['sammy','sandra','cc']


# In[21]:


names


# In[ ]:


for words in names:
    names.append(word)


# In[ ]:


names


# In[6]:


st='S print only words that starts with letter s in statement '


# In[7]:


for word in st.split():
    if word[0]=='s':
        print(word)
        #less code and easy


# In[8]:


for word in st.split():
    if word[0]=='s' or word[0]=='S':
        print(word)


# In[9]:


mynum=range(1,10)


# In[10]:


mynum


# In[12]:


t1=range(0,10,2)


# In[13]:


t1


# In[15]:


list(range(0,11,2))


# In[16]:


for num in range(0,11,2):
    print(num)


# In[19]:


mylist=[x for x in range(1,51) if x%3==0]


# In[20]:


mylist


# In[21]:


st = 'Print every word in this sentence that has an even number of letters'


# In[30]:


for word in st.split():
    if len(word)%2==0:
        print(word +  'is even')


# In[31]:


for num in range(1,101):
    if num%3==0 and num%5==0:
        print('Fizzbuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0:
        print('buzz')
    else:
        print(num)
    


# In[35]:


st = 'Create a list of the first letters of every word in this string'


# In[39]:


mylist=[word[0] for word in st.split()]


# In[40]:


mylist


# In[41]:


#### functions



def myfunc(num1,num2):
    return(num1+num2)


# In[44]:


result=myfunc(10,20)


# In[45]:


result


# In[51]:


def say_hello():
    print('hi')
    return('hi')


# In[52]:


r1=say_hello()


# # 

# In[53]:


r1


# In[54]:


type(r1)


# In[61]:


def say_hello(name):
    print(f'hello {name}')


# In[62]:


say_hello('cc')


# In[65]:


def even_check(num):
    result=num%2==0
    return result


# In[66]:


even_check(35)


# In[67]:


# return true if any num is list is even


# In[74]:


def check_even_list(num_list):
    for num in num_list:
        if num%2==0:
            return True
        else:
            pass
    return False


# In[72]:


check_even_list([1,2,3,5])


# In[75]:


def check_even_list(num_list):
    even_numb=[]
    for num in num_list:
        if num%2==0:
            even_numb.append(num)
        else:
            pass
    return even_numb


# In[77]:


check_even_list([1,2,3,5,8,6])


# In[78]:


stock_prices=[('apl',200),('gog',400),('msf',100)]


# In[79]:


for item in stock_prices:
    print(item)


# In[81]:


for company,price in stock_prices:
    print(price+(0.1*price))
    


# In[97]:


work_hours=[('abby',100),('billy',300),('cc',600)]


# In[98]:


def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)


# In[93]:


employee_check(work_hours)


# In[111]:


######### CREATE GAME   ################


# In[1]:


from random import shuffle


# In[2]:


mylist=['','O','']


# In[3]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[4]:


mylist


# In[5]:


shuffle_list(mylist)


# In[6]:


def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("pick a num: 0,1, or 2:")
    return int(guess)


# In[7]:


player_guess()


# In[8]:


def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("correct guess!")
    else:
        print("wrong better luck nxt tym")
        print(mylist)


# In[9]:


mylist=['','O','']
mixedup_list=shuffle_list(mylist)
guess=player_guess
check_guess(mixedup_list,guess)


# In[11]:


mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)


# In[18]:


def lesser_of_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            result = a
        else:
            result = b
    else:
        if a>b:
            result = a
        else:
            result = b
    return result


# In[20]:


lesser_of_evens(10,25)


# In[21]:


def nums_even(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)


# In[25]:


nums_even(118,20)


# In[36]:


def check_letters(string):
    words=string.split()
    if words[0][0]==words[1][0]:
        return True
    else:
        return False


# In[38]:


check_letters('Letterhead Ama')


# In[39]:


def check_letters(string):
    words=string.lower().split()
    return words[0][0]==words[1][0]


# In[40]:


check_letters('Letterhead lma')


# In[61]:


def makes_twenty(n1,n2):
    if n1+n2==20:
        return True
    
        if n1==20 or n2==20:
            return True
        else:
            return False
    else:
        return False
            
        


# In[62]:


makes_twenty(2,3)


# In[63]:


def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20


# In[64]:


makes_twenty(2,3)


# In[73]:


def cap_word(name):
    name1=name[:2]
    name2=name[2:]
    return name1.capitalize()+name2.capitalize()
    


# In[74]:


cap_word('mcdonalds')


# In[83]:


def master_yodha(text):
    wordlist = text.split()
    rev_words = wordlist[::-1]
    return ' '.join(rev_words)


# In[84]:


master_yodha('I am home')


# In[ ]:




