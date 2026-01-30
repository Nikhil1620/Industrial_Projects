///////////////////////////////////////////////////
//      Generalised Data Structure Library
///////////////////////////////////////////////////

/*
---------------------------------------------------------------------------------------
Type                    Name of class for node      Name of class for Functionality
---------------------------------------------------------------------------------------
Singly Linear            SinglyLLLnode               SinglyLLL          Done
Singly Cirular           SinglyCLLnode               SinglyCLL          Done
Doubly Linear            DoublyLLLnode               DoublyLLL          Done
Doubly Circular          DoublyCLLnode               DoublyCLL          Done
Stack                    Stacknode                   Stack              Done
Queue                    Queuenode                   Queue              Done
---------------------------------------------------------------------------------------
*/

#include<iostream>
using namespace std;

///////////////////////////////////////////////////////////////////////
//          Singly Linear LinlkedList using Generic Approach
///////////////////////////////////////////////////////////////////////

#pragma pack(1)
template<class T>
class SinglyLLLnode
{
    public:
        T data;
        SinglyLLLnode<T> *next;

        SinglyLLLnode(T no)
        {
            this->data = no;
            this->next = NULL;
        }
};

template<class T>
class SinglyLLL
{
    private:        
        SinglyLLLnode<T> * first;
        int iCount;

    public:
        SinglyLLL();
        void InsertFirst(T);
        void InsertLast(T);
        void DeleteFirst();
        void DeleteLast();
        void Display();
        int Count();
        void InsertAtPos(T,int);
        void DeleteAtPos(int);
};

