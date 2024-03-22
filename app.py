import streamlit as st
import sqlite3
import random
import time
import subprocess


# Quiz data
quiz_data = [
    {
        'question': 'What is the purpose of a function in C?',
        'options': ['A. To print output', 'B. To perform a task', 'C. To declare variables', 'D. To comment code'],
        'correct_answer': 'B. To perform a task'
    },
    {
        'question': 'How is a function declared in C?',
        'options': ['A. def function_name()', 'B. function_name()', 'C. void function_name()', 'D. declare function_name()'],
        'correct_answer': 'C. void function_name()'
    },
    {
        'question': 'What is the return type of a function that does not return any value?',
        'options': ['A. int', 'B. void', 'C. char', 'D. double'],
        'correct_answer': 'B. void'
    },
    {
        'question': 'In C, can a function be called before its declaration?',
        'options': ['A. Yes', 'B. No', 'C. Only if it returns a value', 'D. Depends on the compiler'],
        'correct_answer': 'A. Yes'
    },
    {
        "question": "What is a function pointer in C?",
        "options": [
            "A. A pointer that stores the address of a function",
            "B. A pointer that points to another pointer",
            "C. A pointer used only in the main function",
            "D. A pointer that stores the value of a function",
        ],
        "correct_answer": "A. A pointer that stores the address of a function",
    },
    {
        "question": "What is recursion in the context of C functions?",
        "options": [
            "A. A function calling itself",
            "B. A function returning a constant value",
            "C. A function calling another function",
            "D. A function with multiple return statements",
        ],
        "correct_answer": "A. A function calling itself",
    },
    {
        "question": "What is the purpose of the 'volatile' keyword in C function declarations?",
        "options": [
            "A. To declare a variable with constant value",
            "B. To indicate that a variable's value may change anytime outside the program",
            "C. To declare a constant function",
            "D. To prevent the function from being modified",
        ],
        "correct_answer": "B. To indicate that a variable's value may change anytime outside the program",
    },
    {
        "question": "What is the difference between 'calloc' and 'malloc' in C?",
        "options": [
            "A. 'calloc' is used for allocating memory, and 'malloc' is used for deallocating memory",
            "B. 'calloc' initializes memory to zero, and 'malloc' does not",
            "C. 'calloc' is used for allocating memory, and 'malloc' is used for freeing memory",
            "D. 'calloc' is used for character arrays, and 'malloc' is used for integer arrays",
        ],
        "correct_answer": "B. 'calloc' initializes memory to zero, and 'malloc' does not",
    },
    {
        "question": "In C, how are arguments passed to functions by default?",
        "options": [
            "A. By reference",
            "B. By value",
            "C. By pointer",
            "D. By array",
        ],
        "correct_answer": "B. By value",
    },
    {
        "question": "What is the purpose of using 'const' in a function parameter?",
        "options": [
            "A. To declare a constant function",
            "B. To indicate the function does not modify the argument",
            "C. To allow modifying the argument inside the function",
            "D. To specify the data type of the argument",
        ],
        "correct_answer": "B. To indicate the function does not modify the argument",
    },
    {
        "question": "Which type of arguments are modified inside the called function?",
        "options": [
            "A. Output arguments",
            "B. Input arguments",
            "C. Return arguments",
            "D. Constant arguments",
        ],
        "correct_answer": "A. Output arguments",
    },
    {
        "question": "What is the role of the 'void' keyword in a function parameter list?",
        "options": [
            "A. To indicate an empty function",
            "B. To specify a function with no arguments",
            "C. To allow any data type for the function argument",
            "D. To indicate the function takes no arguments",
        ],
        "correct_answer": "D. To indicate the function takes no arguments",
    },
]
def live_execution():
    st.title("C Functions Live Code Execution")

    # Display C code editor
    code = st.text_area("Enter your C code:", value="", height=300)
    run_button = st.button("Run Code")

    if run_button:
        # Write the code to a temporary file
        with open("temp.c", "w") as f:
            f.write(code)

        # Compile and execute the C program
        try:
            compilation_output = subprocess.check_output(["gcc", "temp.c", "-o", "temp"], stderr=subprocess.STDOUT)
            if compilation_output:
                st.error("Compilation Error:\n" + compilation_output.decode())
            else:
                execution_output = subprocess.check_output(["./temp"], stderr=subprocess.STDOUT)
                st.success("Code executed successfully!")
                st.write("Output:")
                st.code(execution_output.decode(), language="text")
        except subprocess.CalledProcessError as e:
            st.error("Execution Error:\n" + e.output.decode())
        except Exception as e:
            st.error("Error:\n" + str(e))



