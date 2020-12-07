
// CPP program to demonstrate multithreading
// using three different callables.
#include <iostream>
#include <thread>
using namespace std;

// A dummy function
void foo(int Z)
{
    for (int i = 0; i < Z; i++) {
        cout << "Thread using function"
                "pointer as callable"<<i<<"\n";
    }
}

// A callable object
class thread_obj {
public:
    void operator()(int x)
    {
        for (int i = 0; i < x; i++)
            cout << "Thread using function"
                    "object as  callable"<<i<<"\n";
    }
};

int main(int argc, char** argv)
{
    cout << "Threads 1 and 2 and 3 "
         "operating independently" << endl;

    // This thread is launched by using
    // function pointer as callable
    int Duration = atoi(argv[1]);
    thread th1(foo, Duration);
    th1.detach();
    // This thread is launched by using
    // function object as callable
    thread th2(thread_obj(), Duration);
    th2.detach();
    // Define a Lambda Expression
    auto f = [](int x) {
        for (int i = 0; i < x; i++)
            cout << "Thread using lambda  "
                    "express as callable"<<i<<"\n";
    };

    // This thread is launched by using
    // lamda expression as callable
    thread th3(f, Duration);
    th3.detach();
    // Wait for the threads to finish
    // Wait for thread t1 to finish


    // Wait for thread t2 to finish


    // Wait for thread t3 to finish

    cin>>Duration;
    return 0;
}
