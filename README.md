# Exercise 1.4 - Message

Write a program that asks the user to write a string. When the user has provided a string (i.e., written some text and pressed the enter key), the program should print the string that was provided by the user.

The exercise template comes with a program template that includes the function and its call.

```python
def main():
    message = input("Write a message...")
    # Write your code here

if __name__ == '__main__':
    main()
```

Example output for when the user writes "Bye".

```plaintext
Write a message:
*Bye*
Bye
```

Example output for when the user writes "Once upon a time...".

```plaintext
Write a message:
*Once upon a time...*
Once upon a time...
```

**Note:** Don't worry too much about `if __name__ == '__main__':` at the moment. We don't technically need it for this program, but it's good practise to include it and it'll be clearer in later exercises.