def poutput():
    st.title("Find the Output: Functions in C")
    st.write("HINT: Try to run these codes in live execution page")

    # Display the first C code snippet
    code_snippet_1 = """
    #include<stdio.h>

    void fun(char*);
    
    int main()
    {
        char a[100];
        a[0] = 'A'; a[1] = 'B';
        a[2] = 'C'; a[3] = 'D';
        fun(&a[0]);
        return 0;
    }
    
    void fun(char *a)
    {
        a++;
        printf("%c", *a);
        a++;
        printf("%c", *a);
    }
    """
    
    # Display the second C code snippet
    code_snippet_2 = """
    #include<stdio.h>

    void fun(int);
    typedef int (*pf) (int, int);
    int proc(pf, int, int);
    
    int main()
    {
        int a=3;
        fun(a);
        return 0;
    }
    
    void fun(int n)
    {
        if(n > 0)
        {
            fun(--n);
            printf("%d,", n);
            fun(--n);
        }
    }
    """
    code_snippet_3 = """
    #include <stdio.h>
 
void fun(int arr[], unsigned int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
}
 
// Driver program
int main()
{
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
    unsigned int n = sizeof(arr) / sizeof(arr[0]);
    fun(arr, n);
    return 0;
}
    """

    

    # Display the first C code snippet and prompt user for input
    st.header("Question 1:")
    st.code(code_snippet_1, language="c")
    user_answer_1 = st.text_input("Enter your answer for Question 1:")

    # Check user input for Question 1 and provide feedback
    if user_answer_1:
        correct_answer_1 = "BC"
        if user_answer_1.strip() == correct_answer_1:
            st.success("Congratulations! Your answer for Question 1 is correct.")
        else:
            st.error("Sorry, your answer for Question 1 is incorrect.")
            st.write("Try to run the code in live execution page")
            st.write("""Explanation for Question 1: In the main() function, an array a of characters is declared and initialized with the values 'A', 'B', 'C', 'D'. Then, the function fun() is called with the address of the first element of the array a.

Now, let's look at the fun() function:

Inside fun(), the pointer a is incremented once (a++), so it now points to the second element of the array a.
The value at the memory location pointed to by a is printed (printf("%c", *a)), which is 'B'.
Then, a is incremented again (a++), so it now points to the third element of the array a.
The value at the memory location pointed to by a is printed (printf("%c", *a)), which is 'C'.
Therefore, the output of the code will be BC. It prints the characters 'B' followed by 'C'.""")

    # Display the second C code snippet and prompt user for input
    st.header("Question 2:")
    st.code(code_snippet_2, language="c")
    user_answer_2 = st.text_input("Enter your answer for Question 2:")

    # Check user input for Question 2 and provide feedback
    if user_answer_2:
        correct_answer_2 = "0,1,2,0,"
        if user_answer_2.strip() == correct_answer_2:
            st.success("Congratulations! Your answer for Question 2 is correct.")
        else:
            st.error("Sorry, your answer for Question 2 is incorrect.")
            st.write("Try to run the code in live execution page")
            st.write("""Explanation for Question 2: This C code snippet defines a function fun that takes an integer n as an argument. In the main() function, fun is called with the argument a, which is initialized to 3. Let's analyze the function fun:The fun function recursively calls itself twice with decremented values of n, printing the value of n each time before the recursive call. It continues to call itself recursively until n becomes less than or equal to 0.

Let's trace the execution with n = 3:

fun(3) is called.
fun(2) is called.
fun(1) is called.
fun(0) is called.
printf("%d,", n); is executed, printing 0,.
The recursion starts unwinding.
printf("%d,", n); is executed again, printing 1,.
fun(-1) is called, but since n is not greater than 0, the function returns without further recursive calls.
So, the output of the code will be 0,1,. It prints 0, followed by 1,""")

    st.header("Question 3:")
    st.code(code_snippet_3, language="c")
    user_answer_3 = st.text_input("Enter your answer for Question 3:")

    # Check user input for Question 2 and provide feedback
    if user_answer_3:
        correct_answer_3 = "1 2 3 4 5 6 7 8"
        if user_answer_3.strip() == correct_answer_3:
            st.success("Congratulations! Your answer for Question 3 is correct.")
        else:
            st.error("Sorry, your answer for Question 3 is incorrect.")
            st.write("Try to run the code in live execution page")
            st.write("""Explanation for Question 3:In the main() function:

An array arr of integers is declared and initialized with values {1, 2, 3, 4, 5, 6, 7, 8}.
The variable n is assigned the size of the array arr divided by the size of arr[0], which gives the number of elements in the array.
The function fun() is called with the array arr and the number of elements n.
The fun() function takes an array arr[] and the number of elements n as parameters.
It simply prints all elements of the array arr[] using a loop.""")





