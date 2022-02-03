class MinStack {
public:
    /** initialize your data structure here. */
    std::vector<int> myStack;

        MinStack(){
            
        }

        void push(int x){
            myStack.push_back(x);
        }   

        void pop(){
            myStack.pop_back();
        }

        int top(){
            return myStack.back();
        }

        int getMin(){
            int min = myStack[0];

            for (int i = 1; i < myStack.size(); i++){
                if (myStack[i] < min){
                    min = myStack[i];
                }
            }

            return min;
        }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */