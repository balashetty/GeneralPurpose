package com.shetty.code;

import java.util.Stack;

class InfixToPostfix {

    public String infixToPostfix(String expression) {
        StringBuilder postfix = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (char character : expression.toCharArray()) {
            if (Character.isLetterOrDigit(character)) {
                postfix.append(character);
            } else if (character == '(') {
                stack.push(character);
            } else if (character == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.append(stack.pop());
                }
                stack.pop(); 
            } else {
                while (!stack.isEmpty() && precedence(character) <= precedence(stack.peek())) {
                    postfix.append(stack.pop());
                }
                stack.push(character);
            }
        }

        while (!stack.isEmpty()) {
            postfix.append(stack.pop());
        }

        return postfix.toString();
    }

    private int precedence(char operator) {
        switch (operator) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
        }
        return -1;
    }

    public static void main(String[] args) {
        InfixToPostfix converter = new InfixToPostfix();
        String infixExpression = "A+B*(C^D-E)";
        String postfixExpression = converter.infixToPostfix(infixExpression);
        System.out.println("Infix Expression: " + infixExpression);
        System.out.println("Postfix Expression: " + postfixExpression);
    }
}