def run_chat():
    # Streamed response emulator
    def response_generator():
        response = random.choice([
        	"C functions are reusable blocks of code that perform a specific task.",
    "A function in C can have parameters, allowing data to be passed into it.",
    "The return type of a function in C specifies the type of value the function returns.",
    "Function prototypes in C declare the function's existence and signature before its implementation.",
    "Recursive functions in C are functions that call themselves.",
    "Function pointers in C allow you to store and call functions dynamically.",
    "The main() function in C is the entry point for program execution.",
    "A function definition in C consists of a function header and a function body.",
    "The void keyword is used as the return type when a function does not return a value.",
    "Function overloading is not supported in C as it is in some other programming languages."
            "C is a high-level programming language.",
            "In C, functions are the building blocks of programs.",
            "C provides a wide range of data types including int, float, char, etc.",
            "Pointers are a powerful feature in C.",
            "Arrays in C allow you to store multiple elements of the same type.",
            "C supports control structures like if-else, loops, and switch-case.",
            "C programming involves memory management.",
            "C is often used for system programming and developing operating systems.",
            "Learning C can be a great foundation for understanding computer architecture."
            
        ])
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    st.title("FUN FACT BOT :robot_face:")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Do you want a fun fact?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
            st.session_state.messages.append({"role": "assistant", "content": response})
            
def quiz():
    st.title("Challenging C Programming Quiz")

    # Display difficult quiz questions
    user_answers = []
    for idx, question_data in enumerate(quiz_data, start=1):
        st.write(f"**Question {idx}:** {question_data['question']}")
        user_answer = st.radio("Select your answer:", question_data["options"], key=f"question_{idx}")
        user_answers.append(user_answer)

        if st.button(f"Submit Answer for Question {idx}"):
            st.success("Answer submitted!")

    # Display final score
    st.title("Quiz Completed! Here's Your Score:")
    correct_answers = [q["correct_answer"] for q in quiz_data]
    score = sum(user_answer == correct_answer for user_answer, correct_answer in zip(user_answers, correct_answers))
    total_questions = len(quiz_data)
    st.write(f"You scored {score} out of {total_questions}!")



# Create a connection to the SQLite database
conn = sqlite3.connect('user_credentials.db')
c = conn.cursor()