template<class T>
SinglyLLL<T> :: SinglyLLL()
{
    cout<<"Object of SinglyLL gets created.\n";
    this->first = NULL;
    this->iCount = 0;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     InsertFirst
//  Input :             Data of node
//  Output :            Nothing
//  Description :       Used to insert node at first position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> :: InsertFirst(T no)
{
    SinglyLLLnode<T> * newn = NULL;

    newn = new SinglyLLLnode<T>(no);

    newn->next = this->first;
    this->first = newn;

    this->iCount++;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     InsertLast
//  Input :             Data of node
//  Output :            Nothing
//  Description :       Used to insert node at last position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::InsertLast(T no)
{
    SinglyLLLnode<T> * newn = NULL;
    SinglyLLLnode<T> * temp = NULL;

    newn = new SinglyLLLnode<T>(no);

    if(this->iCount == 0)
    {
        this->first = newn;
    }
    else
    {
        temp = this->first;

        while(temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
    }
    this->iCount++;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     DeleteFirst
//  Input :             Data of node
//  Output :            Nothing
//  Description :       Used to delete node at first position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::DeleteFirst()
{
    SinglyLLLnode<T> * temp = NULL;

    if(this->first == NULL)
    {
        return;
    }
    else if(this->first->next == NULL)
    {
        delete this->first;
        this->first = NULL;
    }
    else
    {
        temp = this->first;

        this->first = this->first -> next;
        delete temp;
    }

    this->iCount--;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     DeleteLast
//  Input :             Data of node
//  Output :            Nothing
//  Description :       Used to delete node at last position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::DeleteLast()
{
    SinglyLLLnode<T> * temp = NULL;

    if(this->first == NULL)
    {
        return;
    }
    else if(this->first->next == NULL)  
    {
        delete this->first;
        this->first = NULL;
    }
    else
    {
        temp = this->first;

        while(temp->next->next != NULL)
        {
            temp = temp -> next;
        }

        delete temp->next;
        temp->next = NULL;

    }
    this->iCount--;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     Display
//  Input :             Nodes
//  Output :            Nothing
//  Description :       Used to Display each node in the linked list
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::Display()
{
    SinglyLLLnode<T> * temp = NULL;
    int iCnt = 0;

    temp = this->first;

    for(iCnt = 1; iCnt <= this->iCount; iCnt++)
    {
        cout<<"| "<<temp->data<<" |-> ";
        temp = temp->next;
    }

    cout<<"NULL\n";
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     Count
//  Input :             Nodes
//  Output :            Integer
//  Description :       Used to count the nodes in the given Linked list
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
int SinglyLLL<T> ::Count()
{
    return this->iCount;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     InsertAtPos
//  Input :             Data of node and Position
//  Output :            Nothing
//  Description :       Used to insert node at given position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::InsertAtPos(T no, int pos)
{
    SinglyLLLnode<T> * temp = NULL;
    SinglyLLLnode<T> * newn = NULL;

    int iCnt = 0;

    if(pos < 1 || pos > this->iCount + 1)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        this->InsertFirst(no);
    }
    else if(pos == this->iCount+1)
    {
        this->InsertLast(no);
    }
    else
    {
        newn = new SinglyLLLnode<T>(no);

        temp = this->first;
        
        for(iCnt = 1; iCnt < pos-1; iCnt++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next = newn;

        this->iCount++;
    }
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     DeleteAtPos
//  Input :             Position
//  Output :            Nothing
//  Description :       Used to delete node at given position
//  Author :            Nikhil Ramesh Ahire
//  Date :              06/01/2026
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void SinglyLLL<T> ::DeleteAtPos(int pos)
{
    SinglyLLLnode<T> * temp = NULL;
    SinglyLLLnode<T> * target = NULL;

    int iCnt = 0;

    if(pos < 1 || pos > this->iCount)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        this->DeleteFirst();
    }
    else if(pos == this->iCount)
    {
        this->DeleteLast();
    }
    else
    {
        temp = this->first;
        
        for(iCnt = 1; iCnt < pos-1; iCnt++)
        {
            temp = temp->next;
        }

        target = temp->next;

        temp->next = target->next;
        delete target;

        this->iCount--;
    }
}

///////////////////////////////////////////////////////////////////////
//          Doubly Linear LinlkedList using Generic Approach
///////////////////////////////////////////////////////////////////////

#pragma pack(1)
template<class T>
class DoublyLLLnode
{
    public:
        T data;
        DoublyLLLnode *next;
        DoublyLLLnode *prev;

        DoublyLLLnode(T no)
        {
            this->data = no;
            this->next = NULL;
            this->prev = NULL;
        }
};

template<class T>
class DoublyLLL
{
    private:
        DoublyLLLnode<T> * first;
        int iCount;

    public:
        DoublyLLL();

        void InsertFirst(T);
        void InsertLast(T);
        void InsertAtPos(T,int);

        void DeleteFirst();
        void DeleteLast();
        void DeleteAtPos(int);

        void Display();
        int Count();
};

template<class T>
DoublyLLL<T> :: DoublyLLL()
{
    cout<<"Linked List gets created\n";

    this->first = NULL;
    this->iCount = 0;
}

template<class T>
void DoublyLLL<T> ::InsertFirst(T no)
{
    DoublyLLLnode<T> *newn = NULL;
    
    newn = new DoublyLLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
    }
    else
    {
        newn->next = this->first;
        this->first->prev = newn;
        this->first = newn;
    }
    this->iCount++;
}

template<class T>
void DoublyLLL<T> ::InsertLast(T no) 
{
    DoublyLLLnode<T> *newn = NULL;
    DoublyLLLnode<T> *temp = NULL;

    newn = new DoublyLLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
    }
    else
    {
        temp = this->first;
        
        while(temp->next != NULL)
        {
            temp = temp->next;
        }

        temp->next = newn;
        newn->prev = temp;
    }
    this->iCount++;    
}

template<class T>
void DoublyLLL<T> ::InsertAtPos(T no,int pos)
{
    DoublyLLLnode<T> *temp = NULL;
    DoublyLLLnode<T> *newn = NULL;

    int iCnt = 0;

    if((pos < 1) || (pos > this->iCount+1))
    {
        cout<<"Invalid position\n";
        return;
    }  

    if(pos == 1)
    {
        this->InsertFirst(no);
    }
    else if(pos == this->iCount+1)
    {
        this->InsertLast(no);
    }
    else
    {
        newn = new DoublyLLLnode<T>(no);

        temp = this->first;

        for(iCnt = 1; iCnt < pos-1; iCnt++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next->prev = newn;

        temp->next = newn;
        newn->prev = temp;

        this->iCount++;
    }
}

template<class T>
void DoublyLLL<T> ::DeleteFirst()
{
    if(this->first == NULL)                 // LL is empty
    {
        return;
    }
    else if(this->first->next == NULL)      // LL contains 1 node
    {
        delete this->first;
        this->first = NULL;
    }
    else                                    // LL contains more than 1 node
    {
        this->first = this->first->next;
        delete this->first->prev;
        this->first->prev = NULL;
    }

    this->iCount--;
}

template<class T>
void DoublyLLL<T> ::DeleteLast()
{
    DoublyLLLnode<T> *temp = NULL;

    if(this->first == NULL)                 // LL is empty
    {
        return;
    }
    else if(this->first->next == NULL)      // LL contains 1 node
    {
        delete this->first;
        this->first = NULL;
    }
    else                                    // LL contains more than 1 node
    {
        temp = this->first;

        while(temp->next->next != NULL)
        {
            temp = temp->next;
        }

        delete temp->next;
        temp->next = NULL;
    }

    this->iCount--;    
}

template<class T>
void DoublyLLL<T> ::DeleteAtPos(int pos)
{
    DoublyLLLnode<T> *temp = NULL;
    int iCnt = 0;

    if((pos < 1) || (pos > this->iCount))
    {
        cout<<"Invalid position\n";
        return;
    }  

    if(pos == 1)
    {
        this->DeleteFirst();
    }
    else if(pos == this->iCount)
    {
        this->DeleteLast();
    }
    else
    {
        temp = this->first;

        for(iCnt = 1; iCnt < pos-1; iCnt++)
        {
            temp = temp->next;
        }

        temp->next = temp->next->next;
        delete temp->next->prev;
        temp->next->prev = temp;

        this->iCount--;
    }    
}

template<class T>
void DoublyLLL<T> ::Display()
{
    DoublyLLLnode<T> *temp = NULL;
    
    temp = this->first;

    cout<<"\nNULL<=>";
    while(temp != NULL)
    {
        cout<<"| "<<temp->data<<" |<=>";
        temp = temp->next;
    }
    cout<<"NULL\n";
}

template<class T>
int DoublyLLL<T> ::Count()
{
    return this->iCount;
}

///////////////////////////////////////////////////////////////////////
//          Singly Circular LinkedList using Generic Approach
///////////////////////////////////////////////////////////////////////

#pragma pack(1)
template<class T>
class SinglyCLLnode
{
    public:
        T data;
        SinglyCLLnode<T> *next;

        SinglyCLLnode(T no)
        {
            this->data = no;
            this->next = NULL;
        }
};

template<class T>
class SinglyCLL
{
    private:
        SinglyCLLnode<T> * first;
        SinglyCLLnode<T> * last;
        int iCount;

    public:
        SinglyCLL();

        void InsertFirst(T);
        void InsertLast(T);
        void InsertAtPos(T,int);

        void DeleteFirst();
        void DeleteLast();
        void DeleteAtPos(int);

        void Display();
        int Count();
};

template<class T>
SinglyCLL<T> :: SinglyCLL()
{
    cout<<"Object of SinglyCLL gets created.\n";

    this->first = NULL;
    this->last = NULL;
    this->iCount = 0;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     InsertFirst
//
/////////////////////////////////////////////////////////////////////////////
template<class T>
void SinglyCLL<T> :: InsertFirst(T no)
{
    SinglyCLLnode<T> * newn = new SinglyCLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
        this->last = newn;
        newn->next = newn;
    }
    else
    {
        newn->next = this->first;
        this->first = newn;
        this->last->next = this->first;
    }

    this->iCount++;
}

template<class T>
void SinglyCLL<T> :: InsertLast(T no)
{
    SinglyCLLnode<T> * newn = new SinglyCLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
        this->last = newn;
        newn->next = newn;
    }
    else
    {
        this->last->next = newn;
        this->last = newn;
        this->last->next = this->first;
    }

    this->iCount++;
}

template<class T>
void SinglyCLL<T> :: DeleteFirst()
{
    if(this->first == NULL)
    {
        return;
    }
    else if(this->first == this->last)
    {
        delete this->first;
        this->first = NULL;
        this->last = NULL;
    }
    else
    {
        SinglyCLLnode<T> * temp = this->first;

        this->first = this->first->next;
        delete temp;
        this->last->next = this->first;
    }

    this->iCount--;
}

template<class T>
void SinglyCLL<T> :: DeleteLast()
{
    if(this->first == NULL)
    {
        return;
    }
    else if(this->first == this->last)
    {
        delete this->first;
        this->first = NULL;
        this->last = NULL;
    }
    else
    {
        SinglyCLLnode<T> * temp = this->first;

        while(temp->next != this->last)
        {
            temp = temp->next;
        }

        delete this->last;
        this->last = temp;
        this->last->next = this->first;
    }

    this->iCount--;
}

template<class T>
void SinglyCLL<T> :: InsertAtPos(T no,int pos)
{
    if(pos < 1 || pos > this->iCount + 1)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        InsertFirst(no);
    }
    else if(pos == this->iCount + 1)
    {
        InsertLast(no);
    }
    else
    {
        SinglyCLLnode<T> * newn = new SinglyCLLnode<T>(no);
        SinglyCLLnode<T> * temp = this->first;

        for(int i = 1; i < pos - 1; i++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        temp->next = newn;

        this->iCount++;
    }
}

template<class T>
void SinglyCLL<T> :: DeleteAtPos(int pos)
{
    if(pos < 1 || pos > this->iCount)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        DeleteFirst();
    }
    else if(pos == this->iCount)
    {
        DeleteLast();
    }
    else
    {
        SinglyCLLnode<T> * temp = this->first;

        for(int i = 1; i < pos - 1; i++)
        {
            temp = temp->next;
        }

        SinglyCLLnode<T> * target = temp->next;
        temp->next = target->next;
        delete target;

        this->iCount--;
    }
}

template<class T>
void SinglyCLL<T> :: Display()
{
    if(this->first == NULL)
    {
        cout<<"Linked list is empty\n";
        return;
    }

    SinglyCLLnode<T> * temp = this->first;

    do
    {
        cout<<"| "<<temp->data<<" |-> ";
        temp = temp->next;
    } while(temp != this->first);

    cout<<"(First)\n";
}

template<class T>
int SinglyCLL<T> :: Count()
{
    return this->iCount;
}

///////////////////////////////////////////////////////////////////////
//          Doubly Circular LinkedList using Generic Approach
///////////////////////////////////////////////////////////////////////

#pragma pack(1)
template<class T>
class DoublyCLLnode
{
    public:
        T data;
        DoublyCLLnode<T> *next;
        DoublyCLLnode<T> *prev;

        DoublyCLLnode(T no)
        {
            this->data = no;
            this->next = NULL;
            this->prev = NULL;
        }
};

template<class T>
class DoublyCLL
{
    private:
        DoublyCLLnode<T> * first;
        DoublyCLLnode<T> * last;
        int iCount;

    public:
        DoublyCLL();

        void InsertFirst(T);
        void InsertLast(T);
        void InsertAtPos(T,int);

        void DeleteFirst();
        void DeleteLast();
        void DeleteAtPos(int);

        void Display();
        int Count();
};

template<class T>
DoublyCLL<T> :: DoublyCLL()
{
    cout<<"Object of DoublyCLL gets created.\n";

    this->first = NULL;
    this->last = NULL;
    this->iCount = 0;
}

/////////////////////////////////////////////////////////////////////////////
//
//  Function Name :     InsertFirst
//
/////////////////////////////////////////////////////////////////////////////

template<class T>
void DoublyCLL<T> :: InsertFirst(T no)
{
    DoublyCLLnode<T> * newn = new DoublyCLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
        this->last = newn;

        this->first->next = this->first;
        this->first->prev = this->first;
    }
    else
    {
        newn->next = this->first;
        newn->prev = this->last;

        this->first->prev = newn;
        this->last->next = newn;

        this->first = newn;
    }

    this->iCount++;
}

template<class T>
void DoublyCLL<T> :: InsertLast(T no)
{
    DoublyCLLnode<T> * newn = new DoublyCLLnode<T>(no);

    if(this->first == NULL)
    {
        this->first = newn;
        this->last = newn;

        this->first->next = this->first;
        this->first->prev = this->first;
    }
    else
    {
        newn->prev = this->last;
        newn->next = this->first;

        this->last->next = newn;
        this->first->prev = newn;

        this->last = newn;
    }

    this->iCount++;
}

template<class T>
void DoublyCLL<T> :: DeleteFirst()
{
    if(this->first == NULL)
    {
        return;
    }
    else if(this->first == this->last)
    {
        delete this->first;
        this->first = NULL;
        this->last = NULL;
    }
    else
    {
        DoublyCLLnode<T> * temp = this->first;

        this->first = this->first->next;

        this->first->prev = this->last;
        this->last->next = this->first;

        delete temp;
    }

    this->iCount--;
}

template<class T>
void DoublyCLL<T> :: DeleteLast()
{
    if(this->first == NULL)
    {
        return;
    }
    else if(this->first == this->last)
    {
        delete this->first;
        this->first = NULL;
        this->last = NULL;
    }
    else
    {
        DoublyCLLnode<T> * temp = this->last;

        this->last = this->last->prev;

        this->last->next = this->first;
        this->first->prev = this->last;

        delete temp;
    }

    this->iCount--;
}

template<class T>
void DoublyCLL<T> :: InsertAtPos(T no,int pos)
{
    if(pos < 1 || pos > this->iCount + 1)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        InsertFirst(no);
    }
    else if(pos == this->iCount + 1)
    {
        InsertLast(no);
    }
    else
    {
        DoublyCLLnode<T> * newn = new DoublyCLLnode<T>(no);
        DoublyCLLnode<T> * temp = this->first;

        for(int i = 1; i < pos - 1; i++)
        {
            temp = temp->next;
        }

        newn->next = temp->next;
        newn->prev = temp;

        temp->next->prev = newn;
        temp->next = newn;

        this->iCount++;
    }
}

template<class T>
void DoublyCLL<T> :: DeleteAtPos(int pos)
{
    if(pos < 1 || pos > this->iCount)
    {
        cout<<"Invalid position\n";
        return;
    }

    if(pos == 1)
    {
        DeleteFirst();
    }
    else if(pos == this->iCount)
    {
        DeleteLast();
    }
    else
    {
        DoublyCLLnode<T> * temp = this->first;

        for(int i = 1; i < pos - 1; i++)
        {
            temp = temp->next;
        }

        DoublyCLLnode<T> * target = temp->next;

        temp->next = target->next;
        target->next->prev = temp;

        delete target;
        this->iCount--;
    }
}

template<class T>
void DoublyCLL<T> :: Display()
{
    if(this->first == NULL)
    {
        cout<<"Linked list is empty\n";
        return;
    }

    DoublyCLLnode<T> * temp = this->first;

    cout<<"<=> ";
    do
    {
        cout<<"| "<<temp->data<<" |<=> ";
        temp = temp->next;
    } while(temp != this->first);

    cout<<"(First)\n";
}

template<class T>
int DoublyCLL<T> :: Count()
{
    return this->iCount;
}

///////////////////////////////////////////////////////////////////////
//          Stack using Generic Approach
///////////////////////////////////////////////////////////////////////

template<class T>
class Stacknode
{
    public:
        T data;
        Stacknode<T> *next;

        Stacknode(T no)
        {
            this -> data = no;
            this -> next = NULL;
        }
};

template<class T>
class Stack
{
    private:
        Stacknode<T> *first;
        int iCount;

    public:
        Stack();
        void push(T);            
        T pop();              
        T peep();
        void Display();
        int Count();
};

template<class T>
Stack<T> :: Stack()
{
    cout<<"Stack gets created successfully\n";
    this -> first = NULL;
    this -> iCount = 0;
}

template<class T>
void Stack<T> :: push(T no)
{
    Stacknode<T> *newn = NULL;

    newn = new Stacknode<T>(no);

    newn -> next = this -> first;
    this -> first = newn;

    this -> iCount++;

}   

template<class T>
T Stack<T> :: pop()  
{
    T Value = 0;
    Stacknode<T> *temp = this -> first;

    if(this -> first ==NULL)
    {
        cout<<"Stack is Empty\n";
        return -1;
    }

    Value = this -> first -> data;

    this -> first = this -> first -> next;

    delete temp;

    this -> iCount--;

    return Value;
}           

template<class T>
T Stack<T> :: peep()
{
    T Value = 0;

    if(this -> first ==NULL)
    {
        cout<<"Stack is Empty\n";
        return -1;
    }

    Value = this -> first -> data;
    return Value;
}

template<class T>
void Stack<T> :: Display()
{
    Stacknode<T> *temp = this -> first;

    if(this -> first == NULL)
    {
        cout<<"Stack is empty.\n";
        return;
    }

    while(temp != NULL)
    {
        cout<<"|\t"<<temp -> data<<"\t|\n";
        temp = temp -> next;
    }
}

template<class T>
int Stack<T> :: Count()
{
    return this -> iCount;
}

///////////////////////////////////////////////////////////////////////
//              Queue using Generic Approach
///////////////////////////////////////////////////////////////////////

#pragma pack(1)
template<class T>
class Queuenode
{
    public:
        T data;
        Queuenode<T> *next;

        Queuenode<T>(T no)
        {
            this -> data = no;
            this -> next = NULL;
        }
};

template<class T>
class Queue
{
    private:
        Queuenode<T> *first;
        Queuenode<T> *last;
        int iCount;

    public:
        Queue();

        void enqueue(T);            //InsertLast()
        T dequeue();                //DeleteFirst()
        void Display();
        int Count();
};

template<class T>
Queue<T> :: Queue()
{
    cout<<"Queue gets created successfully\n";
    this -> first = NULL;
    this -> last = NULL;
    this -> iCount = 0;
}

template<class T>
void Queue<T> :: enqueue(T no)
{
    Queuenode<T> *newn = NULL;

    newn = new Queuenode<T>(no);   

    if(this -> first == NULL && this -> last == NULL)
    {
        this -> first = newn;
        this -> last = newn;
    }
    else
    {
        this -> last -> next = newn;
        this -> last = this -> last -> next;
    }
    
    this -> iCount++;
}   

template<class T>
T Queue<T> :: dequeue()  
{
    int Value = 0;
    Queuenode<T> *temp = this -> first;

    if(this -> first ==NULL && this -> last == NULL)
    {
        cout<<"Queue is Empty\n";
        return -1;
    }

    Value = this -> first -> data;

    this -> first = this -> first -> next;

    delete temp;

    this -> iCount--;

    return Value;
} 

template<class T>
void Queue<T> :: Display()
{
    Queuenode<T> *temp = this -> first;

    if(this -> first == NULL && this -> last == NULL)
    {
        cout<<"Queue is empty.\n";
        return;
    }

    while(temp != NULL)
    {
        cout<<"| "<<temp -> data<<" | -";
        temp = temp -> next;
    }
    cout<<"\n";
}

template<class T>
int Queue<T> :: Count()
{
    return this -> iCount;
}

//////////////////////////////// End of Library //////////////////////////////////

int main()
{
    
    return 0;
}
