int main()
{
    cout << "================ Singly Linear Linked List ================\n";
        SinglyLLL<int> sll;
        sll.InsertFirst(30);
        sll.InsertFirst(20);
        sll.InsertFirst(10);
        sll.InsertLast(40);
        sll.InsertAtPos(25, 3);
        sll.Display();
        cout << "Count: " << sll.Count() << "\n";

        sll.DeleteFirst();
        sll.DeleteLast();
        sll.DeleteAtPos(2);
        sll.Display();
        cout << "Count: " << sll.Count() << "\n\n";

        // ------------------------------------------------------------

        cout << "================ Doubly Linear Linked List ================\n";
        DoublyLLL<int> dll;
        dll.InsertFirst(20);
        dll.InsertFirst(10);
        dll.InsertLast(30);
        dll.InsertLast(40);
        dll.InsertAtPos(25, 3);
        dll.Display();
        cout << "Count: " << dll.Count() << "\n";

        dll.DeleteFirst();
        dll.DeleteLast();
        dll.DeleteAtPos(2);
        dll.Display();
        cout << "Count: " << dll.Count() << "\n\n";

        // ------------------------------------------------------------

        cout << "================ Singly Circular Linked List ================\n";
        SinglyCLL<int> scll;
        scll.InsertFirst(20);
        scll.InsertFirst(10);
        scll.InsertLast(30);
        scll.InsertLast(40);
        scll.InsertAtPos(25, 3);
        scll.Display();
        cout << "Count: " << scll.Count() << "\n";

        scll.DeleteFirst();
        scll.DeleteLast();
        scll.DeleteAtPos(2);
        scll.Display();
        cout << "Count: " << scll.Count() << "\n\n";

        // ------------------------------------------------------------

        cout << "================ Doubly Circular Linked List ================\n";
        DoublyCLL<int> dcll;
        dcll.InsertFirst(20);
        dcll.InsertFirst(10);
        dcll.InsertLast(30);
        dcll.InsertLast(40);
        dcll.InsertAtPos(25, 3);
        dcll.Display();
        cout << "Count: " << dcll.Count() << "\n";

        dcll.DeleteFirst();
        dcll.DeleteLast();
        dcll.DeleteAtPos(2);
        dcll.Display();
        cout << "Count: " << dcll.Count() << "\n\n";

        // ------------------------------------------------------------

        cout << "================ Stack =================\n";
        Stack<int> st;
        st.push(10);
        st.push(20);
        st.push(30);
        st.Display();
        cout << "Top element: " << st.peep() << "\n";
        cout << "Popped: " << st.pop() << "\n";
        st.Display();
        cout << "Count: " << st.Count() << "\n\n";

        // ------------------------------------------------------------

        cout << "================ Queue =================\n";
        Queue<int> q;
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        q.Display();
        cout << "Dequeued: " << q.dequeue() << "\n";
        q.Display();
        cout << "Count: " << q.Count() << "\n";

        cout << "\n================ All Tests Completed Successfully ================\n";
}