# Create a table to store user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

def create_user(username, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def verify_user(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return c.fetchone() is not None

def puzzles_page():
    st.title("Puzzles Page")
    st.write("Welcome to the puzzles page, {}! Here you can solve puzzles and take quizzes.".format(st.session_state.username))
    
    quiz_options = ["What do you want to do?", "Take Quiz","Predict the output"]
    selected_option = st.selectbox("Select an option:", quiz_options)

    if selected_option == "Take Quiz":
        quiz()
    if selected_option == "Predict the output":
    	poutput()

    
def main():
    st.set_page_config(page_title="FUN WITH FUNCTIONS", page_icon=":rocket:", layout='wide')
    # Set page title
    st.title("FUN WITH FUNCTIONS")
    st.markdown('<style>h1{color: #F0F8FF; text-align: center;}</style>', unsafe_allow_html=True)

    if "username" not in st.session_state:
        st.session_state.username = ""
        st.session_state.logged_in = False

    menu = ["Login", "SignUp", "Puzzles","Fun fact bot","Live Code Execution", "Resources", "Logout"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Login":
        st.subheader("Login Section")
        header_bg = """
        <style>
        .stApp {
            background-image: url('https://t4.ftcdn.net/jpg/06/47/15/51/360_F_647155146_MAlTNNAP8iJTWxw42vwaBkId5XdeE957.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
        </style>
        """
        st.markdown(header_bg, unsafe_allow_html=True)
        
        username = st.text_input("Username", value=st.session_state.username)
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if verify_user(username, password):
                st.success(f":tada: Logged In as {username} :tada:")
                st.session_state.username = username
                st.session_state.logged_in = True
            else:
                st.error(":x: Invalid Username or Password :x:")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        # Adding background image to the sign-up page
        header_bg = """
        <style>
        .stApp {
            background-image: url('https://www.shutterstock.com/image-photo/closeup-shot-female-engineer-working-600nw-669226057.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
        </style>
        """
        st.markdown(header_bg, unsafe_allow_html=True)
        
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        if st.button("Sign Up"):
            if new_password == confirm_password:
                create_user(new_username, new_password)
                st.success(":heavy_check_mark: Account created successfully! You can now login. :heavy_check_mark:")
            else:
                st.error(":x: Passwords do not match. Please try again. :x:")

    elif choice == "Puzzles":
        
        if st.session_state.logged_in:
            puzzles_page()
        else:
            st.error(":x: Please login to access this feature. :x:")

            
    elif choice=="Live Code Execution":
        if st.session_state.logged_in:
            live_execution()
        else:
            st.error("""You can use this to check the output for the puzzles question\n
                     :x: Please login to access this feature. :x:""")
            
    elif choice == "Fun fact bot":
    	run_chat()

    elif choice == "Resources":
        st.title(":books: Resources :books:")
        # Adding background image to the resources page
        header_bg = """
        <style>
        .stApp {
            background-image: url('https://res.cloudinary.com/dlpitjizv/image/upload/v1685725458/impact/20220610_Impact_Blog_What_does_IT_do_hero_bd7eb9cdc6.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
        </style>
        """
        st.markdown(header_bg, unsafe_allow_html=True)
        
        subtopics = ["Cheatsheets", "University Notes", "YouTube Links", "Coding Platform Links"]
        subtopic_choice = st.radio("Select Subtopic", subtopics)

        if subtopic_choice == "Cheatsheets":
            st.title("Cheatsheets")
            st.markdown("Here are some useful cheatsheets:",unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.codewithharry.com/blogpost/c-cheatsheet/'>C Cheatsheet by CodeWithHarry</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.geeksforgeeks.org/c-cheatsheet/'>C Cheatsheet by GeeksforGeeks</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.codecademy.com/learn/learn-c/modules/functions-c/cheatsheet'>Functions in C Cheatsheet by Codecademy</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://quickref.me/c.html#c-function'>C Function Cheatsheet by QuickRef</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://studyopedia.com/c/c-programming-cheat-sheet/#'>C Programming Cheat Sheet by Studyopedia</a>", unsafe_allow_html=True)
            st.markdown("\n", unsafe_allow_html=True)
            
            # Adding background image to the cheatsheets page
            header_bg = """
            <style>
            .stApp {
                background-image: url('https://st3.depositphotos.com/2572561/16360/i/450/depositphotos_163607298-stock-photo-close-up-shot-of-female.jpg');
                background-size: cover;
                background-repeat: no-repeat;
            }
            </style>
            """
            st.markdown(header_bg, unsafe_allow_html=True)

        elif subtopic_choice == "University Notes":
            st.title("University Notes")
            st.markdown("Here are some university notes on functions in C:", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://cs50.harvard.edu/x/2023/notes/1/#functions'>CS50 Harvard University Notes</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://web.stanford.edu/class/archive/cs/cs103/cs103.1156/lectures/09/Small09.pdf'>Stanford University Notes 1</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1172/lectures/2-Functions/2-Functions.pdf'>Stanford University Notes 2</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='http://cse.iitkgp.ac.in/~spp/pds/Lec-4-Functions.pdf'>IIT Kharagpur Notes</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='http://iitk.ac.in/esc101/2011Jan/Lectures/lect16.pdf'>IIT Kanpur Notes</a>", unsafe_allow_html=True)
            st.markdown("\n", unsafe_allow_html=True)
            # Add university notes links here
            # Adding background image to the university page

        elif subtopic_choice == "YouTube Links":
            st.title("YouTube Links")
            st.write("Here are some YouTube videos on functions in C:")
            st.markdown("- <a style='color:white' href='https://www.youtube.com/watch?v=f--fD8Y0RnA'>Introduction to Functions in C</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.youtube.com/watch?v=3lqgdqoY83o'>Functions and Prototypes in C</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.youtube.com/watch?v=K4MA1Hkwj0s'>Function Calls in C Programming</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.youtube.com/watch?v=Ix578mIRZv4'>C Programming Tutorial - Functions</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.youtube.com/watch?v=Npo1u37lcg8'>C Functions - Programming in C</a>", unsafe_allow_html=True)
            st.markdown("\n", unsafe_allow_html=True)
            # Add YouTube links here

        elif subtopic_choice == "Coding Platform Links":
            st.title("Coding Platform Links")
            st.markdown("Here are some coding platform links related to functions in C:", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.w3resource.com/c-programming-exercises/function/index.php'>C Programming Exercises on w3resource</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://codeforwin.org/c-programming/functions-programming-exercises-and-solutions-in-c'>Functions Programming Exercises and Solutions on Codeforwin</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.geeksforgeeks.org/c-functions/?ref=shm'>C Functions on GeeksforGeeks</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://codersdaily.in/courses/hackerrank-c-solution/functions-in-c-solution'>HackerRank C Solution - Functions in C</a>", unsafe_allow_html=True)
            st.markdown("- <a style='color:white' href='https://www.hackerrank.com/challenges/functions-in-c/problem'>HackerRank - Functions in C Problem</a>", unsafe_allow_html=True)
            st.markdown("\n", unsafe_allow_html=True)
            # Add coding platform links here

    elif choice == "Logout":
        st.session_state.username = ""
        st.session_state.logged_in = False
        st.title("Thank you for using our app! You have been successfully logged out.")

    # Adding background image to the header
    header_bg = """
    <style>
    .stApp {

        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """
    #        background-image: url('https://media.istockphoto.com/id/157639696/photo/purple-space-stars.jpg?s=612x612&w=0&k=20&c=fkLtGZxUS9UPlLJUTeGjvvURT0u-vtxvj5sAYbDNrH4=');
    st.markdown(header_bg, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

