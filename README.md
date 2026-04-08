# Binary Search

I chose binary search as an algorithm because it is a highly efficient model for understanding algorithms. It easily mocks a way of searching for something that we mimic in real life, and is not so simple that it is just all math, but not so hard that it's unable to be understood by a beginner. It maps perfectly to the real-world scenario of finding a specific book on a library shelf.

## Demo Video

## Problem Breakdown & Computational Thinking

The binary search algorithm, given a sorted list of book titles and a target title which can be compared alphabetically, is done as follows:
1. define a right and left boundary. at first, these will be the very start and end of the bookshelf
2. find the middle index of the current shelf section
3. check book title at that middle index and compare it to the target book to make a decision:
    a) if the target book comes alphabetically _after_ the middle book, move the left boundary just past the middle (discard left half)
    b) if the target book comes alphabetically _before_ the middle book, move the right boundary just before the middle (discard right half)
    c) if the target is the same as the middle book
4. repeat this pattern until the target book is found, or until the left boundary crosses the right boundary (meaning target isnt on the shelf)

The goal is to create an app which someone can use to understand binary search conceptually. We want both the code and the app to be legible and provide lots of information without overwhelming the user. To achieve this, the complex mathematical details (such as array indexes and floor division) are stripped from the user interface. Instead of showing numbers, the user interface displays the laymans steps that occur, showing the "librarian's" (aka the algorithm's) decisions and how the physical search range is halfed each time.

The program is designed to start with a hardcoded, perfectly alphabetized array of 26 well-known book titles. The user enters a target string (the book they want to find) via the Gradio interface. The program processes this input by converting it to lowercase to avoid case-sensitivity errors , runs the binary search while loop, and outputs a formatted text log detailing the step-by-step journey of finding (or failing to find) the book.

## Steps to Run

Clone repository and install gradio using pip with:

```pip install gradio```

or

```python -m pip install gradio```

then run

```python app.py```

in the repository and follow the localhost link provided.

or:

follow the hugging face link below:

## Hugging Face Link

https://huggingface.co/spaces/gilliannj/cisc121librarysearch

## Author and Acknowledgement

Author: Gillian Jansen

Course: CISC 121

Acknowledgements: Gradio Documentation and help from Google's Gemini LLM for UI assistance, and class lecture slides/videos, as well as past student examples used for help to aid this project.
